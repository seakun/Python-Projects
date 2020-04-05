# write your code here
field = input("Enter cells: ")
player_1 = "X"
player_2 = "O"

game_board = [[field[0], field[1], field[2]],
              [field[3], field[4], field[5]],
              [field[6], field[7], field[8]]]

print("---------")
print("| " + " ".join(game_board[0]) + " |")
print("| " + " ".join(game_board[1]) + " |")
print("| " + " ".join(game_board[2]) + " |")
print("---------")


def win_status(player):
    # check rows
    for row in game_board:
        if row.count(player) == 3:
            return True
    # check columns
    column = [[], [], []]
    for x in range(0, 3):
        for row in game_board:
            column[x].append(row[x])
        if column[x].count(player) == 3:
            return True
    # check diagonals
    diagonal_1 = [game_board[0][0], game_board[1][1], game_board[2][2]]
    diagonal_2 = [game_board[0][2], game_board[1][1], game_board[2][0]]
    if diagonal_1.count(player) == 3 or diagonal_2.count(player) == 3:
        return True


def finished(board):
    for i in range(len(board)):
        if "_" in board[i]:
            return True


def too_many(x, o):
    num_x = [square for row in game_board for square in row if square == x]
    num_y = [square for row in game_board for square in row if square == o]
    if abs(len(num_x) - len(num_y)) >= 2:
        return True


def print_outcome(x, o):
    win_status(x)
    win_status(o)
    if win_status(x) and win_status(o):
        print("Impossible")
    elif too_many(x, o) is True:
        print("Impossible")
    elif win_status(x):
        print(f"{x} wins")
    elif win_status(o):
        print(f"{o} wins")
    elif win_status(x) is not True and win_status(o) is not True:
        if finished(game_board) is True:
            print("Game not finished")
        else:
            print("Draw")

print_outcome(player_1, player_2)
