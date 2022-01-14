from socket import *
import time

SERVER_PORT = 12000

def main():
    try:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', SERVER_PORT))
        serverSocket.listen(1)
        print('The server is ready to receive.\n')

        while True:
            connectionSocket, addr = serverSocket.accept()
            print(time.asctime(time.localtime(time.time())), '|', addr, 'connected')
            
            request = connectionSocket.recv(1024).decode()
            results(connectionSocket, addr, request)

    except OSError as error:
        print("OSError: %s" % error)
    exit(0)

def results(connectionSocket, addr, request):
    msg = ""
    if(request == "Tie Game!"):
        msg = "Tie Game!"
    elif(request == "You won this time! Good Job!"):
        msg = "You won this time! Good Job!"
    elif(request == "Sorry, Computer's won this time!"):
        msg = "Sorry, Computer's won this time!"
    connectionSocket.send(msg.encode())
    print(time.asctime(time.localtime(time.time())), '|', addr, msg)

if __name__ == "__main__":
    main()