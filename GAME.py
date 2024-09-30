from morpiongame import MorpionGame
from pongame import PongGame
from coolfunctions import *
playing = True




    

def main():
    print("games: \n Morpion (1) \n Pong(2)")
    a = asknumber(1, 2, "\nselect :")
    if a == 1:
        a = MorpionGame()
    if a == 2:
        a = PongGame()
    if asknumber(1, 2, "\n Whant to replay ? 1=Y 2=N :") == 1:
        main()
if __name__ == '__main__':
    main()