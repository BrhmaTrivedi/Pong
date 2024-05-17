import pygame
import sys
import os

from ball import Ball
from bars import Bars

class Pong:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1280,720))

        pygame.display.set_caption('Pong')

        self.barsize = (40, 120)
        self.barypos = (self.screen.get_height() - self.barsize[1])/ 2

        self.bar1 = Bars(self, self.screen, [30, self.barypos], self.barsize)
        self.bar2 = Bars(self, self.screen, [1210, self.barypos], self.barsize)
        
        self.ball = Ball(self, self.screen, 10)

        self.clock = pygame.time.Clock()

    
    def run(self):
        self.ball.startup()

        while True:
            self.screen.fill((255,255,255))
 
            self.ball.update()
            self.ball.render()

            self.bar1.update()
            self.bar1.render()

            self.bar2.update()
            self.bar2.render()


            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_UP:
                        self.bar2.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.bar2.moving_down = True
                    if event.key == pygame.K_w:
                        self.bar1.moving_up = True
                    if event.key == pygame.K_s:
                        self.bar1.moving_down = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.bar2.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.bar2.moving_down = False
                    if event.key == pygame.K_w:
                        self.bar1.moving_up = False
                    if event.key == pygame.K_s:
                        self.bar1.moving_down = False

            pygame.display.update()
            self.clock.tick(60)

Pong().run()