# A friendly game of Tic-Tac-Toe! 
# By: Kelley Robertson


def main():

    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

    user = True # When true it referes to X, otherwise O.
    turns = 0

    while turns < 9: 
        active_user = current_user(user)
        print_board(board)
        user_input = input("Please enter a position 1 through 9 or enter \"q\" to quit: ")
        if quit(user_input): break
        if not check_input(user_input):
            print("Please try again.")
            continue
        user_input = int(user_input) - 1
        coords = coordinates(user_input)
        if is_taken(coords, board):
            print("Please Try again.")
            continue
        add_to_board(coords, board, active_user)
        if is_win(active_user, board):
            print_board(board)
            print(f"{active_user.upper()} Won!!")
            break
        turns += 1
        if turns == 9: print("Its a draw!")
        user = not user

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot}|", end="")
        print()
        print("-+-+-")

def quit(user_input):
    if user_input.lower() == "q": 
        print("Thanks for playing!")
        return True
    else: return False

def check_input(user_input):
    # Check if its a number.
    if not is_num(user_input): return False
    user_input = int(user_input)
    # check if its 1-9
    if not boundry(user_input): return False
    return True

def is_num(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def boundry(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else: return True

def is_taken(coords, board):
    row = coords [0]
    col = coords [1]
    if board [row] [col] != "-":
        print("This position is already taken.")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int (col % 3)
    return (row, col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return "X"
    else: return "O"

def is_win(user, board):
    if check_row(user, board): return True
    if check_col(user, board): return True
    if check_diagnol(user, board): return True
    return False

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False

def check_col(user, board):
    for col in range (3):
        complete_col = True
        for row in range (3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diagnol(user, board):
    # From top left to bottom right
    if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False

if __name__ == "__main__":
    main()