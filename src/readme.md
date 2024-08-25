# Programming plan

This project plans to use the OOP and event-driven frameworks in the
Python language. The app will run using the Pygame engine.

## Screens

* Main menu
* Tutorial
  * Mock game board that walks through how some of the basic FIDE pieces move
    * Rook (simplest piece, sliding pieces)
    * Knight (jumping pieces)
    * Pawn (different move/capture, promotion)
    * King (check, castling, checkmate)
    * Kick user back to main menu
* Options
  * Board theme/background
  * Display size, fullscreen
  * Audio
  * Assist mode (move and threat indicators)
  * Language (future)
* Local multiplayer
  * Hot seat
  * LAN
* Online multiplayer (future)

## Play and game UI

* The board state should be lightweight to facilitate passing board states
  around different functions.
  * Board state: wraps an 2D 8x8 int array.
  * Each int represents either a blank square or a piece; piece IDs will be
    entered into a global dictionary.
* During play, obviously the current board state is tracked in memory.
* After each move, the previous board state and the board state delta are
  stored in the undo cache.
  * Board state delta: pieces moved, pieces removed (e.g., capture), pieces
    added (e.g., promotion).
* The undo cache is a stack containing pairs of (board state, board state delta)
  to facilitate animations between board states.
