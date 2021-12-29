from tkinter import *
# setup gui
window = Tk()
window.title('TicTacToe')#create window and background
window.configure(background='White')
window.geometry('550x700')

buttons = []
label = Label(window, text= "")
label.grid(row=4, column=1,)

player = "X"
ai = "O"# this is the ai
move = 1 #any number just to declare it
winner = None
board = [""," "," "," ",
    " "," "," ",
    " "," "," "]
gameOver = False

def button1Logic():
    button_1["state"] = DISABLED
    button_1['text'] = player
    board[1] = player
    againstComputer()


def button2Logic():
    button_2["state"] = DISABLED
    button_2['text'] = player
    board[2] = player
    againstComputer()

def button3Logic():
    button_3["state"] = DISABLED
    button_3['text'] = player
    board[3] = player
    againstComputer()

def button4Logic():
    button_4["state"] = DISABLED
    button_4['text'] = player
    board[4] = player
    againstComputer()

def button5Logic():
    button_5["state"] = DISABLED
    button_5['text'] = player
    board[5] = player
    againstComputer()

def button6Logic():
    button_6["state"] = DISABLED
    button_6['text'] = player
    board[6] = player
    againstComputer()

def button7Logic():
    button_7["state"] = DISABLED
    button_7['text'] = player
    board[7] = player
    againstComputer()

def button8Logic():
    button_8["state"] = DISABLED
    button_8['text'] = player
    board[8] = player
    againstComputer()

def button9Logic():
    button_9["state"] = DISABLED
    button_9['text'] = player
    board[9] = player
    againstComputer()



button_1 = Button (window, text=board[1], padx=40, pady=30, command=button1Logic)
button_2 = Button (window, text=board[2], padx=40, pady=30, command=button2Logic)
button_3 = Button (window, text=board[3], padx=40, pady=30, command=button3Logic)
button_4 = Button (window, text=board[4], padx=40, pady=30, command=button4Logic)
button_5 = Button (window, text=board[5], padx=40, pady=30, command=button5Logic)
button_6 = Button (window, text=board[6], padx=40, pady=30, command=button6Logic)
button_7 = Button (window, text=board[7], padx=40, pady=30, command=button7Logic)
button_8 = Button (window, text=board[8], padx=40, pady=30, command=button8Logic)
button_9 = Button (window, text=board[9], padx=40, pady=30, command=button9Logic)


button_1.grid(row=1, column=0,)
button_2.grid(row=1, column=1,)
button_3.grid(row=1, column=2,)

button_4.grid(row=2, column=0,)
button_5.grid(row=2, column=1,)
button_6.grid(row=2, column=2,)

button_7.grid(row=3, column=0,)
button_8.grid(row=3, column=1,)
button_9.grid(row=3, column=2,)

def againstComputer():
    if playerWon() == None:
        bestMove()
        text = "Its your turn", player
        label.config(text = text)
        #check after you played if you have won, lost, or tied
    elif playerWon() == ai:
        label.config(text = "The computer has won the Game")

    elif playerWon() == player:
        label.config(text = "You have won the Game")
    else:
        label.config(text = "Tie")
    text = "Its your turn", player
    label.config(text = text)
    return



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
    buttons[move]['text'] = ai
    
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
                


    
# while computerPlaying != "y" or computerPlaying != "n":
# print("Would you like to play against the computer(y/n)")
# computerPlaying = input()

# if computerPlaying == "y":
#     while playerWon() == None:

#         print("Its your turn", player, "where would you like to move. ")
#         Turn = int(input())

#         #Check if turn is good
#         if board[Turn] != " ":
#             print("This move is already taken please choose another move")
#             continue
#         board[Turn] = player
#         if playerWon() == None:
#             bestMove() # this plays what the ai's best move is
#         else:
#             break
# #X,O,tie, or None and tie x and o mean the game is over

# #if playing without computer
# else:
#     while playerWon() == None:
#         print("Its your turn", player, "where would you like to move. ")
#         Turn = int(input())

#         #Check if turn is good
#         if board[Turn] != " ":
#             print("This move is already taken please choose another move")
#             continue
#         board[Turn] = player

#         if player == "X":
#             player = "O"
#         else:
#             player = "X"  
window.mainloop()