# write your code here
user_field = "_" * 9
game_board = []
game_status = []
player_1 = "X"
player_2 = "O"


def print_field(field, current_player):
    global game_board
    global user_field
    coordinates = list()
    game_board = [[field[0], field[1], field[2]],
                  [field[3], field[4], field[5]],
                  [field[6], field[7], field[8]]]

    def printer(board):
        print("---------")
        print("| " + " ".join(board[0]) + " |")
        print("| " + " ".join(board[1]) + " |")
        print("| " + " ".join(board[2]) + " |")
        print("---------")

    if user_field == "_" * 9:
        printer(game_board)  # print before input only if board is empty

    field = input("Enter the coordinates: ").split()

    def validation(user_input):
        # validate input type
        for item in user_input:
            if item.isnumeric():
                if 1 <= int(item) <= 3:
                    # - 1 to match matrix coordinate (0-2 vs 1-3)
                    coordinates.append(int(item) - 1)
                else:
                    print("Coordinates should be from 1 to 3!")
                    coordinates.clear()
                    return False
            else:
                print("You should enter numbers!")
                coordinates.clear()
                return False
        del coordinates[2:]
        # adjust coordinates for matrix output
        coordinates[1] = abs(coordinates[1] - 2)
        coordinates.reverse()
        if game_board[coordinates[0]][coordinates[1]] == "_":
            # trim extra input items if coordinate list is too long
            return coordinates, True
        else:
            print("This cell is occupied! Choose another one!")
            coordinates.clear()
            return False

    while validation(field) is False:
        field = input("Enter the coordinates: ").split()

    # update game board with new move
    game_board[coordinates[0]][coordinates[1]] = current_player
    printer(game_board)
    user_field = "".join(game_board[0]) + "".join(game_board[1]) + "".join(game_board[2])
    return field, user_field


def print_game_status():
    global game_status

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
                return False

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
            if finished(game_board) is False:
                # print("Game not finished")
                pass
            else:
                print("Draw")
                game_status.append(True)

    game_status = [win_status(player_1), win_status(player_2),
                   finished(game_board), too_many(player_1, player_2)]
    print_outcome(player_1, player_2)
    return game_status


def make_move(player):
    print_field(user_field, player)
    print_game_status()


while any(game_status) is not True:
    make_move(player_1)
    if any(game_status) is not True:
        make_move(player_2)