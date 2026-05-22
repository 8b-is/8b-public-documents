\ ============================================
\ Constraint-first automaton
\ ============================================

0 value state

: allowed? ( n -- f )
  dup 0 >=
  swap 9 <= and ;

: transition ( delta -- )
  state +
  dup allowed?
  if to state
  else drop
  then ;

: wander
  100 0 do
    state .
    i 3 mod 1- transition
  loop ;
