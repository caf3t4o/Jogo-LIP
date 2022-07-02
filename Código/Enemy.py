from re import X
from turtle import width
import pygame
from config import *
import math
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites,self.game.enemies
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x* TILE_SIZE
        self.y = y* TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = random.choice(['left','right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7,30)
        
        self.image = self.game.enemy_spritesheet.get_sprite(3,2,self.width,self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x= self.x
        self.rect.y= self.y
        
    def update(self):
        self.movement()
        self.animate()
        
        self.rect.x+= self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
        
    
    def movement (self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop<= -self.max_travel:
                self.facing = 'right'
                
        if self.facing == 'right':
            self.x_change+= ENEMY_SPEED
            self.movement_loop+= 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
                
    def animate(self):

        right_animations = [self.game.enemy_spritesheet.get_sprite(0, 32, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(32, 32, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(64, 32, self.width, self.height),
                           self.game.enemy_spritesheet.get_sprite(96, 32, self.width, self.height)]

        left_animations = [self.game.enemy_spritesheet.get_sprite(0, 96, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(32, 96, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(64, 96, self.width, self.height),
                            self.game.enemy_spritesheet.get_sprite(96, 96, self.width, self.height)]
        
        if self.facing == "left":
            if self.x_change == 0 :
                self.image = self.game.enemy_spritesheet.get_sprite(3,34,self.width,self.height)
            else: 
                self.image = left_animations[math.floor(self.animation_loop)] # a cada 10 frames muda o loop da animação
                self.animation_loop+= 0.1
                if self.animation_loop>= 3:
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.x_change == 0 :
                self.image = self.game.enemy_spritesheet.get_sprite(3,34,self.width,self.height)
            else: 
                self.image = right_animations[math.floor(self.animation_loop)] # a cada 10 frames muda o loop da animação
                self.animation_loop+= 0.1
                if self.animation_loop>= 3:
                    self.animation_loop = 1
        