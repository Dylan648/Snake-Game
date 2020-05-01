import pygame
pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake')

player_x = 250
player_y = 250
player_height = 20
player_width = 20
speed = .5

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    window.fill((0,0,0))    
    pygame.draw.rect(window, (0,255,0), (player_x, player_y, player_height, player_width))
    pygame.display.update()

pygame.quit()