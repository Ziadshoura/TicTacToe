Player = "X"

global computerPlaying 
computerPlaying = ""
X = [""," "," "," ",
    " "," "," ",
    " "," "," "]
#Detect if anyone has won yet
def PlayerWon():
    #Top Row
    if X[1] == X[2] and X[2] == X[3] and X[3] != " ":
        return True
    #Middle Row
    elif X[4] == X[5] and X[5] == X[6] and X[6] != " ":
        return True
    #Bottom Row
    elif X[7] == X[8] and X[8] == X[9] and X[9] != " ":
        return True
    #Left Column
    elif X[1] == X[4] and X[4] == X[7] and X[7] != " ":
        return True
    #Middle Column
    elif X[2] == X[5] and X[5] == X[8] and X[8] != " ":
        return True
    #Right Column
    elif X[3] == X[6] and X[6] == X[9] and X[9] != " ":
        return True        
    #Top Right to Bottom Left Diagonal
    elif X[3] == X[5] and X[5] == X[7] and X[7] != " ":
        return True     
    #Top Left to Bottom Right Diagonal
    elif X[1] == X[5] and X[5] == X[9] and X[9] != " ":
        return True


#Displays the board
def printBoard():
    for i in range(10):
            print ('\n')
    print("",X[1],"|",X[2],"|",X[3],
        "\n",X[4],"|",X[5],"|",X[6], 
        "\n",X[7],"|",X[8],"|",X[9])


#while computerPlaying != "y" or computerPlaying != "n":
print("Would you like to play against the computer(y/n)")
computerPlaying = input()
print(computerPlaying)

if computerPlaying == "y":

    printBoard()
     


#if
else:
    while not PlayerWon():
        printBoard()
        print("Its your turn", Player, "where would you like to move. ")
        Turn = int(input())

        #Check if turn is good
        if X[Turn] != " ":
            print("This move is already taken please choose another move")
            continue
        X[Turn] = Player

        if Player == "X":
            Player = "O"
        else:
            Player = "X"


if Player == "X":
        Player = "O"
else:
        Player = "X"   
printBoard()
print("Good Game,", Player, "Has Won the Game")

