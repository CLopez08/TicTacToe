def get_names(two):
    name = []
    name.append(input("What is your name player1?\n"))
    if two == True:
        name.append(input("What is your name player2?\n"))
    else:
        name.append("Computer")
    return name

def check_for_winner(player_names, board):
    winner = "tie"
      #Check for horizontal victory player 1
    if board[1] == [3,'X','X','X']:
        winner = player_names[0]
    elif board[2] == [2,'X','X','X']:
        winner = player_names[0]
    elif board[3] == [1,'X','X','X']:
        winner = player_names[0]

    #Check for vertical victory player 1
    if board[1][1] == "X" and board[2][1] == "X" and board[3][1] == "X":
        winner = player_names[0]
    elif board[1][2] == "X" and board[2][2] == "X" and board[3][2] == "X":
        winner = player_names[0]
    elif board[1][3] == "X" and board[2][3] == "X" and board[3][3] == "X":
        winner = player_names[0]

    #Check for diagonal victory player 1
    if board[1][1] == "X" and board[2][2] == "X" and board [3][3] == "X":
        winner = player_names[0]
    elif board[3][1] == "X" and board[2][2] == "X" and board [1][3] == "X":
        winner = player_names[0]

        #Check for horizontal victory player 2
    if board[1] == [3,'O','O','O']:
        winner = player_names[1]
    elif board[2] == [2,'O','O','O']:
        winner = player_names[1]
    elif board[3] == [1,'O','O','O']:
        winner = player_names[1]

    #Check for vertical victory player 2
    if board[1][1] == "O" and board[2][1] == "O" and board[3][1] == "O":
        winner = player_names[1]
    elif board[1][2] == "O" and board[2][2] == "O" and board[3][2] == "O":
        winner = player_names[1]
    elif board[1][3] == "O" and board[2][3] == "O" and board[3][3] == "O":
        winner = player_names[1]

    #Check for diagonal victory player 2
    if board[1][1] == "O" and board[2][2] == "O" and board [3][3] == "O":
        winner = player_names[1]
    elif board[3][1] == "O" and board[2][2] == "O" and board [1][3] == "O":
        winner = player_names[1]

    return winner

def PvP_game():
    import random

    board = [
        ["Y",],
        [3,"_","_","_"],
        [2,"_","_","_"],
        [1,"_","_","_"],
        [" ",1,2,3,"X"]
        ]
    for list in board:
        print (*list, sep=' ')

    winner ="tie"
    two = True
    names = get_names(two)
    move_count = 0
    while move_count < 9:
        #Player 1 turn
        player1_row = int(input("{}, enter x-coordinante:\n".format(names[0])))
        player1_column = int(input("{}, enter y-coordinante:\n".format(names[0])))
        if player1_column == 3:
            player1_column = 1
        elif player1_column == 1:
            player1_column = 3
        board[player1_column][player1_row] = "X"
        for list in board:
            print (*list, sep=' ')
        move_count += 1
        if move_count == 9:
            break
        if move_count >= 5:
            winner = check_for_winner(names, board)
        if winner != "tie":
            break
      
        #Player 2 turn
        player2_row = int(input("{}, enter x-coordinate:\n".format(names[1])))
        player2_column = int(input("{}, enter y-coordinate:\n".format(names[1])))
        if player2_column == 3:
            player2_column = 1
        elif player2_column == 1:
            player2_column = 3
        board[player2_column][player2_row] = "O"
        for list in board:
            print (*list, sep=' ')
        move_count += 1
        if move_count >= 6:
            winner = check_for_winner(names, board)
        if winner != "tie":
            break

    if winner == "tie":
        print("Cat's game!")
    else:
        print("The winner is {}!".format(winner))
        
def PvC_game(games_won):
    import random

    board = [
        ["Y","Games won:", games_won],
        [3,"_","_","_"],
        [2,"_","_","_"],
        [1,"_","_","_"],
        [" ",1,2,3,"X"]
        ]
    
    for list in board:
        print (*list, sep=' ')
    winner ="tie"
    two = False
    names = get_names(two)
    move_count = 0
    while move_count < 9:
        #Player 1 turn
        player1_row = int(input("{}, enter x-coordinante:\n".format(names[0])))
        player1_column = int(input("{}, enter y-coordinante:\n".format(names[0])))
        if player1_column == 3:
            player1_column = 1
        elif player1_column == 1:
            player1_column = 3
        board[player1_column][player1_row] = "X"
        for list in board:
            print (*list, sep=' ')
        move_count += 1
        if move_count == 9:
            break
        if move_count >= 5:
            winner = check_for_winner(names, board)
        if winner != "tie":
            break

        #Computer Turn
        match = False
        while match == False:
            computer_x = random.randint(1,3)
            computer_y = random.randint(1,3)
            if board[computer_x][computer_y] == "_":
                board[computer_x][computer_y] = "O"
                match = True
        input("Computer is calculating move\n........")
        for list in board:
            print (*list, sep=' ')
        move_count += 1
        if move_count >= 5:
            winner = check_for_winner(names, board)
        if winner != "tie":
            break
    if winner == "tie":
        print("Cat's game!")
    elif winner == names[1]:
        print("You are such a loser")
    else:
        print("You win!")
        games_won += 1
    return games_won

def tic_tac():
    game_on = "y"
    games_won = 0
    while game_on == "y":
        game_type = int(input("How many players? 1 or 2\n"))
        if game_type == 1:
            games_won = PvC_game(games_won)
        else:
            PvP_game()
        game_on = input("Would you like to play again? y/n\n")

tic_tac()

