player = "X"
ai = "O"# this is the ai
move = 1 #any number just to declare it
winner = None
board = [""," "," "," ",
    " "," "," ",
    " "," "," "]
gameOver = False

#Detect if anyone has won yet
def playerWon():
    global winner 
    winner = None
    #Top Row
    if board[1] == board[2] and board[2] == board[3] and board[3] != " ":
        winner = board[1]
    #Middle Row
    if board[4] == board[5] and board[5] == board[6] and board[6] != " ":
        winner = board[4]
    #Bottom Row
    if board[7] == board[8] and board[8] == board[9] and board[9] != " ":
        winner = board[7]
    #Left Column
    if board[1] == board[4] and board[4] == board[7] and board[7] != " ":
        winner = board[1]
    #Middle Column
    if board[2] == board[5] and board[5] == board[8] and board[8] != " ":
        winner = board[2]
    #Right Column
    if board[3] == board[6] and board[6] == board[9] and board[9] != " ":
        winner = board[3]        
    #Top Right to Bottom Left Diagonal
    if board[3] == board[5] and board[5] == board[7] and board[7] != " ":
        winner = board[3]     
    #Top Left to Bottom Right Diagonal
    if board[1] == board[5] and board[5] == board[9] and board[9] != " ":
        winner = board[1]
    
    openSpots = 0
    for i in range(1,10):
        if board[i] == " ":
            openSpots +=1

    


    if winner == None and openSpots == 0:
        return "tie"

    else:
        return winner
    
    


#Displays the board
def printBoard():
    # for i in range(10):
    #         print ('\n')
    print("",board[1],"|",board[2],"|",board[3],
        "\n",board[4],"|",board[5],"|",board[6], 
        "\n",board[7],"|",board[8],"|",board[9])

def bestMove():
    bestscore = -1000000 
    move = 0
    for i in range(1,10):
        if board[i] == " ":
            board[i] = ai
            if (playerWon() == ai):
                return i
            score = minimax(board, False)
            print('position: ', i, 'score: ', score)
            board[i] = " "
            if(score >bestscore):
                bestscore = score
                move = i
    board[move] = ai
    
scores = {
    "X" : -1,
    "O" : 1,
    "tie" : 0
}

def minimax(board, aiTurnNext):
    result = playerWon()

    turn = {False: 'X', True: ai}

    #if the game is over, return the score
    if result != None:
        return scores[result]

    totalScore = 0
    for i in range(1,10):
        if board[i] == " ":
            board[i] = turn[aiTurnNext]
            score = minimax(board, not aiTurnNext)

            board[i] = " "
            totalScore += score

    return totalScore
                


    
#while computerPlaying != "y" or computerPlaying != "n":
print("Would you like to play against the computer(y/n)")
computerPlaying = input()

if computerPlaying == "y":
    while playerWon() == None:
        printBoard()

        print("Its your turn", player, "where would you like to move. ")
        Turn = int(input())

        #Check if turn is good
        if board[Turn] != " ":
            print("This move is already taken please choose another move")
            continue
        board[Turn] = player
        if playerWon() == None:
            bestMove() # this plays what the ai's best move is
        else:
            break
#X,O,tie, or None and tie x and o mean the game is over
    

#if playing without computer
else:
    while not gameOver:
        printBoard()
        print("Its your turn", player, "where would you like to move. ")
        Turn = int(input())

        #Check if turn is good
        if board[Turn] != " ":
            print("This move is already taken please choose another move")
            continue
        board[Turn] = player

        if player == "X":
            player = "O"
        else:
            player = "X"
        if playerWon() != None:
            break
  
printBoard()
print("Good Game,", playerWon(), "Has Won the Game")
