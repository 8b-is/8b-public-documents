# Flyxion pForth Experimental Suite

Experimental pForth programs encoding core motifs from the RSVP, CLIO,
MEM|8, TARTAN, and constraint-first frameworks.

## Files

| File | Description |
|------|-------------|
| 01-semantic-relaxation.fth | RSVP-inspired 1D scalar smoothing field. High-frequency distinctions collapse into mesoscale attractors without a global controller. Run with `run`. |
| 02-clio-projection.fth | CLIO-style projection operator. Maps high-dimensional states onto compressed admissibility classes (parity + magnitude). Run with `classify`. |
| 03-constraint-automaton.fth | Constraint-first automaton. Admissibility relation is primary; reachable state ontology is derived. Run with `wander`. |
| 04-rsvp-dynamics.fth | Scalar Phi / vector vel toy dynamics with dissipation. Damped oscillation toward entropic stability. Run with `simulate`. |
| 05-experimental-suite.fth | Full 11-program suite: TARTAN tiling, MEM|8 wave memory, semantic attractor engine, constraint rewrite system, sheaf gluing, manifold projection, salience detector, entropy computer, cellular RSVP lattice, merge algebra, monoidal category interpreter. |
| 06-flyxion-core-vocabulary.fth | Unified framework. All systems share scalar, vector, and entropy fields with a common `field:`, `step`, `show`, `status`, and `run` interface. Loads into a `flyxion` vocabulary. |

## Usage

Load any file into pForth with `include filename.fth`, then call the
top-level entry word listed above.

For the core vocabulary, set the field size before running:

```
include 06-flyxion-core-vocabulary.fth
flyxion definitions
32 field: randomize run
```

Or seed a wave and run the wave propagator:

```
32 field: seed-wave wave-run
```

## Design Notes

- All programs use only integer arithmetic (no floats).
- Boundary conditions are toroidal (wraparound) unless otherwise noted.
- The core vocabulary uses a double-buffered temp-field to avoid
  in-place update artifacts during field evolution.
- `constrain` acts as an admissibility gate after each tick.
- `glue-test` detects sheaf-theoretic obstructions (discontinuities)
  across neighboring cells.
