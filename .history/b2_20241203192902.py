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

    def move(self, dx, dy, bbox):
        dx = max(bbox[0], min(self.x + dx, bbox[1] - self.width))
        dy = max(0, min(self.y + dy, bbox[2] - self.height))

        self.x = dx
        self.y = dy

class Obstacle:
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.speed = speed

        self.color = random.choice(LIST_COLOR)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def move(self):
        self.y += self.speed

class UI:

    def draw_text(self, screen, text, x, y, font_size=30, color=(255, 255, 255)):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect(center=(x, y))
        screen.blit(rendered_text, text_rect)

    def draw_game_info(self, screen, score, lives, speed, x, y):
        self.draw_text(screen, f"Score: {score}", x, y)
        self.draw_text(screen, f"Lives: {lives}", x, y + 40)
        self.draw_text(screen, f"Speed: {speed:.2f}", x, y + 80)

