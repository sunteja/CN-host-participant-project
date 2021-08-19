import socket
from thread import *
import pickle
from game import Game
import pygame

server = "172.16.129.92"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(3)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

#questions = ["color of cricket ball?\nA)white\nB)black\nC)pink\nD)blue", "cat says?\nA)meow\nB)bow\nC)chrip\nD)none"]
answers = ["A","B"]
def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))


    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)
#                    elif data == "Buzz":
#                        game.buzzer(p)
                        

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//3
    if idCount % 3 == 2:
        #p=1
        games[gameId] = Game(gameId)
        print("Creating a new game...")
        p=1
    elif idCount % 3 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 2


    start_new_thread(threaded_client, (conn, p, gameId))
