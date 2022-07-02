WIN_WIDTH = 1280 #RESOLUÇÃO LARGURA
WIN_HEIGHT= 690 # RESOLUÇÃO ALTURA
TILE_SIZE = 32 #TAMANHO DA TILE
FPS = 60

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2

RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

#480/32 = 15
#640/32 = 20
#B = parede
#P = Player
tilemap = [
   'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
   'B..........B.......BB..................B',
   'B...BBB............BB..........E.......B',
   'B..................BB..................B',
   'B..................BB..................B',
   'B........P.............................B',
   'B......................................B',
   'B......................................B',
   'B......................................B',
   'B......................................B',
   'B......................................B',
   'B.............B....BB..................B',
   'B.............B....BB..................B',
   'B.............B....BB..................B',
   'B...........E......BB..................B',
   'B..................BB..................B',
   'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB..BBBBBBB',
   'B......................................B',
   'B......................................B',
   'B........E.............................B',
   'B......................................B',
   'B......................................B', 
   'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]