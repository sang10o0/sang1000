import pygame
import sys 
import random
from time import sleep

# 게임 설정
padWidth = 480 
padHeight = 640

# 이미지 및 사운드 파일 경로
IMAGE_PATH = "C:/Users/psc77/Desktop/PyShooting/"
FONT_PATH = "C:/Users/psc77/Desktop/PyShooting/"
rockImage = [IMAGE_PATH + f"rock{i:02d}.png" for i in range(1, 31)]
explosionSound = [IMAGE_PATH + f"explosion0{i}.wav" for i in range(1, 5)]

# 색깔
WHITE = (255, 255, 255)
RED = (255, 0, 0)

is_shot = False  # 전역 변수로 선언하고 초기화

def load_image(image_path):
    """이미지를 로드합니다."""
    return pygame.image.load(image_path)

def load_sound(sound_path):
    """사운드를 로드합니다."""
    return pygame.mixer.Sound(sound_path)

def write_text(text, font_path, size, color, x, y):
    """텍스트를 화면에 씁니다."""
    font = pygame.font.Font(font_path, size)
    text_surface = font.render(text, True, color)
    gamePad.blit(text_surface, (x, y))


def draw_object(obj, x, y):
    """오브젝트를 그립니다."""
    gamePad.blit(obj, (x, y))

def is_collision(obj1_x, obj1_y, obj1_width, obj1_height, obj2_x, obj2_y, obj2_width, obj2_height):
    """두 오브젝트의 충돌 여부를 확인합니다."""
    return (obj1_x < obj2_x + obj2_width and
            obj1_x + obj1_width > obj2_x and
            obj1_y < obj2_y + obj2_height and
            obj1_y + obj1_height > obj2_y)

def init_game(): 
    """게임 초기화"""
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init() 
    gamePad = pygame.display.set_mode((padWidth, padHeight)) 
    pygame.display.set_caption('PyShooting') 
    background = load_image(IMAGE_PATH + 'background.png')
    fighter = load_image(IMAGE_PATH + 'fighter.png')
    missile = load_image(IMAGE_PATH + 'missile.png')
    explosion = load_image(IMAGE_PATH + 'explosion.png')
    pygame.mixer.music.load(IMAGE_PATH + 'music.wav')
    pygame.mixer.music.play(-1)
    missileSound = load_sound(IMAGE_PATH + 'missile.wav')
    gameOverSound = load_sound(IMAGE_PATH + 'gameover.wav')
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

        draw_object(background, 0, 0) 

        x = max(0, min(x + fighterX, padWidth - fighterWidth))

        if y < rockY + rockHeight and (x < rockX + rockWidth and x + fighterWidth > rockX):
            crash()

        draw_object(fighter,x,y)

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
                draw_object(missile, bx, by)

        write_text(f"파괴한 운석: {shotCount}", FONT_PATH + 'NanumGothic.ttf', 30, WHITE, 10, 10)
        write_text(f"통과한 운석: {rockPassed}", FONT_PATH + 'NanumGothic.ttf', 30, WHITE, padWidth - 200, 10)

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
            game_over()

        if isShot:
    # 운석 폭발
            draw_object(explosion, rockX, rockY)  # 운석 폭발 그리기
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

        draw_object(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    

def crash():
    """운석과 전투기가 충돌했을 때 호출되는 함수"""
    write_message('전투기 파괴!')

def game_over():
    """게임 오버 시 호출되는 함수"""
    write_message('게임 오버!')

def write_message(text):
    """화면에 메시지를 출력하는 함수"""
    global gamePad, gameOverSound
    textFont = pygame.font.Font(FONT_PATH + 'NanumGothic.ttf', 60)
    text_surface = textFont.render(text, True, (255, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.center = (padWidth / 2, padHeight / 2)
    gamePad.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.stop(-1)
    sys.exit()  # 게임 종료

init_game()
runGame()

