\ ============================================
\ Semantic Relaxation Field
\ RSVP-inspired scalar smoothing
\ ============================================

64 constant SIZE

create field SIZE cells allot
create nextf SIZE cells allot

: addr ( i -- a )
  cells field + ;

: naddr ( i -- a )
  cells nextf + ;

: init-field
  SIZE 0 do
    i 7 mod 20 * i xor
    i addr !
  loop ;

: sample ( i -- n )
  SIZE mod addr @ ;

: relax-at ( i -- n )
  dup 1- sample
  over sample +
  swap 1+ sample +
  3 / ;

: step
  SIZE 0 do
    i relax-at
    i naddr !
  loop

  SIZE 0 do
    i naddr @
    i addr !
  loop ;

: show
  cr
  SIZE 0 do
    i addr @ 8 / dup 9 >
    if drop [char] # else [char] . then
    emit
  loop cr ;

: run
  init-field
  40 0 do
    show
    step
  loop ;
