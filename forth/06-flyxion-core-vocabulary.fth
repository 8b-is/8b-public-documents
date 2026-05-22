\ ============================================================
\ FLYXION CORE VOCABULARY
\ Unified Experimental RSVP / CLIO / MEM|8 Framework
\ for pForth
\ ============================================================

only forth also definitions

vocabulary flyxion
flyxion definitions

\ ============================================================
\ GLOBAL FIELD CONFIGURATION
\ ============================================================

64 constant MAX-FIELD

create scalar-field MAX-FIELD cells allot
create vector-field MAX-FIELD cells allot
create entropy-field MAX-FIELD cells allot
create temp-field MAX-FIELD cells allot

0 value field-size
0 value tick-count

: saddr cells scalar-field + ;
: vaddr cells vector-field + ;
: eaddr cells entropy-field + ;
: taddr cells temp-field + ;

: field: ( n -- )
  to field-size ;

: zero-fields
  field-size 0 do
    0 i saddr !
    0 i vaddr !
    0 i eaddr !
    0 i taddr !
  loop ;

\ ============================================================
\ GENERIC DISPLAY SYSTEM
\ ============================================================

: .energy ( n -- )
  abs 4 / dup 9 >
  if
    drop [char] #
  else
    48 +
  then emit ;

: show-scalar
  cr
  field-size 0 do
    i saddr @ .energy
  loop cr ;

: show-entropy
  cr
  field-size 0 do
    i eaddr @ .energy
  loop cr ;

: show-vector
  cr
  field-size 0 do
    i vaddr @ .energy
  loop cr ;

: status
  cr
  ." tick=" tick-count .
  cr ." scalar : " show-scalar
  ." vector : " show-vector
  ." entropy: " show-entropy ;

\ ============================================================
\ RSVP INITIALIZATION
\ ============================================================

: randomize
  field-size 0 do
    i 17 * 53 + 97 mod
    i saddr !

    i 7 * 31 + 41 mod
    i vaddr !

    100 i -
    i eaddr !
  loop ;

: seed-wave
  zero-fields
  field-size 2 / dup
  200 swap saddr !

  field-size 3 / dup
  -80 swap vaddr !

  field-size 0 do
    80 i eaddr !
  loop ;

\ ============================================================
\ LOCAL NEIGHBOR OPERATORS
\ ============================================================

: left  ( i -- j )
  1- dup 0<
  if drop field-size 1- then ;

: right ( i -- j )
  1+ field-size mod ;

: avg3 ( a b c -- n )
  + + 3 / ;

: scalar-neighborhood ( i -- n )
  dup left saddr @
  over saddr @
  swap right saddr @
  avg3 ;

: entropy-neighborhood ( i -- n )
  dup left eaddr @
  over eaddr @
  swap right eaddr @
  avg3 ;

\ ============================================================
\ RSVP DYNAMICS
\ ============================================================

: update-vector ( i -- )
  dup scalar-neighborhood
  negate 3 /
  over vaddr @ +
  swap taddr ! ;

: update-scalar ( i -- )
  dup saddr @
  over vaddr @ +
  swap taddr ! ;

: update-entropy ( i -- )
  dup entropy-neighborhood
  over saddr @ abs 5 /
  -
  swap taddr ! ;

: commit-vector
  field-size 0 do
    i taddr @
    i vaddr !
  loop ;

: commit-scalar
  field-size 0 do
    i taddr @
    i saddr !
  loop ;

: commit-entropy
  field-size 0 do
    i taddr @
    i eaddr !
  loop ;

: step-vector
  field-size 0 do
    i update-vector
  loop
  commit-vector ;

: step-scalar
  field-size 0 do
    i update-scalar
  loop
  commit-scalar ;

: step-entropy
  field-size 0 do
    i update-entropy
  loop
  commit-entropy ;

: dissipate
  field-size 0 do
    i vaddr @
    9 * 10 /
    i vaddr !
  loop ;

: tick
  step-vector
  step-scalar
  step-entropy
  dissipate
  1 +to tick-count ;

\ ============================================================
\ CLIO PROJECTION OPERATORS
\ ============================================================

: parity-class ( n -- m )
  2 mod ;

: magnitude-class ( n -- m )
  abs 10 / ;

: projection ( n -- a b )
  dup parity-class
  swap magnitude-class ;

: classify-field
  cr
  field-size 0 do
    i saddr @
    projection
    ." [" i .
    ." p=" .
    ." m=" .
    ." ] "
  loop cr ;

\ ============================================================
\ MEM|8 WAVE MEMORY
\ ============================================================

: inject ( pos amp -- )
  swap saddr +! ;

: propagate
  field-size 1 do
    i saddr @
    i 1- saddr +!
  loop ;

: decay
  field-size 0 do
    i saddr @
    95 * 100 /
    i saddr !
  loop ;

: resonate
  propagate
  decay ;

\ ============================================================
\ SEMANTIC ATTRACTORS
\ ============================================================

: attractor ( n -- n )
  dup 20 <
  if 0 exit then

  dup 50 <
  if 32 exit then

  64 ;

: relax ( n -- n )
  dup attractor
  over -
  4 /
  - ;

: semantic-step
  field-size 0 do
    i saddr @
    relax
    i saddr !
  loop ;

\ ============================================================
\ CONSTRAINT TOPOLOGY
\ ============================================================

: admissible? ( n -- f )
  dup -200 >=
  swap 200 <= and ;

: constrain
  field-size 0 do
    i saddr @
    dup admissible? 0=
    if drop 0 then
    i saddr !
  loop ;

\ ============================================================
\ SEMANTIC MERGE ALGEBRA
\ ============================================================

: compatible? ( a b -- f )
  - abs 25 < ;

: merge ( a b -- c )
  2dup compatible?
  if + 2 /
  else 2drop 0
  then ;

: merge-fields
  field-size 0 do
    i saddr @
    i vaddr @
    merge
    i taddr !
  loop

  field-size 0 do
    i taddr @
    i saddr !
  loop ;

\ ============================================================
\ CATEGORY-THEORETIC MORPHISMS
\ ============================================================

: morphism: create , does> @ execute ;

: double 2 * ;
: increment 1+ ;
: negate-field negate ;

' double morphism: M2
' increment morphism: M1
' negate-field morphism: MN

: compose ( x xt1 xt2 -- y )
  rot swap execute
  swap execute ;

: morph-demo
  5 ['] M2 ['] M1 compose . ;

\ ============================================================
\ SHEAF-LIKE GLUING CONDITIONS
\ ============================================================

0 value overlap

: coherent? ( a b -- f )
  - abs overlap < ;

: glue-test
  field-size 1 do
    i saddr @
    i 1- saddr @
    coherent? 0=
    if
      ." obstruction@" i . cr
    then
  loop ;

\ ============================================================
\ MAIN EXECUTION MODES
\ ============================================================

: run
  0 to tick-count
  begin
    status
    tick
    constrain
    key?
  until ;

: semantic-run
  begin
    status
    semantic-step
    constrain
    key?
  until ;

: wave-run
  begin
    status
    resonate
    key?
  until ;

: merge-run
  begin
    status
    merge-fields
    key?
  until ;

forth definitions
