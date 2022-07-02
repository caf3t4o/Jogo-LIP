from re import X
from turtle import width
import pygame
from config import *
from Enemy import *
import math
import random

class Spritesheet:
    def __init__(self,file):
        self.sheet = pygame.image.load(file).convert()
        
    def get_sprite(self,x,y,width,height):
        sprite =pygame.Surface([width,height])
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(WHITE)
        
        return sprite

class Player (pygame.sprite.Sprite):
    def __init__ (self,game,x,y):
        
        self.game = game
        self._layer = PLAYER_LAYER  #camada da tela que vai aparecer
        self.groups = self.game.all_sprites 
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x* TILE_SIZE  #32 POR 32 A TILE 
        self.y = y* TILE_SIZE 
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        self.animation_loop = 1
        
        
        self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)
        
       
        
        self.rect = self.image.get_rect()  #hitbox e a imagem serem iguais
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update (self):
        self.movement()
        self.animate()
        self.collide_enemy()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED      
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
            
            
        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
            
            
        if keys[pygame.K_UP]:  # y começa de cima, então - é subir
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
            
        
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            
    def collide_enemy(self):
          hits = pygame.sprite.spritecollide(self,self.game.enemies,False)
          if hits:
              self.kill()
              self.game.playing = False
          
    def collide_blocks(self,direction):
        if direction == "x":
            hits = pygame.sprite.  spritecollide(self,self.game.blocks,False)
            if hits:
                if self.x_change>0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED
                    
                if self.x_change<0:
                    self.rect.x = hits[0].rect.right 
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                    
        if direction == "y":
            hits = pygame.sprite.  spritecollide(self,self.game.blocks,False)
            if hits:
                if self.y_change>0:
                    self.rect.y = hits[0].rect.top   - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                if self.y_change<0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
    def animate(self):
        
        down_animations = [self.game.character_spritesheet.get_sprite(1, 3, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(46, 3, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(92, 3, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(1, 74, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(46, 74, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(92, 74, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(1, 111, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(46, 111, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(92, 111, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(1, 39, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(46, 39, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(92, 39, self.width, self.height)]
        
        if self.facing == "down":
            if self.y_change == 0 :
                self.image = self.game.character_spritesheet.get_sprite(1,3,self.width,self.height)
            else: 
                self.image = down_animations[math.floor(self.animation_loop)] # a cada 10 frames muda o loop da animação
                self.animation_loop+= 0.1
                if self.animation_loop>= 3:
                    self.animation_loop = 1
                    
        if self.facing == "up":
            if self.y_change == 0 :
                self.image = self.game.character_spritesheet.get_sprite(1,74,self.width,self.height)
            else: 
                self.image = up_animations[math.floor(self.animation_loop)] # a cada 10 frames muda o loop da animação
                self.animation_loop+= 0.1
                if self.animation_loop>= 3:
                    self.animation_loop = 1
        
        if self.facing == "left":
            if self.x_change == 0 :
                self.image = self.game.character_spritesheet.get_sprite(1,111,self.width,self.height)
            else: 
                self.image = left_animations[math.floor(self.animation_loop)] # a cada 10 frames muda o loop da animação
                self.animation_loop+= 0.1
                if self.animation_loop>= 3:
                    self.animation_loop = 1
        
        if self.facing == "right":
            if self.x_change == 0 :
                self.image = self.game.character_spritesheet.get_sprite(1,39,self.width,self.height)
            else: 
                self.image = right_animations[math.floor(self.animation_loop)] # a cada 10 frames muda o loop da animação
                self.animation_loop+= 0.1
                if self.animation_loop>= 3:
                    self.animation_loop = 1



class Block(pygame.sprite.Sprite): 
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = BLOCK_LAYER  # Dizer ao pygame em qual camada vai aparecer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x* TILE_SIZE
        self.y = y* TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.image = self.game.wall_spritesheet.get_sprite(14*32,5*32,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Ground (pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILE_SIZE
        self.y = y *TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(256,352,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        