
import pygame
import time
import gif_pygame

pygame.font.init()
my_font = pygame.font.SysFont('IBM Plex Mono', 50)

def rendertext(text, color, pos ,screen):
    text_surface = my_font.render(text, False, color)
    screen.blit(text_surface, (pos))
    
def asknumber(screen, rangee, text, type, size):
    running = True
    input = ""
    screen.fill((0, 0, 0))
    rendertext(text, (255, 255, 255), (((2 * 200) / 2) - 100 , ((2 * 200) / 2) - 100), screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                if event.key == pygame.K_RETURN:
                    
                    if type == 'str':
                        if len(input) >= rangee[0] and len(input) <= rangee[1]: 
                            running = False
                        else:
                            input = ''
                    if type == 'int':
                        try:
                            print(int(input))
                            if int(input) >= rangee[0] and int(input) <= rangee[1]:
                                input = int(input)
                                running = False
                            else:
                                input =  ''
                        except:
                            input = ''
                        
                
                if -128 <= event.key < 127 and event.key not in (8, 13):
                    input += chr(event.key)
                rendertext(str(input), (255, 255, 255), (((2 * 200) / 2) - 100, (2 * 200) / 2), screen)
                rendertext(text, (255, 255, 255), (((2 * 200) / 2) - 100 , ((2 * 200) / 2) - 100), screen)
                pygame.display.flip()
                screen.fill((0, 0, 0))
        time.sleep(.1)
    return input

def getGif(gif):
    a = gif_pygame.load(gif)
    return a 