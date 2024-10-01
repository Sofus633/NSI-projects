import pygame




class Pong:
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.ball = Ball((10, 10))
        self.objects = [slef.player1, self.player2, slef.ball]

    def display(self):
        for obj in slef.objectes:
            screen.blit(obj.surface, )

class Player:
    def __init__(self,ide ,position):
        self.id = ide
        self.position = position
        self.size = 100
        self.surface 


class Ball:
    def __init__(self, position):
        self.position = position
        self.velocity = (1, 1)

    def update(slef):
        self.position = self.velocity[0] + position[0], self.velocity[1] + self.position[1]

    def collition(self, player1, player2):
        if self.position[1] > 500 or self.position[1] < 0:
            self.velocity[1] = - slef.velocity[1]
        if self.position[0] > 500-10 or self.position < 10:
            if self.position[1] < slef.player1.position[1] + slef.player1.size and self.position[0] > slef.player1.position or self.position[1] < self.player2.position[1] + self.position1.size and self.position [0] > self;player2.position:
                self.velocity[0] =- self.velocity[0]
    
