# KRZYŻYK I KÓŁKO

board = [" " for i in range(9)]


def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):
    if icon == "X":
        number = "1(X)"
    elif icon == "O":
        number = "2(O)"

    print("Your turn player {}".format(number))

    choise = int(input("Player {} enter your move (1-9): ".format(number)).strip())
    if board[choise -1] == " ":
        board[choise -1] = icon
        print_board()
        
    else:
        print()
        print("This spot is taken!")
        print()
        return("This spot is taken!")
    


def is_draw():
    if " " not in board:
        return True
    else:
        return False
               

        
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon or\
        board[3] == icon and board[4] == icon and board[5] == icon or\
        board[6] == icon and board[7] == icon and board[8] == icon or\
        board[0] == icon and board[3] == icon and board[6] == icon or\
        board[1] == icon and board[4] == icon and board[7] == icon or\
        board[2] == icon and board[5] == icon and board[8] == icon or\
        board[0] == icon and board[4] == icon and board[8] == icon or\
        board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

play = True

while True:

    if player_move("X")== "This spot is taken!":
        player_move("X")
        
    if is_victory("X"):
        print("Player X Wins!")
        anwser = input("Do you want to play again? (y/n): ").strip().lower()
        if anwser == "n":
            print("ok...")
            break
        else:
            i = 0
            while i <= 8:
                board[i] = " "
                i = i + 1
    
    elif is_draw():
        print("Is Draw!")
        anwser = input("Do you want to play again? (y/n): ").strip().lower()
        if anwser == "n":
            print("ok...")
            break
        else:
            i = 0
            while i <= 8:
                board[i] = " "
                i = i + 1
        
               
    
    if player_move("O")== "This spot is taken!":
        player_move("O")
        
    if is_victory("O"):
        print("Player O Wins!")
        anwser = input("Do you want to play again? (y/n): ").strip().lower()
        if anwser == "n":
            print("ok...")
            break
        else:
            i = 0
            while i <= 8:
                board[i] = " "
                i = i + 1
        
        
    elif is_draw():
        print("Is Draw!")
        anwser = input("Do you want to play again? (y/n): ").strip().lower()
        if anwser == "n":
            print("ok...")
            break
        else:
            i = 0
            while i <= 8:
                board[i] = " "
                i = i + 1
        
            


