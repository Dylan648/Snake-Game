import pygame, random
import pygame.freetype
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption('game')

GAME_FONT = pygame.freetype.Font("font.ttf", 24)
player_x = 250
player_y = 400
enemy_x = 250
enemy_y = 0
player_height = 20
player_width = 20
player_speed = 10
enemy_speed = 10
score = 0

is_running = True

while is_running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
    
    enemy_y += enemy_speed
    if enemy_y > 500:
        enemy_y = 0
        enemy_x = random.randint(25,475)
        score += 1

    window.fill((0,0,0)) 
    GAME_FONT.render_to(window, (250, 10), str(score), (255, 255, 255))
    player = pygame.draw.rect(window, (255,0,0), (player_x, player_y, player_height, player_width))
    enemy = pygame.draw.rect(window, (0,0,255), (enemy_x, enemy_y, player_height, player_width))

    if player.colliderect(enemy):
        enemy_speed = 0
        player_speed = 0
        if event.type == pygame.KEYUP:
            if keys[pygame.K_r]:
                #this doesnt quite work yet, screen needs to update before it actually restarts.
                score = 0
                enemy_speed = 10
                enemy_y = 10
                enemy_x = 250
                player_speed = 10
                player_x = 250
                player_y = 400
    elif score > 5:
        enemy_speed = 15
    elif score > 10:
        enemy_speed = 20
    pygame.display.update()
