import pygame
from pygame.locals import QUIT

# Initialisation de Pygame
pygame.init()
pygame.display.set_caption("Jeu de BlackJack")
FramePerSec = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
FPS = 60
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
background = 
vec = pygame.math.Vector2

# Boucle de jeu
while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()