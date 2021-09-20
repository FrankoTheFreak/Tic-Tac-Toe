
# Tic Tac Toe

Creating a two player tic tac toe game.
### Thought Process

1. Display board format and instructions to the players.
2. Ask them whether they want to start  playing.
3. If yes then make player1 choose marker (X or O) and assign player2 his marker likewise.
4. Determine who gets to play the first move.
5. Depending upon who gets the first turn (e.g player1) display board format & game board and ask him to place their marker
6. Now go to next player ask him to place their marker.
7. Further after a marker is placed do a fullboard check to determine whether its a win or tie, if ts is none then let players continue playing.
8. Further incase of a win or tie display the winner or tie game.
9. After completion of one successful game ask them if they want to play again.
10. If yes then repeat the same process again else exit.


  
## Code Description

All the modules and functions in this project are explained below.

  
### Modules 

`import random`

Python random module is an in-built module which is used to generate random numbers. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc




  
### Functions

```bash
  def board format():
```

This function is used to display the board format to the players so that they have an idea that what number on numpad points to what location on the game board.

```bash
  def display_board(board):
```
This function takes the board as an argument and is used to display the game board to the players according to the markers that are present in the board argument that was passed to it. 

```bash
  def player_marker():
```
This function is used so that the players can choose their markers (X or O) and returns a tuple of (p1_marker,p2_marker) accordingly.

```bash
  def start_game():
```
This function is used to ask the players whether they want to start playing. If the answer is yes then it returns True and the game begins else it displays a thank you message.

```bash
  def first_turn():
```
This function is used along with random module and is used to determine which player gets to play the first move.

```bash
  def place_marker(board,position,marker):
```
This function takes three arguments board, position and marker and is used to place the marker (X or O) on the board at a position entered by the player.

```bash
  def win_check(board,mark):
```
This function takes two arguments board and mark and basically checks the board for all the possibilities in which a win can be declared. There are three cases for a win 1) a row has same marker in all three position 2) a column has same marker in all three position 3) a diagonal has same marker in all three position.

```bash
  def tie_check(board):
```
This function takes board as an argument and returns tie if all win conditions are false.

```bash
  def fullboard_check(board):
```
This function takes board as an argument and does a full board check and is used along with above function where the board is full yet no winner is identified and hence is used to determine that the game is a tie.

```bash
  def replay():
```
This function is used to ask the players if they are interested to play again after the completion of a game. If yes then it starts the game from the beginning.

### Screenshots

![ss1](https://user-images.githubusercontent.com/90572543/134028654-3eae7503-fe70-4870-817d-7a926d6897a3.PNG)

![ss2](https://user-images.githubusercontent.com/90572543/134028690-98178ebd-24ed-447d-87c7-e39e4df1da52.PNG)

![ss3](https://user-images.githubusercontent.com/90572543/134028730-8426156c-2d26-4c43-99a2-0180a3d4bda3.PNG)

![ss4](https://user-images.githubusercontent.com/90572543/134028778-ac591218-b17e-453b-9320-591708dfa8d8.PNG)

![ss5](https://user-images.githubusercontent.com/90572543/134028816-c342304d-0ce4-46d1-b972-60c730efa079.PNG)

![ss6](https://user-images.githubusercontent.com/90572543/134028841-5487d40d-9ebb-4b88-b3b5-c0c399cbdf3d.PNG)

### Conclusion

This is a two player tic tac toe which can be played in the command line on execution of this program.
  
