import pygame
import random


width = 800
height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

LIST_COLOR = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE]

class Player:
    def __init(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.x, self.y, self.w, self.h))

    def move(self, dx, dy, boundaries):
        #(100, 300, 600)
        self.x = max(boundaries[0], min(self.x + dx, boundaries[1] - self.width))
        self.y = max(0, min(self.y + dy, boundaries[2] - self.height))