import pygame
import time

WHITE = (255, 255, 255)

class Pong:
    def __init__(self, screen, size):
        self.size = size
        self.player1 = Player(1, [0, 0])
        self.player2 = Player(2, [self.size*200 - 10, 0])
        self.ball = Ball((100, 100))
        self.objects = [self.player1, self.player2, self.ball]
        self.screen = screen
        self.main()
    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.player1.position[1] += 100
                        print(self.player1.position)
                    if event.key == pygame.K_z: 
                        self.player1.position[1] -= 100
                    if event.key == pygame.K_l:
                        self.player2.position[1] += 100
                    if event.key == pygame.K_o: 
                        self.player2.position[1] -= 100
            self.ball.update()
            self.display()
            self.ball.collision(self.player1, self.player2)
            time.sleep(.1)
        
    def display(self):
        self.screen.fill((0, 0, 0))
        for obj in self.objects:
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(obj.position[0], obj.position[1], 10, obj.size))
        pygame.display.flip()

class Player:
    def __init__(self,ide ,position):
        self.id = ide
        self.position = position
        self.size = 100
        self.surface = pygame.Rect(self.position[0], self.position[1], 10, self.size)
    def update(self):
        pass


class Ball:
    def __init__(self, position):
        self.position = position
        self.velocity = (10, 10)
        self.size = 10
        self.surface = pygame.Rect(self.position[0], self.position[1], 10, self.size)
        
    def update(self):
        self.position = self.velocity[0] + self.position[0], self.velocity[1] + self.position[1]

    def collision(self, player1, player2):
        if self.position[1] <= 0 or self.position[1] >= 500:
            self.velocity = (self.velocity[0], -self.velocity[1]) 

        if self.position[0] <= 10:
            if player1.position[1] <= self.position[1] <= player1.position[1] + player1.size:
                self.velocity = (-self.velocity[0], self.velocity[1]) 

        if self.position[0] >= 490: 
            if player2.position[1] <= self.position[1] <= player2.position[1] + player2.size:
                self.velocity = (-self.velocity[0], self.velocity[1])  

    
if __name__ == "__main__":
    Pong()