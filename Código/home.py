from re import X
from turtle import width
import pygame
from config import *
from Enemy import *
import math
import random

class Home(pygame.sprite.Sprite): 
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = BLOCK_LAYER  # Dizer ao pygame em qual camada vai aparecer
        self.groups = self.game.all_sprites, self.game.houses
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x* TILE_SIZE
        self.y = y* TILE_SIZE
        self.width = TILE_SIZE*3
        self.height = TILE_SIZE*3
        
        self.image = self.game.house_spritesheet.get_sprite(0*32,0*32,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        