import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640
def initGame():
    global gamePad, clock
    pvgame.init()
    gamePad = pygame.display.set_mode((padwidth, padHeight))
    pygame.display.set_caption('PyShooting')
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock

 onGame= False
 while not onGame:
     for event in pygame.event.get():
         if event.type in [pygame.QUIT]:
             pygame.quit()
             sys.exit()

        gamePad.fill(BLACK)

        pygame.display.update()

        clock.tick(60)

pygame.quit()

initGame()
runGame()

