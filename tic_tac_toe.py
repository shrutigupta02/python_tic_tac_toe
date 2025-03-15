import random

def display_board(board):
    print("+-------+-------+-------+")
    for i in range(len(board)):
        print("|       |       |       |")
        print("|  ",board[i][0],"  |   ",board[i][1]," |   ",board[i][2]," |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    inp = int(input("enter move:"))
    valid_moves = [cell for row in board for cell in row]
    if inp not in range(1,10) or inp not in valid_moves:
        enter_move(board)
        return
    for i in range(3):
        for j in range(3):
            if board[i][j] == inp:
                board[i][j] = "O" 
                return board


def make_list_of_free_fields(board):
    global free_fields
    free_fields = []

    for i in range(3):
        for j in range(3):
            if board[i][j] in range(1,10):
                free_fields.append((i,j))
            continue

def computer_move(board):
    move_row = 1
    move_col = 1
    while (move_row, move_col) not in free_fields:
        move_row = random.randint(0,2)
        move_col = random.randint(0,2)
    board[move_row][move_col] = "X"
    return board
                
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
            
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True
        
    return False
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


board = [[1,2,3], [4,'X',6], [7,8,9]]
make_list_of_free_fields(board)
while len(free_fields) != 0:
    display_board(board)
    board = enter_move(board)
    make_list_of_free_fields(board)
    if victory_for(board, 'O'):
        print("You win!")
        break;
    board = computer_move(board)
    make_list_of_free_fields(board)
    if victory_for(board, 'X'):
        print("You lost!")
        break;
else:
    print("Draw!")

display_board(board)
