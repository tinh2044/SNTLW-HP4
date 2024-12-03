import pygame


pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My Game")

pygame.display.update()

color = "green"



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()

    pygame.draw.line(window, color, (200, 200), (300, 300), 10)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            color = (225, 0, 0)
        else:
            color = "green"

    pygame.display.update()