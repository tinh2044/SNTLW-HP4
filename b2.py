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

    def draw_text(self, screen, text, x, y, font_size=30):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        rendered_text = font.render(text, True, WHITE)
        text_rect = rendered_text.get_rect(center=(x, y))
        screen.blit(rendered_text, text_rect)

    def draw_game_info(self, screen, score, lives, speed, x, y):
        self.draw_text(screen, f"Score: {score}", x, y)
        self.draw_text(screen, f"Lives: {lives}", x, y + 40)
        self.draw_text(screen, f"Speed: {speed:.2f}", x, y + 80)

class GameManager:
    def __init__(self):
        pygame.init()
        self.w = 800
        self.h = 600
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.score = 0
        self.speed = 2
        self.obstacles = []

        self.road_width = self.width // 4
        self.num_road = self.width // self.road_width
        self.ui = UI()

        self.player = Player(self.road_width * 2, self.height - 100, 60, 100)

        self.obstacle_types = {
            "car": {"width": 60, "height": 120, "speed": 1, "colors": LIST_COLOR},
            "bike": {"width": 40, "height": 100, "speed": 1.5, "colors": LIST_COLOR},
            "truck": {"width": 100, "height": 150, "speed": 0.75, "colors": LIST_COLOR},
        }
