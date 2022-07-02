import pygame
from sprites import *
from config import *

import sys
 
class Game:
    def __init__(self):  
        pygame.init() #iniciar pygame
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT)) #TÁ NO CONFIG
        self.clock = pygame.time.Clock() #Ajustar o Frame Rate
    
        self.running = True #Rodando?
        
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet ('img/enemy.png')
    
    def createTilemap(self):
        for i, row in enumerate(tilemap): #enumerar a posição e o conteudo
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column == "B":
                    Block(self,j,i)
                if column == "E":
                    Enemy(self,j,i)
                if column == "P":
                    Player(self,j,i)
        
    def new(self):
        #jogo começa
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        
        self.createTilemap()
        
        
        
    #input,teclado
    def events(self):
        #Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #se apertar no fechar o jogo para de funcionar
                self.playing = False
                self.running = False
        
    #atualizar, fazer se mexer
    def update(self):
        self.all_sprites.update()
        
        
    # Mostrar as sprites
    def draw (self):
        self.screen.fill(BLACK) #tela preta
        self.all_sprites.draw(self.screen) # olha todas as sprites, acha a imagem e desenha no retangulo
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #Game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        pass
        
    def intro_screen(self):
        pass


g = Game()

g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()