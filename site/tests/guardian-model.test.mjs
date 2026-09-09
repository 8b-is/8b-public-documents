import test from 'node:test';
import assert from 'node:assert/strict';
import { configuration, initialState, step, verdict, PRESETS, U32_MAX } from '../src/lib/guardian-model.mjs';

test('same Infant label hides a distinguishing 63 versus 0 stable streak', () => {
  const near = initialState(63);
  const fresh = initialState();
  assert.equal(near.stage, fresh.stage);
  assert.deepEqual(step(near, PRESETS.stable), {
    stage: 'EarlyChildhood', stable: 0, nonviable: 0, terminal: false, level: 'Safe',
  });
  assert.equal(step(fresh, PRESETS.stable).stage, 'Infant');
  assert.equal(step(fresh, PRESETS.stable).stable, 1);
  assert.equal(near.stable, 63, 'a step must not mutate the original state');
});

test('graduation occurs at 64, not 63, from a fresh state', () => {
  let state = initialState();
  for (let i = 0; i < 63; i++) state = step(state, PRESETS.stable);
  assert.equal(state.stage, 'Infant');
  assert.equal(state.stable, 63);
  state = step(state, PRESETS.stable);
  assert.equal(state.stage, 'EarlyChildhood');
  assert.equal(state.stable, 0);
});

test('a viable setback interrupts the streak and regresses the stage', () => {
  const config = configuration(3, 4);
  let state = initialState(2);
  state = step(state, PRESETS.viable, config);
  assert.equal(state.stable, 0);
  state = step(step(step(state, PRESETS.stable, config), PRESETS.stable, config), PRESETS.stable, config);
  assert.equal(state.stage, 'EarlyChildhood');
  state = step(state, PRESETS.viable, config);
  assert.equal(state.stage, 'Infant');
  assert.equal(state.nonviable, 0);
  assert.equal(verdict(state), 'Run', 'Caution runs despite failing the stability bar');
});

test('both kinds of viable cycle reset a nonviability streak', () => {
  const config = configuration(3, 3);
  for (const recovery of [PRESETS.stable, PRESETS.viable]) {
    let state = step(step(initialState(), PRESETS.nonviable, config), PRESETS.nonviable, config);
    state = step(state, recovery, config);
    assert.equal(state.nonviable, 0);
    state = step(step(state, PRESETS.nonviable, config), PRESETS.nonviable, config);
    assert.equal(state.terminal, false);
  }
});

test('Mercy occurs on the production boundary of 512 consecutive jitter misses', () => {
  let state = initialState(63);
  for (let i = 0; i < 511; i++) state = step(state, PRESETS.nonviable);
  assert.equal(state.stable, 0);
  assert.equal(state.nonviable, 511);
  assert.equal(verdict(state), 'Throttle(1)');
  state = step(state, PRESETS.nonviable);
  assert.equal(verdict(state), 'Terminate(NonViable)');
});

test('terminal verdict stays latched even if later note_cycle calls graduate', () => {
  const config = configuration(2, 2);
  let state = initialState();
  for (const input of [PRESETS.nonviable, PRESETS.nonviable, PRESETS.stable, PRESETS.stable]) {
    state = step(state, input, config);
  }
  assert.equal(state.stage, 'EarlyChildhood');
  assert.equal(state.nonviable, 0);
  assert.equal(verdict(state), 'Terminate(NonViable)');
});

test('top stage is capped and still resets its earned streak', () => {
  const config = configuration(2, 4);
  let state = initialState();
  for (let i = 0; i < 4; i++) state = step(state, PRESETS.stable, config);
  assert.equal(state.stage, 'EarlyChildhood');
  assert.equal(state.stable, 0);
});

test('all nonterminal safety verdicts reflect the supplied level', () => {
  for (const [level, expected] of Object.entries({ Safe: 'Run', Caution: 'Run', Warning: 'Throttle(1)', Critical: 'SkipCycle', Emergency: 'Quarantine' })) {
    assert.equal(verdict({ ...initialState(), level }), expected);
  }
});

test('invalid thresholds and unknown evidence are rejected instead of defaulted', () => {
  for (const invalid of [0, -1, NaN, Infinity, 2.5, '64']) {
    assert.throws(() => configuration(invalid, 4), RangeError);
    assert.throws(() => configuration(3, invalid), RangeError);
  }
  assert.throws(() => step(initialState(), { level: undefined, jitterViolation: false }), TypeError);
  assert.throws(() => step(initialState(), { level: 'Safe', jitterViolation: undefined }), TypeError);
});

test('nonviability counters saturate at the Rust u32 bound', () => {
  const state = { ...initialState(), nonviable: U32_MAX };
  assert.equal(step(state, PRESETS.nonviable).nonviable, U32_MAX);
});
