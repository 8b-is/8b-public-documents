\ ============================================================
\ Flyxion / RSVP / CLIO / MEM|8 Experimental pForth Suite
\ ============================================================

\ ------------------------------------------------------------
\ 1. TARTAN recursive tiling simulator
\ ------------------------------------------------------------

16 constant TILES
create tile TILES cells allot

: taddr cells tile + ;

: seed-tiles
  TILES 0 do
    i i * 7 + 31 mod i taddr !
  loop ;

: aura ( i -- n )
  dup taddr @
  swap 1+ TILES mod taddr @ +
  2 / ;

: retile
  TILES 0 do
    i aura
    i taddr !
  loop ;

: show-tiles
  cr TILES 0 do
    i taddr @ .
  loop cr ;

: tartan
  seed-tiles
  20 0 do
    show-tiles
    retile
  loop ;


\ ------------------------------------------------------------
\ 2. MEM|8-style wave memory experiment
\ ------------------------------------------------------------

32 constant MEM
create wave MEM cells allot

: waddr cells wave + ;

: inject ( pos amp -- )
  swap waddr +! ;

: decay
  MEM 0 do
    i waddr @ 9 * 10 / i waddr !
  loop ;

: spread
  MEM 1 do
    i waddr @
    i 1- waddr +!
  loop ;

: probe
  cr MEM 0 do
    i waddr @ abs 5 >
    if [char] * else [char] . then emit
  loop cr ;

: mem8
  MEM 0 do 0 i waddr ! loop
  8 40 inject
  22 -30 inject
  40 0 do
    probe
    spread
    decay
  loop ;


\ ------------------------------------------------------------
\ 3. Stack-based semantic attractor engine
\ ------------------------------------------------------------

: attract ( n -- n )
  dup 10 <
  if 0
  else dup 30 <
    if 20
    else 50
    then
  then ;

: semantic-step ( n -- n )
  dup attract
  over - 2 /
  - ;

: semantic-run
  73
  30 0 do
    dup .
    semantic-step
  loop drop ;


\ ------------------------------------------------------------
\ 4. Constraint-preserving rewrite system
\ ------------------------------------------------------------

: admissible? ( n -- f )
  dup 0 >= swap 100 <= and ;

: rewrite ( n -- n )
  dup 2 mod 0=
  if 3 / 7 +
  else 2 * 1+
  then
  dup admissible? 0=
  if drop 42 then ;

: rewrite-run
  17
  40 0 do
    dup .
    rewrite
  loop drop ;


\ ------------------------------------------------------------
\ 5. Tiny sheaf-gluing metaphor
\ ------------------------------------------------------------

0 value patch-a
0 value patch-b
0 value overlap

: compatible? ( -- f )
  patch-a patch-b + 2 / overlap = ;

: glue
  compatible?
  if ." sections glue" cr
  else ." obstruction detected" cr
  then ;

: sheaf-test
  10 to patch-a
  14 to patch-b
  12 to overlap
  glue
  10 to patch-a
  20 to patch-b
  12 to overlap
  glue ;


\ ------------------------------------------------------------
\ 6. Projection/manifold compression
\ ------------------------------------------------------------

: pi ( x -- m )
  10 / ;

: same-fiber? ( x y -- f )
  pi swap pi = ;

: manifold-demo
  0 100 do
    i dup pi
    ." x=" swap .
    ." m=" .
    cr
  7 +loop ;


\ ------------------------------------------------------------
\ 7. Marine-style salience detector
\ ------------------------------------------------------------

0 value last
0 value jitter

: observe ( x -- )
  dup last -
  abs to jitter
  to last ;

: salient? ( -- f )
  jitter 12 > ;

: marine-demo
  0 to last
  0 to jitter
  30 0 do
    i i * 17 mod observe
    salient?
    if ." !" else ." ." then
  loop cr ;


\ ------------------------------------------------------------
\ 8. Symbolic entropy computer
\ ------------------------------------------------------------

: choices->entropy ( n -- s )
  0 swap
  begin dup 1 >
  while
    2 /
    swap 1+ swap
  repeat
  drop ;

: entropy-demo
  1
  12 0 do
    dup ." choices=" dup .
    choices->entropy ." entropy~" . cr
    2 *
  loop drop ;


\ ------------------------------------------------------------
\ 9. Cellular RSVP lattice
\ ------------------------------------------------------------

32 constant N
create phi N cells allot
create ent N cells allot

: paddr cells phi + ;
: eaddr cells ent + ;

: init-rsvp
  N 0 do
    i 5 mod 20 * i paddr !
    100 i - i eaddr !
  loop ;

: rsvp-cell ( i -- )
  dup paddr @
  over eaddr @ 10 /
  -
  swap paddr ! ;

: rsvp-step
  N 0 do i rsvp-cell loop ;

: rsvp-show
  cr N 0 do
    i paddr @ 10 >
    if [char] # else [char] . then emit
  loop cr ;

: rsvp-run
  init-rsvp
  30 0 do
    rsvp-show
    rsvp-step
  loop ;


\ ------------------------------------------------------------
\ 10. Semantic merge algebra prototype
\ ------------------------------------------------------------

: conflict? ( a b -- f )
  - abs 20 > ;

: merge ( a b -- c )
  2dup conflict?
  if 2drop -1
  else + 2 /
  then ;

: merge-demo
  10 12 merge .
  10 80 merge .
  40 50 merge . ;


\ ------------------------------------------------------------
\ 11. Tiny monoidal category interpreter
\ ------------------------------------------------------------

: id ;
: tensor ( a b -- a+b ) + ;
: compose ( x f -- y ) execute ;

: morph-a 2 * ;
: morph-b 3 + ;

: category-demo
  5 ['] morph-a compose .
  5 ['] morph-b compose .
  5 ['] morph-a compose
  ['] morph-b compose .
