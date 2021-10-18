
the_board = {
    "7": "", "8": "", "9": "",
    "4": "", "5": "", "6": "",
    "1": "", "2": "", "3": "",
}


def print_board(board):
    print(f'{board["7"]} | {board["8"]} | {board["9"]}')
    print("- - - -")
    print(f'{board["4"]} | {board["5"]} | {board["6"]}')
    print("- - - -")
    print(f'{board["1"]} | {board["2"]} | {board["3"]}')


def game():
    turn = "X"
    count = 0

    for i in range(9):
        print_board(the_board)
        print(f"It's {turn}'s turn")

        user_move = input("Pick a number between 1 and 9: ")

        try:
            if the_board[user_move] == "":
                the_board[user_move] = turn
                count += 1
            else:
                print("That spot is occupied, try again.")
        except KeyError:
            print("Please enter numbers between 1 and 9")

        if count >= 5:
            if the_board["1"] == the_board["2"] and the_board["3"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["4"] == the_board["5"] and the_board["6"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["7"] == the_board["8"] and the_board["9"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["1"] == the_board["4"] and the_board["7"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["2"] == the_board["5"] and the_board["8"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["3"] == the_board["6"] and the_board["9"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["1"] == the_board["5"] and the_board["9"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
            elif the_board["7"] == the_board["5"] and the_board["3"]:
                print_board(the_board)
                print("Game over!")
                print(f"{turn} won!")
                break
        if count == 9:
            print_board(the_board)
            print("Game over!")
            print("We have a tie!")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"


if __name__ == "__main__":
    game()
