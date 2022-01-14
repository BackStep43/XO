from socket import *

from flask import request
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

Users = {}
user_status = ""
def Status_User() :
    user_status = input("New User press 'N' || Old users press 'Y' || Exit press 'Q' || Reset press 'R' : ")
    if user_status.upper() == 'N':
        newUser() 
    elif user_status.upper() == 'Y':
        oldUser()
    elif user_status.upper() == 'Q':
        clientSocket.close
        exit()
def newUser():
    createID = input("Create Username : ")
    if createID in Users:
        print("ID already exists!")
    else:
        createPass = input("Create Password : ")
        Users[createID] = createPass
        print("Created")

def oldUser():
    logIn = input("ID : ")
    passWord = input("Password : ")

    if logIn in Users and Users[logIn] == passWord:
        print("Loging succesfull")

        board = [' ' for x in range(10)]

        def insertLetter(letter, pos):
            board[pos] = letter

        def spaceIsFree(pos):
            return board[pos] == ' '

        print('   |   |')
        print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
        print('   |   |')
        print('---+---+---')
        print('   |   |')
        print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
        print('   |   |')
        print('---+---+---')
        print('   |   |')
        print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
        print('   |   |')

        def main():
            print('Welcome to Tic Tac Toe!')
            printBoard(board)
            while not(isBoardFull(board)):
                if not(isWinner(board, 'O')):
                    playerMove()
                    printBoard(board)
                else:
                    computerWin = "Sorry, Computer's won this time!"
                    clientSocket.send(computerWin.encode())
                    results = clientSocket.recv(1024).decode()
                    print(results)
                    exit()
                if not(isWinner(board, 'X')):
                    move = compMove()
                    if move == 0:
                        tie = 'Tie Game!'
                        clientSocket.send(tie.encode())
                        results = clientSocket.recv(1024).decode()
                        print(results)
                        exit()
                    else:
                        insertLetter('O', move)
                        print('Computer placed an \'O\' in position', move , ':')
                        printBoard(board)
                else:
                    playerWin = "You won this time! Good Job!"
                    clientSocket.send(playerWin.encode())
                    results = clientSocket.recv(1024).decode()
                    print(results)
                    exit()

        def printBoard(board):
            print('   |   |')
            print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
            print('   |   |')
            print('---+---+---')
            print('   |   |')
            print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
            print('   |   |')
            print('---+---+---')
            print('   |   |')
            print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
            print('   |   |')
            
        def isWinner(bo, le):
            return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

        def playerMove():
            run = True
            while run:
                move = input('Please select a position to place an \'X\' (1-9): ')
                try:
                    move = int(move)
                    if move > 0 and move < 10:
                        if spaceIsFree(move):
                            run = False
                            insertLetter('X', move)
                        else:
                            print('Sorry, this space is occupied!')
                    else:
                        print('Please type a number within the range!')
                except:
                    print('Please type a number!')
                    

        def compMove():
            possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
            move = 0

            for let in ['O', 'X']:
                for i in possibleMoves:
                    boardCopy = board[:]
                    boardCopy[i] = let
                    if isWinner(boardCopy, let):
                        move = i
                        return move

            cornersOpen = []
            for i in possibleMoves:
                if i in [1,3,7,9]:
                    cornersOpen.append(i)
                    
            if len(cornersOpen) > 0:
                move = selectRandom(cornersOpen)
                return move

            if 5 in possibleMoves:
                move = 5
                return move

            edgesOpen = []
            for i in possibleMoves:
                if i in [2,4,6,8]:
                    edgesOpen.append(i)
                    
            if len(edgesOpen) > 0:
                move = selectRandom(edgesOpen)
                
            return move

        def selectRandom(li):
            import random
            ln = len(li)
            r = random.randrange(0,ln)
            return li[r]
            

        def isBoardFull(board):
            if board.count(' ') > 1:
                return False
            else:
                return True
        if __name__ == "__main__":
                main()                
    else:
        print("Wrong ID or Password")

while user_status != 'R' or user_status != 'R':
    Status_User()