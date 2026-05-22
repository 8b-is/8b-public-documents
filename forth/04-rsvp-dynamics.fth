\ ============================================
\ RSVP toy dynamics
\ scalar Phi and vector v
\ ============================================

0 value phi
0 value vel

: update-vel
  phi 2 / neg
  vel + to vel ;

: update-phi
  vel + to phi ;

: dissipate
  vel 9 * 10 / to vel ;

: tick
  update-vel
  update-phi
  dissipate ;

: simulate
  100 to phi
  0 to vel

  40 0 do
    ." phi=" phi .
    ." vel=" vel .
    cr
    tick
  loop ;
