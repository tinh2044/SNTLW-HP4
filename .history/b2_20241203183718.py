import pygame


pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My Game")

pygame.display.update()

color = "green"

pygame.draw.line(window, "green", (200, 200), (300, 300), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            # break
        pass
    

    pygame.display.update()