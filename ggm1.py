# 초기 코드
import pygame
import sys 
import random
from time import sleep
 
padWidth = 480 
padHeight = 640
rockImage = ["C:/Users/psc77/Desktop/PyShooting/rock11.png",
"C:/Users/psc77/Desktop/PyShooting/rock12.png",
"C:/Users/psc77/Desktop/PyShooting/rock13.png",
"C:/Users/psc77/Desktop/PyShooting/rock14.png",
"C:/Users/psc77/Desktop/PyShooting/rock15.png",
"C:/Users/psc77/Desktop/PyShooting/rock16.png",
"C:/Users/psc77/Desktop/PyShooting/rock17.png",
"C:/Users/psc77/Desktop/PyShooting/rock18.png",
"C:/Users/psc77/Desktop/PyShooting/rock19.png",
"C:/Users/psc77/Desktop/PyShooting/rock20.png",
"C:/Users/psc77/Desktop/PyShooting/rock21.png",
"C:/Users/psc77/Desktop/PyShooting/rock22.png",
"C:/Users/psc77/Desktop/PyShooting/rock23.png",
"C:/Users/psc77/Desktop/PyShooting/rock24.png",
"C:/Users/psc77/Desktop/PyShooting/rock25.png",
"C:/Users/psc77/Desktop/PyShooting/rock26.png",
"C:/Users/psc77/Desktop/PyShooting/rock27.png",
"C:/Users/psc77/Desktop/PyShooting/rock28.png",
"C:/Users/psc77/Desktop/PyShooting/rock29.png",
"C:/Users/psc77/Desktop/PyShooting/rock30.png",
"C:/Users/psc77/Desktop/PyShooting/rock01.png",
"C:/Users/psc77/Desktop/PyShooting/rock02.png",
"C:/Users/psc77/Desktop/PyShooting/rock03.png",
"C:/Users/psc77/Desktop/PyShooting/rock04.png",
"C:/Users/psc77/Desktop/PyShooting/rock05.png",
"C:/Users/psc77/Desktop/PyShooting/rock06.png",
"C:/Users/psc77/Desktop/PyShooting/rock07.png",
"C:/Users/psc77/Desktop/PyShooting/rock08.png",
"C:/Users/psc77/Desktop/PyShooting/rock09.png",
"C:/Users/psc77/Desktop/PyShooting/rock10.png"]

explosionSound = ["C:/Users/psc77/Desktop/PyShooting/explosion01.wav",
"C:/Users/psc77/Desktop\PyShooting/explosion02.wav",
"C:/Users/psc77/Desktop\PyShooting/explosion03.wav",
"C:/Users/psc77/Desktop\PyShooting/explosion04.wav",]


def writeScore(count):
    global gamePad
    font = pygame.font.Font("C:/Users/psc77/Desktop/PyShooting/NanumGothic.ttf", 20)
    text = font.render('파괴한 운석 수: ' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (10, 0))

# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font("C:/Users/psc77/Desktop/PyShooting/NanumGothic.ttf", 20)
    text = font.render('통과한 운석: ' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (350, 0))


def writeMessage(text):
    global gamePad, gameOverSound
    textFont = pygame.font.Font("C:/Users/psc77/Desktop/PyShooting/NanumGothic.ttf", 60)
    text = textFont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.stop(-1)
    runGame()

# 전투기가 운석과 충돌했을 때 메시지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴!')

# 게임 오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')


def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y))


def initGame(): 
    global gamePad, clock, background, fighter , missile, explosion, missileSound, gameOverSound
    pygame.init() 
    gamePad = pygame.display.set_mode((padWidth, padHeight)) 
    pygame.display.set_caption('PyShooting') 
    background = pygame.image.load('C:/Users/psc77/Desktop/PyShooting/background.png')
    fighter = pygame.image.load('C:/Users/psc77/Desktop/PyShooting/fighter.png')
    missile = pygame.image.load('C:/Users/psc77/Desktop/PyShooting/missile.png')
    explosion =pygame.image.load('C:/Users/psc77/Desktop/PyShooting/explosion.png')
    pygame.mixer.music.load("C:/Users/psc77/Desktop/PyShooting/music.wav")
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound("C:/Users/psc77/Desktop/PyShooting/missile.wav")
    gameOverSound = pygame.mixer.Sound("C:/Users/psc77/Desktop/PyShooting/gameover.wav")
    clock = pygame.time.Clock()


def runGame(): 
    global gamePad, clock, background, fighter, missile, explosion, missileSound

    # 전투기 크기 
    fighterSize = fighter.get_rect().size 
    fighterWidth = fighterSize[0] 
    fighterHeight = fighterSize[1]

     # 전투기 초기 위치 
    x = padWidth * 0.45 
    y = padHeight * 0.9 
    fighterX = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size  # 운석 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    isShot = False
    shotCount = 0
    rockPassed = 0

    onGame= False 
    while not onGame: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -= 5

                elif event.key == pygame.K_RIGHT: # 전투기 오른쪽으로 이동
                    fighterX += 5

                elif event.key == pygame.K_SPACE: # 미사일 발사 
                    missileSound.play()
                    missileX = x + fighterWidth / 2 
                    missileY = y - fighterHeight 
                    missileXY.append([missileX, missileY])

            if event.type == [pygame.KEYUP]: # 방향키를 떼면 전투기 멈춤 
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    fighterX = 0

        drawObject(background, 0, 0) 

        x += fighterX
        if x < 0:
            x = 0 
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
        
        if y < rockY + rockHeight:
            if(rockX> x and rockX < x + fighterWidth) or \
                    (rockX +rockWidth > x and rockX + rockWidth < + fighterWidth):
                crash()

        drawObject(fighter,x,y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):  # 미사일 요소에 대해 반복함
                bxy[1] -= 10  # 총알의 y좌표 -10 (위로 이동)
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1
        
                if bxy[1] <= 0:  # 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy)  # 미사일 제거
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)


        writeScore(shotCount)

        rockY += rockSpeed  # 운석 아래로 움직임

        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size  # 운석 크기
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            rockPassed += 1
        
        if rockPassed == 3:
            gameOver()

        writePassed(rockPassed)

        if isShot:
    # 운석 폭발
            drawObject(explosion, rockX, rockY)  # 운석 폭발 그리기
            destroySound.play()
    # 새로운 운석 (랜덤)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            
            isShot = False

            rockSpeed += 0.2
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

initGame()
runGame()