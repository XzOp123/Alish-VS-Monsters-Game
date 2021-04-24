import pygame
import random
from math import sqrt
from pygame import mixer

pygame.init()
pygame.mixer.init()

explosion = pygame.mixer.Sound('explosion.wav')
laser = pygame.mixer.Sound('laser.wav')
pygame.mixer.music.load('music.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
mario = pygame.mixer.Sound('mario_sound_end.mp3')

image = random.choices(['cthulhu.png', 'enemy.png'])

pygame.display.Info()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alish VS Monsters")
icon = pygame.image.load(r'3d-movie.png')
pygame.display.set_icon(icon)

background1 = pygame.image.load('background_1.png')

beta_font = pygame.font.Font('freesansbold.ttf', 15)
arrow_font = pygame.font.Font('freesansbold.ttf', 35)


def beta_func():
    beta_set = beta_font.render(f'v.1.2.6(alpha)', True, (255, 255, 255))
    screen.blit(beta_set, (5, 5))


def arrow_right():
    right_set = arrow_font.render(f'<--------', True, (0, 0, 0))
    screen.blit(right_set, (540, 355))


def arrow_left():
    left_set = arrow_font.render(f'-------->', True, (0, 0, 0))
    screen.blit(left_set, (150, 355))


EnemyIMG = []
EnemyX = []
EnemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 9
for i in range(num_of_enemies):
    EnemyIMG.append(pygame.image.load('cthulhu.png'))
    EnemyX.append(random.randint(0, 736))
    EnemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

PlayerIMG = pygame.image.load(r'176458889_208370900743684_7423843189261827827_n.png')
PlayerIMG = pygame.transform.smoothscale(PlayerIMG, (64, 64))
PlayerX = 370
PlayerY = 480
playerX_change = 0

BulletIMG = pygame.image.load('bullet.png')
BulletX = 0
BulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('balloons.ttf', 32)
TestX = 330
TestY = 10


def show_score(x, y):
    score = font.render(f'Score : {str(score_value)}', True, (255, 255, 255))
    if score_value >= 20:
        score = font.render(f'Score : {str(score_value)}', True, (36, 206, 219))
    if score_value >= 50:
        score = font.render(f'Score : {str(score_value)}', True, (218, 165, 32))

    screen.blit(score, (x, y))


over_font = pygame.font.Font('monster shadow.ttf', 75)


def smili_right():
    right = pygame.image.load('right.png')
    right = pygame.transform.smoothscale(right, (128, 128))
    screen.blit(right, (650, 150))


def smili_left():
    left = pygame.image.load('left.png')
    left = pygame.transform.smoothscale(left, (128, 128))
    screen.blit(left, (50, 150))


def player(x, y):
    screen.blit(PlayerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyIMG[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(BulletIMG, (x + 16, y + 10))


def isCollision(EnemyX, EnemyY, BulletX, BulletY):
    distance = sqrt(((EnemyX - BulletX)) ** 2 + ((EnemyY - BulletY) ** 2))
    if distance < 27:
        return True
    else:
        return False


def start_hello():
    over_text = over_font.render(f'Alish VS Monsters!', True, (255, 100, 255))
    screen.blit(over_text, (40, 160))


action = None


def buttons():
    global action
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 90 + 210 > mouse[0] > 90 and 400 + 125 > mouse[1] > 400:
        pygame.draw.rect(screen, (0, 255, 0), (90, 400, 210, 125))
        if click[0] == True:
            action = True
    else:
        pygame.draw.rect(screen, (0, 125, 0), (90, 400, 210, 125))

    if 500 + 210 > mouse[0] > 500 and 400 + 125 > mouse[1] > 400:
        pygame.draw.rect(screen, (255, 0, 0), (500, 400, 210, 125))
        if click[0] == True:
            action = False
            quit()
    else:
        pygame.draw.rect(screen, (125, 0, 0), (500, 400, 210, 125))

    if 757 + 40 > mouse[0] > 757 and 0 + 40 > mouse[1] > 0:
        pygame.draw.rect(screen, (32, 32, 32), (757, 3, 40, 40))
        pygame.draw.rect(screen, (32, 32, 32), (518, 3, 237, 120))
        info_text1 = beta_font.render(f"'Press SPACE' to shoot Bullet", True, (255, 0, 0))
        screen.blit(info_text1, (530, 10))
        info_text2 = beta_font.render(f"You cant play again if you die", True, (0, 255, 0))
        screen.blit(info_text2, (532, 27))
        info_text3 = beta_font.render(f"Use'<' and '>' arrow key to move ", True, (0, 255, 255))
        screen.blit(info_text3, (522, 47))
        info_text4 = beta_font.render(f"Kill as Many monsters as you", True, (255, 255, 0))
        screen.blit(info_text4, (528, 67))
        info_text5 = beta_font.render(f"POSSIBLY CAN!", True, (255, 255, 0))
        screen.blit(info_text5, (568, 81))
        info_text6 = beta_font.render(f"GOOD LUCK!", True, (255, 255, 255))
        screen.blit(info_text6, (583, 105))


    else:
        pygame.draw.rect(screen, (0, 0, 0), (757, 3, 40, 40))

    button_word = pygame.font.Font('freesansbold.ttf', 25)
    button_set = button_word.render(f'PLAY!', True, (255, 255, 255))
    screen.blit(button_set, (155, 455))
    button_set2 = button_word.render(f'QUIT', True, (255, 255, 255))
    screen.blit(button_set2, (575, 455))
    button_set = button_word.render(f'?', True, (255, 255, 255))
    screen.blit(button_set, (770, 13))


start_screen = True


def game_over_text():
    global action
    screen.fill((128, 255, 0))
    over_text = over_font.render(f'Game Over!', True, (255, 255, 255))
    screen.blit(over_text, (190, 110))
    smili_left()
    smili_right()
    arrow_left()
    arrow_right()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 300 + 210 > mouse[0] > 300 and 300 + 125 > mouse[1] > 300:
        pygame.draw.rect(screen, (255, 0, 0), (300, 300, 210, 125))
        if click[0] == True:
            quit()
    else:
        pygame.draw.rect(screen, (125, 0, 0), (300, 300, 210, 125))

    button_word = pygame.font.Font('freesansbold.ttf', 25)
    button_set2 = button_word.render(f'QUIT', True, (255, 255, 255))
    screen.blit(button_set2, (370, 355))


while start_screen == True and action == None:
    screen.fill((76, 0, 153))
    start_hello()
    beta_func()
    buttons()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            start_screen = False

            quit()

    pygame.display.update()

while action:
    screen.blit(background1, (0, 0))
    beta_func()

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
            quit()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                playerX_change = -5
            if events.key == pygame.K_RIGHT:
                playerX_change = 5

            if events.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    laser.set_volume(0.2)
                    laser.play()
                    BulletX = PlayerX
                    fire_bullet(BulletX, BulletY)

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
                playerX_change = 0

    PlayerX += playerX_change

    if PlayerX <= 0:
        PlayerX = 0
    elif PlayerX >= 736:
        PlayerX = 736

    for i in range(num_of_enemies):

        if EnemyY[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 20000
                mario.set_volume(0.05)
                pygame.mixer.music.stop()
                mario.play(0)
            game_over_text()
            break

        EnemyX[i] += enemyX_change[i]
        if EnemyX[i] <= 0:
            enemyX_change[i] = 3.8
            EnemyY[i] += enemyY_change[i]
        elif EnemyX[i] >= 736:
            enemyX_change[i] = -3.8
            EnemyY[i] += enemyY_change[i]

        collision = isCollision(EnemyX[i], EnemyY[i], BulletX, BulletY)
        if collision:
            explosion.set_volume(0.08)
            explosion.play()
            BulletY = 480
            bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = random.randint(50, 150)

        enemy(EnemyX[i], EnemyY[i], i)

    if BulletY <= 0:
        BulletY = 480
        bullet_state = 'ready'

    if bullet_state == "fire":
        fire_bullet(BulletX, BulletY)
        BulletY -= bulletY_change

    player(PlayerX, PlayerY)
    show_score(TestX, TestY)
    pygame.display.update()
