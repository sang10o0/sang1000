import pygame
import sys 
from time import sleep

BLACK=(0, 0, 0) 
padWidth = 480 
padHeight = 640
FPS = 60

def initGame(): 
    global gamePad, clock 
    pygame.init() 
    gamePad = pygame.display.set_mode((padWidth, padHeight)) 
    pygame.display.set_caption('PyShooting') 
    clock = pygame.time.Clock()


def runGame(): 
    global gamePad, clock

    onGame= False 
    while not onGame: 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()

        gamePad.fill(BLACK)

        drawobject(background, 0, 0) 

        pygame.display.update()

        clock.tick(60)

def drawobject(obj, x, y): 
    global gamePad 
    gamePad.blit(obj, (x, y))

def initcame():
    global gamePad, clock,background 
    pygame.init() 
    gamePad = pygame.display.set_mode((padWidth, padHeight)) 
    pygame.display.set_caption('PyShooting') # 게임 이름 설정 
    background = pygame.image.load("C:/Users/psc77/Desktop/PyShooting/background.png") #배경 그림 
    clock = pygame.time.Clock() 

initcame()
runGame()