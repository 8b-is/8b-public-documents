## Abstract

A controller can be simplified only relative to the behavior its specification requires it to preserve. This paper separates specification freedom from missing evidence, then distinguishes both from information lost through an inadequate state abstraction. AyeOS supplies two complementary cases: a proposed phase-evidence interface in which unknown phase must not become zero phase, and an implemented Guardian whose maturation label omits a counter needed to determine its next transition. A third, architectural case explains why refusal may leave material state unchanged while extending a durable decision history. Together these cases motivate an explicit observation contract covering both operational and audit behavior. Classical compatible-state reduction supplies relevant methods, but does not automatically interpret missing evidence or establish the correctness of a particular abstraction. Brief BBS and sound-driver comparisons illustrate the design vocabulary without asserting a shared intellectual history. The paper closes with a bounded verification proposal and an implementation-status table; no new exhaustive verification or preservation mechanism is claimed as a completed result.

## Specification Freedom and Missing Evidence

A specification may require one response, permit several responses, or forbid a response. Separately, a controller may lack evidence needed to determine which situation it occupies. The latter is an epistemic condition, not permission to choose the implementation’s most convenient value.

In classical incompletely specified sequential-machine minimization, unspecified behavior supplies implementation freedom subject to the specified behavior and consistency constraints. A missing sensor observation cannot simply be entered as such a don’t-care unless the modeling contract actually permits the resulting choices. If uncertainty matters, it must be modeled as an explicit input, state, or set of possible states before minimization is applied.

| Situation | Modeling obligation |
|:---|:---|
| Required behavior | Preserve the specified response. |
| Several permitted responses | Retain legitimate implementation freedom. |
| Unknown or missing evidence | Represent the uncertainty and define its handling. |
| Forbidden behavior | Exclude it under the stated environmental assumptions. |

For example, let $B$ be a set of physical states consistent with the available evidence, and let $A(s)$ be the actions permitted in state $s$. Under a contract requiring safety for every state still considered possible, a justified action must belong to

$$
A_{\mathrm{robust}}(B)=\bigcap_{s\in B}A(s).
$$

 This is an explicit robust-safety modeling choice, not a universal definition of admissibility. An empty intersection requires a specified resolution—such as requesting evidence, entering a protective mode, or escalating—rather than an arbitrary completion of the missing observation.

The distinction has an immediate AyeOS example. The proposed phase-time design uses an optional raw phase observation. Absence means unknown; it does not mean zero radians, in phase, or safe to combine coherently. A synthetic wave’s numerical phase is also not evidence of a measured phase. The document explicitly rejects zero as an unknown sentinel [\[5\]](#reference-5). This is a proposed interface and migration requirement, not a claim that every current wave or wire format already implements it.

A useful acceptance test follows directly: under a contract requiring validated phase evidence for coherent combination, replacing a missing observation with a numeric zero must not turn an ineligible combination into an eligible one. A known zero observation and an absent observation remain distinct even if a display initially renders both without an offset.

## The Guardian: A Label Is Not the Full State

The Guardian implementation inspected at AyeOS revision `9d052392` contains a maturation stage, consecutive-stability and nonviability counters, a wrapped watchdog, a terminal latch, configuration, and an observation counter [\[4\]](#reference-4). Its default graduation threshold is 64 qualifying stable cycles; its default Mercy threshold is 512 consecutive nonviable cycles.

Consider two nonterminal instances labeled `Infant`, with otherwise compatible conditions for the next qualifying stable cycle. One has accumulated 63 stable cycles and the other none. One more qualifying stable cycle advances the first to `EarlyChildhood`; the second remains `Infant`. Thus a single input extension distinguishes the instances when maturation stage is observable.

This is a counterexample to a label-only state abstraction. It does not demonstrate incomplete specification: a completely specified deterministic machine can contain states with the same current output and different future outputs. The missing distinction here is not missing sensor evidence. It is a known counter value discarded by an inadequate abstraction.

### Observable Behavior and Audit Behavior

Let $H_t$ denote a recorded sequence of boundary calls and their inputs through event position $t$, and let $\sigma_t$ be the implementation state after those calls. Replay additionally requires an initial state, fixed configuration, transition semantics, and any external inputs on which those calls depend. The counterexample uses the projection

$$
\alpha(\sigma)=\operatorname{stage}(\sigma).
$$

 The projection is adequate for displaying the present stage, but not for predicting its next required transition.

Define an observation contract $\mathcal O$ before deciding that states may be merged. For a deterministic, fully specified controller, let $\operatorname{Trace}_{\mathcal O}(\sigma,u)$ include current observations and observations after every prefix of an input sequence $u$. For states sharing the same admissible-input language, behavioral equivalence requires

$$
\sigma\equiv_{\mathcal O}\sigma'
\quad\Longleftrightarrow\quad
\forall u\in\mathcal U:\;
\operatorname{Trace}_{\mathcal O}(\sigma,u)
=\operatorname{Trace}_{\mathcal O}(\sigma',u).
$$

 If enabled inputs differ between states, the contract must also account for that difference. For nondeterministic or incompletely specified machines, equality of deterministic traces is replaced by the relevant compatibility or refinement obligation; the same equation must not be applied unchanged.

For the existing Guardian, candidate operational observations include the value returned by `stage()` and the verdict returned by `check_safety()`. Internal watchdog fields are not automatically public observations. For a future audited controller, the contract may additionally require decision reasons, policy identifiers, evidence references, and committed event positions. Those audit outputs are proposed extensions unless separately implemented and tested.

*Commitment Before Appearance* provides a useful companion model: material state $M_t$ and semantic state $S_t$ are different folds of one committed history [\[6\]](#reference-6). Two histories can yield the same display while differing in a refusal or authorization relevant to a later query. A representation sufficient for the display need not suffice for the audit. This does not prohibit efficient caches or state-based controllers; it requires their jurisdiction to be explicit.

### Refusal Can Commit a Record Without Executing an Action

For an illustrative refusal event $e_R$, the two-fold model permits

$$
H_{t+1}=H_t\mathbin{\|}e_R,\qquad
M_{t+1}=M_t,\qquad S_{t+1}\ne S_t.
$$

 The requested material effect is withheld, while the reason and occurrence of refusal become part of history. This is an architectural example, not a report of a new Guardian ledger implementation.

The word *commit* consequently needs an object. Committing an adjudication record is distinct from applying a candidate’s effects. Even permission to apply those effects does not imply execution:

$$
\operatorname{Apply}(a)\Rightarrow\operatorname{MayApply}(a),
\qquad
\operatorname{MayApply}(a)\not\Rightarrow\operatorname{Apply}(a).
$$

 This qualification preserves the useful record/admit/commit vocabulary without forcing refusal to mean historical silence.

The same distinction gives memory compression a concrete test. Suppose two records preserve the same association, but only one preserves a person’s contextual rejection of it. A later proposal to reuse that association requires different handling under a contract respecting that rejection. The records are then distinguishable for that task, even if their ordinary retrieval summaries coincide. A rejection is scoped to its subject, time, and context; it need not assert that the rejected proposition is universally false. The archival and current-authority distinction is consistent with the two-fold model, while a concrete MEM8 implementation still requires its own specification and tests.

## Reduction, Encoding, and Graph Analysis

State reduction asks which behavioral distinctions can be represented together. Encoding asks how to represent the resulting states economically. A smaller state count does not by itself establish a cheaper encoding or faster implementation.

In incompletely specified machines, compatibility need not be transitive. Compatible sets must respect jointly specified outputs and the successor obligations induced by future inputs. A closed cover covers the original states and, for each selected set and input, contains a selected set that includes all its specified successors. Covering successors individually across several unrelated sets does not satisfy that condition. Exact minimization may require nonmaximal compatibles; maximal compatibles alone are not a general exact solution [\[1\]](#reference-1), [\[2\]](#reference-2), [\[3\]](#reference-3).

Gray-style encoding can reduce switching along suitable transition paths. AMD’s synthesis guidance identifies long paths without branching as a suitable case [\[9\]](#reference-9). An arbitrary transition graph does not necessarily admit one-bit changes on every edge. For the current Rust controller, changing enum discriminants does not establish a benefit: instruction count, branching, footprint, and decoding cost must be measured. For a hardware implementation, gate and switching costs become additional relevant metrics.

A transition table and a directed graph can encode the same information. Graph representation makes reachability, cycles, and recovery paths convenient to analyze; it does not add semantics absent from the table. Visiting each state once is insufficient to test all transitions or relevant histories. A verification plan must include interrupted stability streaks, repeated failures, and whatever recovery or terminal behavior its contract actually specifies.

## Waiting, Authority, and Verification

### Unknown Evidence Requires a Defined Response

An explicit `HOLD` outcome can preserve evidence without applying a proposed effect. It must not be confused with deletion, a finding of falsehood, or a terminal stop. Nor does holding a candidate freeze the surrounding world: deadlines, incoming events, and recovery opportunities can continue to change.

A HOLD contract therefore needs an owner, a re-evaluation trigger, applicable deadlines, and an escalation or cancellation rule. Waiting is one possible specified response to uncertainty, not a universal safety guarantee. This paper proposes that distinction for future controller design; it does not add `HOLD` to the current Guardian verdict interface.

The evaluation boundary also needs protection. *The Verification Boundary* describes a feedback failure in which an accepted error becomes part of the machinery evaluating later claims [\[8\]](#reference-8). In a controller, the corresponding design obligation is to prevent a reinforcing pathway from unilaterally redefining the evidence or criteria that authorize its own influence. A candidate adversarial test repeats one source event through many derivations and checks that those copies do not count as independent warrant. This is an intended property to specify and test, not a theorem established by the analogy.

### A Bounded Experiment, Not a Full-System Proof

The actual Guardian is finite but contains wide counters and watchdog state; finite does not mean small enough for naive exhaustive enumeration. The proposed first experiment uses the same explicitly small threshold configuration in a reference model and the implementation. Graduation and nonviability thresholds such as 2, 3, and 4 permit short distinguishing traces. Enumerate an explicitly finite alphabet of cycle periods and jitter flags, with declared call order, and compare operational observations after every prefix up to a stated exploration depth.

This is exhaustive within the selected configurations, alphabet, and depth. It is not a proof for every period, call sequence, or production threshold. The reference model must represent the watchdog conditions needed to distinguish stable, unstable-but-viable, and nonviable cycles; replacing the watchdog by an unconstrained label requires its own abstraction justification.

Separate tests should exercise the production boundaries: graduation at 63/64 qualifying cycles, Mercy at 511/512 consecutive nonviable cycles, streak resets, and persistence of the terminal verdict. A counter abstraction for a general proof must preserve the transition and observation obligations, through a simulation or refinement argument appropriate to the property. Merely grouping counts 5 through 63 with an at-threshold value, or appealing to monotonicity without such an argument, does not preserve graduation timing.

Environmental assumptions must be listed, not invented as implementation guarantees. The Guardian API does not itself establish that callers invoke it only once per physical tick or never call `note_cycle` after terminal latching. The harness must either include those calls or justify their exclusion from the claimed scope.

### Implementation and Evidence Status

| Item | Status at inspected sources | Evidence obligation |
|:---|:---|:---|
| Streak-sensitive graduation | Implemented; 63/0 example follows from the code | Compare traces under declared inputs and configuration. |
| Unknown phase | Proposed interface and migration design | Validate missing versus measured zero; test domain and uncertainty checks. |
| Mercy | Terminal verdict is latched in the inspected Guardian | Do not claim durable preservation from termination alone. |
| Durable refusal and HOLD | Architectural examples in this paper | Implement event schema, reason, ordering, restart and timeout behavior before claiming delivery. |
| Guardian withdrawal | Future lifecycle requirement | Specify bounded authority, handoff, re-entry, and missing-telemetry behavior. |
| Bounded model exploration | Proposed; not executed for this paper | Publish model, alphabet, depth, configurations, traces, and counterexamples. |

*From Vocabulary to Kernel* motivates the distinction between design correspondence and demonstrated behavior [\[7\]](#reference-7). Its philosophical account cannot establish that a particular code revision has a preservation or withdrawal mechanism. The inspected maturation ladder contains Infant and EarlyChildhood; graduation is not itself a demonstrated retirement of the Guardian. Release evidence must identify the exact implementation and test result supporting each stronger claim.

## Brief Comparisons: BBS and Sound Drivers

The same questions can be posed in other domains without claiming a common intellectual history. In a BBS door interface, a session record can convey a remaining time allowance without itself specifying whether a new game round may begin. A hypothetical door contract must define that admission rule and what happens when the session disconnects. File transfer supplies another distinction: receiving bytes is not the same operation as verifying them. ZMODEM’s streaming and offset-based recovery illustrate an explicit recovery protocol rather than a universal per-block acknowledgment rule [\[10\]](#reference-10). These examples motivate contracts; they do not establish the behavior of every historical implementation.

For the MOS 6581 SID, the datasheet specifies that setting a voice’s Gate bit initiates Attack–Decay–Sustain and clearing it initiates Release [\[11\]](#reference-11). A driver contract can separately specify whether an incoming note retriggers, queues, or uses another voice. Silence in that contract is an unresolved design decision, not necessarily missing sensor evidence. The intended register writes, internally realized chip state, and musical intent must not be treated as interchangeable observations. A real-time budget encourages predictable handling but does not prove exhaustive coverage. These comparisons are subordinate to the Guardian and phase-evidence cases, whose source boundary is explicit.

## Conclusion

Unknown phase and a hidden streak counter are different errors waiting to happen: one replaces absent evidence with an asserted value; the other discards information already needed for a required transition. Durable refusal adds a third distinction: withholding an effect need not withhold its history. All three become checkable only after the required observations and permissible inputs have been stated.

The proposed contribution is therefore a scoped verification task rather than a universal minimization claim. Specify operational and audit behavior, distinguish current implementation from intended safeguards, compare a bounded reference model with implementation traces, and retain counterexamples to invalid abstractions. The experiment in Section [4.2](#a-bounded-experiment-not-a-full-system-proof) would supply evidence for exactly the configurations and executions examined. Any broader release claim must earn its own justification.

## References

### Reference 1

M. C. Paull and S. H. Unger. “Minimizing the Number of States in Incompletely Specified Sequential Switching Functions.” *IRE Transactions on Electronic Computers*, EC-8(3), 1959, pp. 356–367.

### Reference 2

A. Grasselli and F. Luccio. “A Method for Minimizing the Number of Internal States in Incompletely Specified Sequential Networks.” *IEEE Transactions on Electronic Computers*, EC-14(3), 1965, pp. 350–359.

### Reference 3

T. Villa, T. Kam, R. K. Brayton, and A. L. Sangiovanni-Vincentelli. *State Minimization of FSM’s with Implicit Techniques*. Memorandum UCB/ERL M96/17, 17 April 1996. <https://digicoll.lib.berkeley.edu/record/133866/files/ERL-96-17.pdf>.

### Reference 4

8b-is contributors. *AyeOS Guardian implementation*, `crates/mem8-safety/src/guardian.rs`, revision `9d052392a673d6aeebc69f1846f4ed1fb728e3f4`; inspected 9 September 2026. Repository access may be restricted. <https://github.com/8b-is/aye/blob/9d052392a673d6aeebc69f1846f4ed1fb728e3f4/crates/mem8-safety/src/guardian.rs>.

### Reference 5

Hue and Aye. *Phase-Time Domains and Observations—Design Spec*. 23 August 2026; status: Proposed. AyeOS, `docs/superpowers/specs/2026-08-23-phase-time-domain-design.md`, inspected at revision `9d052392`.

### Reference 6

Flyxion. *Commitment Before Appearance: Event Histories, Material State, and the Two Folds of a Layered World*. Unpublished manuscript, September 2026; supplied source `00011581-commitment-before-appearance.tex`.

### Reference 7

Flyxion. *From Vocabulary to Kernel*. Unpublished companion manuscript; reviewed revision 9 September 2026, based on supplied source `00001742-vocabulary-to-kernel.tex`.

### Reference 8

Flyxion. *The Verification Boundary*. Unpublished manuscript; supplied source `00000075-verification-boundary.tex`, inspected 9 September 2026.

### Reference 9

AMD. “Gray State Encoding.” *Vivado Design Suite User Guide: Synthesis*, UG901. <https://docs.amd.com/r/en-US/ug901-vivado-synthesis/Gray-State-Encoding>.

### Reference 10

C. Forsberg. *The ZMODEM Inter Application File Transfer Protocol*. Omen Technology Inc., 1988 (revised).

### Reference 11

MOS Technology. *MOS 6581 SID (Sound Interface Device) Datasheet*, including Appendix B, “SID Envelope Generators.”
