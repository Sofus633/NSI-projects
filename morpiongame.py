from coolfunctions import *
import pygame
import time


class MorpionGame:
    def __init__(self, screen, size ) -> None:
        self.screen = screen
        self.size = asknumber(screen, (3, 9), "type number 3 - 9:", "int",size)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.running = True
        self.tour = self.player1
        print((self.size * 200, self.size * 200))
        pygame.init()
        self.screen = pygame.display.set_mode((self.size * 200, self.size * 200))
        self.board = GameBoard(self.size, self.screen)
        self.playeagame()
        
    def getinputs(self):
        getinginp = True
        while getinginp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos() 
                    boardpos = int(pos[0]/ 200) , int(pos[1] / 200)
                    a = self.placerpion2(boardpos[0], boardpos[1])
                    print(a)
                    if a:
                        getinginp = False
        time.sleep(.1)  

    
        
    def playeagame(self):
        if self.running:
            self.board.displaygraphique()
            
            
            self.getinputs()
                
            if self.board.checkall() == False:
                self.playeagame()
            
            else:
                self.running = False
                
            
            
                print(f'Yey {self.player2.name if self.tour == self.player1 else self.player1.name} a gagner !')
        celebrating = True
        gif = getGif("img/catcelebrating.gif")
        while celebrating:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    celebrating = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        celebrating = False
            self.screen.fill((0, 0, 0))
            gif.render(self.screen, (100, 200))
            rendertext(f'Yey {self.player2.name if self.tour == self.player1 else self.player1.name} a gagner !', (255, 255, 255), (((self.size*200)/2) - 150, 100), self.screen )
            rendertext('Press enter to continue', (255, 255, 255), (100, 140), self.screen )
            pygame.display.flip()
    
    def placerpion2(self, x, y):
        valid = self.board.placepion(x, y, self.tour)
        if valid == False:
            self.getinputs()
        self.tour = self.player2 if self.tour == self.player1 else self.player1
        return True
    
    def placerpion(self):
            x = asknumber(1, self.size, "\nColone :") -1
            y = asknumber(1, self.size, "Ligne :") -1
            valid = self.board.placepion(x, y, self.tour)
            if valid == False:
                self.placerpion()
            self.tour = self.player2 if self.tour == self.player1 else self.player1
            

class GameBoard:
    def __init__(self,size, screen):
        self.size = size
        self.realboard = [[None for _ in range(size)]for _ in range(size)]
        self.screen = screen
    
    def display(self):
        print("  ", end="")
        for x in range(self.size):
            print(str(x+1), end=" ")
        print()
        for y in range(self.size):
            print(str(y+1) + " ", end="")
            for x in range(self.size):
                print(self.get_pion_case(x, y), end=" ")
            print()
    
    def displaygraphique(self):
        for y in range(len(self.realboard)):
            for x in range(len(self.realboard)):
                print("passing", self.realboard[y][x])
                if self.realboard[y][x] != None:
                    print(self.realboard[y][x].pion, "PIONNNNNNNNNNNNNN")
                    self.screen.blit(self.realboard[y][x].pion , [y * 200 + 50, x * 200+ 50])
        pygame.display.flip()
    
    def get_pion_case(self, x, y):
        return " " if self.realboard[y][x] == None else self.realboard[y][x].pion
    
    def placepion(self, x, y, pion):
        if self.realboard[x][y] == None:
            self.realboard[x][y] = pion
            print('Pion placer !')
            return True
        else:
            print('Case occupée !')
            return False
    
    def checkallligneandcolones(self):
        """_summary_
        return False if no ligne win else player
        Returns:
            Player: pion / name
            or 
            Boolean: False
        """
        for y in range(self.size):
            a = []
            b = []
            for x in range(self.size):
                if self.realboard[y][x] != None:
                    
                    if len(a) > 0:
                        if a[0] == self.realboard[y][x]:
                            a.append(self.realboard[y][x])
                    else:
                        a.append(self.realboard[y][x])
                if self.realboard[x][y] != None:
                    
                    if len(a) > 0:
                        if a[0] == self.realboard[x][y]:
                            b.append(self.realboard[x][y])
                    else:
                        b.append(self.realboard[x][y])
            if len(a) == self.size:
                return a[0]
            if len(b) == self.size:
                return b[0]
        return False
            
    def checkalldiagonales(self):
        """_summary_
        return False if no diag win else player
        Returns:
            Player: pion / name
            or 
            Boolean: False
        """
        y = 0
        x_2 = self.size - 1
        diag1 = []
        diag2 = []
        for x in range(self.size):
                
            if self.realboard[y][x] != None:
                if len(diag1) > 0:
                    if diag1[0] == self.realboard[y][x]:
                        diag1.append(self.realboard[y][x])
                else:
                    diag1.append(self.realboard[y][x])
                
            if self.realboard[y][x_2] != None:
                if len(diag2) > 0:
                    if diag2[0] == self.realboard[y][x_2]:
                        diag2.append(self.realboard[y][x_2])
                else:
                    diag2.append(self.realboard[y][x_2])
            
            y += 1
            x_2 -= 1
        if len(diag1) == self.size:
            return diag1[0]
        if len(diag2) == self.size:
            return diag2[0]
        return False
        
    def checkall(self):
        """_summary_
        return False if no player win else player
        Returns:
            Player: pion / name
            or 
            Boolean: False
        """
        a = [self.checkallligneandcolones(), self.checkalldiagonales()]
        for val in a:
            if val != False:
                return val
        else:
            return False

class Player:
    def __init__(self, id):
        print(f"\nplayer {id} :")
        self.pion = pygame.image.load("img/circle.png" if id == 1 else "img/cross.png")
        self.name = "circle" if id == 1 else "cross"
        
    
if __name__ == "__main__":
    MorpionGame()