'''------------------------------------------------- Start of the code -----------------------------------------------------'''

''' Tic Tac Toe (2 Player) Game '''

''' Functions '''

# to display board format
def board_format():
    # give the players an idea about the board format so that they can place their markers
    print('\t\t*** BOARD FORMAT ***')
    print('-------------------------------------------------------')
    print('1'+'|'+'2'+'|'+'3')
    print('-+-+-')
    print('4'+'|'+'5'+'|'+'6')
    print('-+-+-')
    print('7'+'|'+'8'+'|'+'9')
    print('-------------------------------------------------------')

# to display player board
def display_board(board):
    print('\n\t\t*** GAME BOARD ***\n')

    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])

# to let players choose their markers
def player_marker():
    print('-------------------------------------------------------')
    p1_marker = input("Player 1 Choose ( 'X' or 'O') : ").upper()
    if p1_marker == 'X':
        p2_marker = 'O'
    else:
        p2_marker = 'X'

    return (p1_marker,p2_marker)

# to start playing
def start_game():
    start = input("Would you like to start the game? ('Yes' or 'No') : ").lower()
    if start == 'yes':
        return True
    else:
        print('-------------------------------------------------------')
        print('\t ---> Make sure you play next time <---\n\t\t THANK YOU (^_^)')
        print('-------------------------------------------------------')

# to determine who goes first 
import random
def first_turn():
    flip = random.randint(1,2)

    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'

# to place marker at a position on the board
def place_marker(board,position,marker):
    board[position] = marker

# to check for win
def win_check(board,mark):
    win = False
    # conditions for win

    # case - 01 : all rows are same
    if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark):
        win = True
    #  case - 02 : all columns are same
    elif (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
        win = True
    #  case - 03 : all diagonals are same
    elif (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark) :
        win = True
    return win

# to check for tie
def tie_check(board):
    tie = False
    check = fullboard_check(board)
    if check == True:
       tie = True
    else:
        tie = False
    return tie

# to do a full board check
def fullboard_check(board):
    flag = 0
    for i in range(1,10):
        if board[i] != ' ':
            flag += 1
    if flag == 9:
        return True
    else:
        return False

# to ask whether they want to play again
def replay():
    choice = input("Do you want to play again? (Yes or No) : ").lower()
    if choice == 'yes':
        return True
    else:
        return False

'''  Main Game Code  '''
print('\n\n')
print('-------------------------------------------------------')
# greet the players
print('\t----> Welcome To Tic Tac Toe Game <----')

# dicplay them the board format 
print('-------------------------------------------------------')
board_format()

# ask them whether they want to start playing
game_on = start_game()

while game_on == True:

    # take input (X or O) from the players
    marker_selection = player_marker()
    (p1_marker,p2_marker) = marker_selection
    print('-------------------------------------------------------')
    print(f"\n\t*** Player 1 has choose '{p1_marker}' *** \n")
    print(f"\n\t*** Player 2 has choose '{p2_marker}' *** \n")
    print('-------------------------------------------------------')

# create board for the players
    board = [' '] * 10
    
# determine which player plays the first move 
    turn = first_turn()
    print(f'\n\t <- {turn} has the first turn -> \n ')
    
    while True:
        # Player 1 turn 
        if turn == 'Player 1':
            print('-------------------------------------------------------')
            # display game board
            board_format()
            display_board(board)

            # choose a position
            position = int(input(f"(P1) --> Place my marker [{p1_marker}] at : ")) 

            # place marker at a position
            place_marker(board,position,p1_marker)
            display_board(board)
            print('-------------------------------------------------------')

            # check for win or a tie
            win = win_check(board,p1_marker)       
            if win == True:
                print('\n\t Congratulations Player 1, YOU HAVE WON !!!\n\t') 
                print('-------------------------------------------------------')         
                game_on = False
                break
                
            # if not a win then check for tie 
            tie = tie_check(board)
            if tie == True:
                print('-------------------------------------------------------')
                print('\n\t It is a TIE !!!\n\t')
                print('-------------------------------------------------------')
                game_on = False
                break
                
                # if it is not a tie then pass the turn to player 2
            if win == False and tie == False:
                turn = 'Player 2'

      
        # Player 2 turn 
        else: # turn == 'Player 2':
            print('-------------------------------------------------------')
            # display game board 
            board_format()
            display_board(board)

            # choose a position
            position = int(input(f"(P2) --> Place my marker [{p2_marker}] at : ")) 

            # place marker at a position
            place_marker(board,position,p2_marker)
            display_board(board)
            print('-------------------------------------------------------')

            # check for win or a tie
            win = win_check(board,p1_marker)       
            if win == True:
                print('-------------------------------------------------------')
                print('\n\t Congratulations Player 2, YOU HAVE WON !!!\n\t')
                print('-------------------------------------------------------')          
                game_on = False
                break

            # if not a win then check for tie 
            tie = tie_check(board)
            if tie == True:
                print('-------------------------------------------------------')
                print('\n\t\t It is a TIE !!!\n')
                print('-------------------------------------------------------')
                game_on = False
                break

            # if it is not a tie then pass the turn to player 2
            if win == False and tie == False:
                turn = 'Player 1'

    play_again = replay()
    if play_again == True:
        game_on = True
    else:
        game_on = False
        print('-------------------------------------------------------')
        print('\n\t ^-^ THANK YOU FOR PLAYING ^-^ \n\t')
        print('-------------------------------------------------------')

            
'''-------------------------------------------------- End of the code -----------------------------------------------------'''
