import pygame


pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My Game")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

pygame.display.update()

pygame.draw.rect(window, "blue", pygame.rect(0, 0, 100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            # break

    

    pygame.display.update()