\ ============================================
\ CLIO-style Projection Operator
\ Constraint-preserving reduction
\ ============================================

: parity-class ( n -- m )
  2 mod ;

: magnitude-class ( n -- m )
  abs 10 / ;

: clio-project ( n -- a b )
  dup parity-class
  swap magnitude-class ;

: classify
  cr
  50 0 do
    i clio-project
    ." State "
    i .
    ." -> parity="
    .
    ." magnitude="
    .
    cr
  loop ;
