import pygame


pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My Game")

pygame.display.update()

color = "red"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if color == "red":
                color = "green"
            else:
                color = "red"
    pygame.draw.rect(window, color, (200, 200), (300, 300), 10)



    pygame.display.update()