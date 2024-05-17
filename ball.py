import pygame
import random 

class Ball:
    def __init__(self, game, screen, rad):
        self.game = game
        self.screen = screen

        self.top_rect = pygame.Rect(0, 0, self.screen.get_width(), 2)
        self.bottom_rect = pygame.Rect(0, 720, self.screen.get_width(), 2)

        self.ballimg = pygame.image.load('assets/Ellipse 1.png')

        self.ballpos = [0,0]
        self.ballrect = self.ballimg.get_rect()

        self.movingup = False
        self.movingdown = False
        self.movingright = False
        self.movingleft = False

        self.velocity = [0,0]

        self.screencenter = [(self.screen.get_width() - self.ballimg.get_width())/2 , (self.screen.get_height() - self.ballimg.get_height())/2]
    

    def startup(self):
        self.ballpos = self.screencenter
        self.movingleft = True
        self.movingdown = True

        self.ballrect.x = self.screencenter[0]
        self.ballrect.y = self.screencenter[1]
    
    
    def _check_collisions(self):
        collision = [self.ballrect.colliderect(self.game.bar1.rect), self.ballrect.colliderect(self.game.bar2.rect), 
                     self.ballrect.colliderect(self.top_rect), self.ballrect.colliderect(self.bottom_rect),
                     self.ballrect.colliderect(self.game.bar1.bar_invisible_rect), self.ballrect.colliderect(self.game.bar2.bar_invisible_rect),
                     ]
        return collision
    
    def bounce(self):
        collision_result = self._check_collisions()
        if collision_result[2] or collision_result[3] or collision_result[4] or collision_result[5]:
            self.movingup = not self.movingup
            self.movingdown = not self.movingdown

        elif collision_result[0] or collision_result[1]:
            self.movingleft = not self.movingleft
            self.movingright = not self.movingright
        
        
    
    def add_momentum(self):
        if self._check_collisions()[0]:
            if (self.game.bar1.velocity > 0):
                self.velocity[1] += 4
            elif (self.game.bar1.velocity < 0):
                self.velocity[1] -= 4


    def update(self):
        if self._check_collisions()[0] or self._check_collisions()[1] or self._check_collisions()[2] or self._check_collisions()[3]:
            self.bounce()
            self.add_momentum()
        
        if self.movingright:
            self.velocity[0] = 6
        if self.movingleft:
            self.velocity[0] = -6
        if self.movingup:
            self.velocity[1] = -6
        if self.movingdown:
            self.velocity[1] = 6
        

        
        self.ballpos[0] += self.velocity[0]
        self.ballpos[1] += self.velocity[1]

        self.ballrect.x = self.ballpos[0]
        self.ballrect.y = self.ballpos[1]

    def render(self):

        self.screen.blit(self.ballimg, (self.ballrect.x, self.ballrect.y))