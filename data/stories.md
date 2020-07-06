## happy path
* greet
  - utter_greet
  
## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## check in path
* check_in
  - utter_check_in

## check out path
* check_out
  - utter_check_out
  
## cancel reservation path
* cancel_reservation
  - utter_cancel_reservation1
  - utter_cancel_reservation2
  
## cancel policy path
* cancel_policy
  - utter_cancel_policy
  
## resteraunt path
* resteraunt
  - utter_resteraunt
  
## resteraunt timing path
* restaurant_timing
  - utter_resteraunt_timing

## breakfast timing path
* breakfast_timing
  - utter_breakfast_timing

## breakfast path
* breakfast
  - utter_breakfast
  
## clean room1 path
* clean_room
  - utter_clean_room
* clean_room_rn
  - utter_clean_room_rn
  
## clean room right now path
* clean_room_rn
  - utter_clean_room_rn

## clean room2 path
* clean_room
  - utter_clean_room
* future_cleaning
  - action_schedule_cleaning
  
## clean room later path
* future_cleaning_single
  - action_schedule_cleaning
  

## book deluxe room path
* book_room
  - utter_book_room
* room{"room_numbers":"2"}
  - utter_book_room_type
* deluxe_room
  - utter_confirm_deluxe
  
## book simple room path
* book_room
  - utter_book_room
* room{"room_numbers":"2"}
  - utter_book_room_type
* simple_room
  - utter_confirm_simple 

## book deluxe room short path
* direct_room_booking{"room_numbers":"2"}
  - utter_book_room_type
* deluxe_room
  - utter_confirm_deluxe

## book simple room short path
* direct_room_booking{"room_numbers":"2"}
  - utter_book_room_type
* simple_room
  - utter_confirm_simple  

## direct duplex booking shortest path
* direct_deluxe_room{"room_numbers":"2"}
  - utter_confirm_deluxe
   
## direct simple booking shortest path
* direct_simple_room{"room_numbers":"2"}
  - utter_confirm_simple
      