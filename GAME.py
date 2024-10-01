from morpiongame import MorpionGame
from pong import Pong
from coolfunctions import *
import pygame
import time


playing = True

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
size = 3
selecter = 0
pygame.font.init()
my_font = pygame.font.SysFont('IBM Plex Mono', 50)
screen = pygame.display.set_mode((size  * 200, size  * 200))
running = True

#def main():
#    print("games: \n Morpion (1) \n Pong(2)")
#    a = asknumber(1, 2, "\nselect :")
#    if a == 1:
#        a = MorpionGame(screen)
#    if a == 2:
#        a = PongGame()
#    if asknumber(1, 2, "\n Whant to replay ? 1=Y 2=N :") == 1:
#        main()

def main():
    global size
    global running
    global selecter
    global screen
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    selecter = 0 if selecter else 1
                if event.key == pygame.K_q:
                    selecter = 0 if selecter else 1
                if event.key == pygame.K_RETURN:
                    if selecter == 0:
                        MorpionGame(screen, size )
                        screen = pygame.display.set_mode((size  * 200, size  * 200))
                    if selecter == 1:
                        Pong(screen, size)
                        
        rendertext("Morpion", WHITE if selecter else GREEN, ((size  * 200)/2 + 30, (size  * 200)/2), screen)
        rendertext("Pong", GREEN if selecter else WHITE, ((size  * 200)/2 - 150, (size  * 200)/2) , screen)
        pygame.display.flip()
        time.sleep(.1)

if __name__ == '__main__':
    main()
    