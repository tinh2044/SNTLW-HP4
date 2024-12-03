import pygame
from pygame import display, image

pygame.init()

window = display.set_mode((800, 600))
display.set_caption("My Game")

icon = image.load("icon.png")
display.set_icon(icon)

pygame.display.update()

# pygame.draw.rect(display)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            # break

    

    pygame.display.update()