
pygame.display.update()  # 게임화면을 다시그림

# 미사일로 운석을 파괴하기 위한 모습
def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padwidth, padHeight))
    pygame.display.set_caption("PyShooting")  # 게임 이름
    background = pygame.image.load('background.png')  # 배경 그림
    fighter = pygame.image.load('fighter.png')  # 전투기 그림
    missile = pygame.image.load('missile.png')  # 미사일 그림
    explosion = pygame.image.load('explosion.png')  # 폭발 그림
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter, missile, explosion
    # 전투기 미사일에 운석이 맞았을 경우
    isShot = False
    shotCount = 0
    rockPassed = 0
    
    onGame = False
    while not onGame:
        pass
        # 여기에 게임 루프 코드 추가

# 미사일로 운석 파괴하기 하지만 투명임
if len(missileXY) != 0:
    for i, bxy in enumerate(missileXY):
        # 미사일 요소에 대해 반복함
        bxy[1] -= 10  # 총알의 y좌표를 위로 이동
        missileXY[i][1] = bxy[1]
        
        # 미사일이 운석을 맞추었을 경우
        if bxy[1] < rockY:
            if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                missileXY.remove(bxy)
                isShot = True
                shotCount += 1
        
        # 미사일이 화면 밖을 벗어나면
        if bxy[1] <= 0:
            try:
                missileXY.remove(bxy)  # 미사일 제거
            except:
                pass
# 운석을 맞춘 경우
if isShot:
    # 운석 폭발
    drawobject(explosion, rockX, rockY)  # 운석 폭발 그리기
    
    # 새로운 운석 (랜덤)
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    isShot = False
    
    drawobject(rock, rockX, rockY)  # 운석 그리기

# 파괴한 운석수와 놓친 운석수 표시하기 1
# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수: ' + str(count), True, (255, 255, 255))
    gamePad.blit(text, (10, 0))

# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('통과한 운석: ' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (360, 0))

# 운석을 맞춘 점수 표시
writeScore(shotCount)

rockY += rockSpeed  # 운석 아래로 움직임

# 운석이 지구로 떨어진 경우
if rockY > padHeight:
    # 새로운 운석 (랜덤)
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padwidth - rockWidth)
    rockY = 0
    rockPassed += 1

    # 놓친 운석 개수 표시
    writePassed(rockPassed)

#운석을 맞추면 속도 증가시키기
# 운석을 맞춘 경우
if isShot:
    # 운석 폭발
    drawobject(explosion, rockX, rockY)  # 운석 폭발 그리기

    # 새로운 운석 (랜덤)
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    isShot = False

    # 운석 맞추면 속도 증가
    rockSpeed += 0.02
    if rockSpeed > -10:
        rockSpeed = 10
#게임오버
# 게임 메시지 출력
def writeMessage(text):
    global gamePad
    textFont = pygame.font.Font('NanumGothic.ttf', 60)
    textSurface = textFont.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth / 2, padHeight / 2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()

# 전투기가 운석과 충돌했을 때 메시지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴!')

# 게임 오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')

# 전투기 위치 재조정
x += fighterX
if x < 0:
    x = 0
elif x > padWidth - fighterWidth:
    x = padWidth - fighterWidth

# 전투기가 운석과 충돌했는지 체크
if y < rockY + rockHeight:
    if (rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
        crash()

drawobject(fighter, Xt, y)

# 운석을 놓친 개수가 3개 이상이면 게임 오버
if rockPassed == 3:
    gameOver()

# 놓친 운석 개수 표시
writePassed(rockPassed)

# 게임 사운드 넣기ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ
padWidth = 480  # 게임 화면의 가로 크기
padHeight = 640  # 게임 화면의 세로 크기

rockImage = [
    'rock01.png', 'rock02.png', 'rock03.png',
    'rock04.png', 'rock05.png', 'rock06.png',
    'rock07.png', 'rock08.png', 'rock09.png',
    'rock10.png', 'rock11.png', 'rock12.png',
    'rock13.png', 'rock14.png', 'rock15.png',
    'rock16.png', 'rock17.png', 'rock18.png',
    'rock19.png', 'rock20.png', 'rock21.png',
    'rock22.png', 'rock23.png', 'rock24.png',
    'rock25.png', 'rock26.png', 'rock27.png',
    'rock28.png', 'rock29.png', 'rock30.png'
]

explosionSound = [
    'explosion01.wav', 'explosion02.wav',
    'explosion03.wav', 'explosion04.wav'
]

def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption("PyShooting")
    background = pygame.image.load("background.png")
    # fighter = pygame.image.load('fighter.png')
    missile = pygame.image.load('missile.png')
    explosion = pygame.image.load('explosion.png')
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('missile.wav')
    gameOverSound = pygame.mixer.Sound('gameover.wav')
    clock = pygame.time.Clock()

def runGame(): 
    global gamepad, clock, background, fighter, missile, explosion, missileSound

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # 미사일 발사
                missileSound.play()  # 미사일 사운드 재생 
                missileX = x + fighterWidth / 2 
                missileY = y - fighterHeight 
                missileXY.append([missileX, missileY])
#def runGame(): 
    #global gamepad, clock, background, fighter, missile, explosion, missileSound

    #elif event.key == pygame.K_SPACE:  # 미사일 발사
        #missileSound.play()  # 미사일 사운드 재생 
        #missileX = x + fighterWidth / 2 
        #missileY = y - fighterHeight 
        #missileXY.append([missileX, missileY])

# 소리 2    게임 메시지 출력
def writeMessage(text):
    global gamePad, gameOverSound
    textFont = pygame.font.Font('NanumGothic.ttf', 80)
    textSurface = textFont.render(text, True, (255, 0, 0))
    textRect = textSurface.get_rect()
    textRect.center = (padWidth / 2, padHeight / 2)
    gamePad.blit(textSurface, textRect)
    pygame.display.update()
    pygame.mixer.music.stop()  # 배경 음악 정지
    gameOverSound.play()  # 게임 오버 사운드 재생
    sleep(2)
    pygame.mixer.music.play(-1)  # 배경 음악 재생
    runGame()

# 운석을 맞춘 경우
if isShot:
    # 운석 폭발
    drawObject(explosion, rockX, rockY)  # 운석 폭발 그리기
    destroySound.play()  # 운석 폭발 사운드 재생

    # 새로운 운석 (랜덤)
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
    isShot = False

# 운석 랜덤 생성
rock = pygame.image.load(random.choice(rockImage))
rockSize = rock.get_rect().size  # 운석 크기
rockWidth = rockSize[0]
rockHeight = rockSize[1]
destroySound = pygame.mixer.Sound(random.choice(explosionSound))