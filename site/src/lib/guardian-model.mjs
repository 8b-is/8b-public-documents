/**
 * Educational projection of Guardian::note_cycle/check_safety at 9d052392.
 * Inputs supply the level AFTER record_cycle. This is not a watchdog model,
 * nor a claim that every sequence of supplied levels is physically reachable.
 */
export const U32_MAX = 0xffff_ffff;
export const LEVELS = Object.freeze(['Safe', 'Caution', 'Warning', 'Critical', 'Emergency']);
export const PRESETS = Object.freeze({
  stable: Object.freeze({ label: 'Stable · Safe, no jitter miss', level: 'Safe', jitterViolation: false }),
  viable: Object.freeze({ label: 'Setback · Caution, no jitter miss', level: 'Caution', jitterViolation: false }),
  nonviable: Object.freeze({ label: 'Nonviable · Warning, jitter miss', level: 'Warning', jitterViolation: true }),
});

function natural(value, name, minimum = 0) {
  if (!Number.isSafeInteger(value) || value < minimum || value > U32_MAX) {
    throw new RangeError(`${name} must be an integer from ${minimum} to ${U32_MAX}.`);
  }
  return value;
}

export function configuration(graduation = 64, mercy = 512) {
  return Object.freeze({
    graduation: natural(graduation, 'Graduation threshold', 1),
    mercy: natural(mercy, 'Mercy threshold', 1),
  });
}

export function initialState(stable = 0) {
  return { stage: 'Infant', stable: natural(stable, 'Stable streak'), nonviable: 0, terminal: false, level: 'Safe' };
}

export function verdict(state) {
  if (state.terminal) return 'Terminate(NonViable)';
  const result = {
    Safe: 'Run', Caution: 'Run', Warning: 'Throttle(1)',
    Critical: 'SkipCycle', Emergency: 'Quarantine',
  }[state.level];
  if (!result) throw new TypeError('Unknown watchdog level.');
  return result;
}

export function step(state, input, config = configuration()) {
  if (!LEVELS.includes(input.level) || typeof input.jitterViolation !== 'boolean') {
    throw new TypeError('A cycle needs a known post-watchdog level and a boolean jitter flag.');
  }
  configuration(config.graduation, config.mercy);
  if (!['Infant', 'EarlyChildhood'].includes(state.stage)) throw new TypeError('Unknown maturation stage.');
  natural(state.stable, 'Stable streak');
  natural(state.nonviable, 'Nonviable streak');
  const next = { ...state, level: input.level };
  if (!input.jitterViolation && input.level === 'Safe') {
    next.stable = Math.min(U32_MAX, state.stable + 1);
    next.nonviable = 0;
    if (next.stable >= config.graduation) {
      next.stage = 'EarlyChildhood';
      next.stable = 0;
    }
  } else {
    next.stable = 0;
    next.stage = 'Infant';
    if (input.jitterViolation) {
      next.nonviable = Math.min(U32_MAX, state.nonviable + 1);
      if (next.nonviable >= config.mercy) next.terminal = true;
    } else {
      next.nonviable = 0;
    }
  }
  // Deliberately no early return on terminal: the source still permits
  // note_cycle to change state, but check_safety retains the terminal verdict.
  return next;
}
