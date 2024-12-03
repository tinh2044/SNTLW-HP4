import sys
import random
import pygame

width = 800
height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

LIST_COLOR = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, ORANGE]


class Player:
    def __init__(self, x, y, car_width, car_height, color):
        self.x = x
        self.y = y
        self.width = car_width
        self.height = car_height
        self.color = color
        self.lives = 3

    def move(self, dx, dy, boundaries):
        self.x = max(boundaries[0], min(self.x + dx, boundaries[1] - self.width))
        self.y = max(0, min(self.y + dy, boundaries[2] - self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class Obstacle:
    def __init__(self, obj_type, x, y, width, height, speed, colors):
        self.type = obj_type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = random.choice(colors)

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


class UIManager:

    def draw_text(self, screen, text, x, y, font_size=30, color=(255, 255, 255)):
        font = pygame.font.Font('freesansbold.ttf', font_size)
        rendered_text = font.render(text, True, color)
        text_rect = rendered_text.get_rect(center=(x, y))
        screen.blit(rendered_text, text_rect)

    def draw_game_info(self, screen, score, lives, speed, x, y):
        self.draw_text(screen, f"Score: {score}", x, y)
        self.draw_text(screen, f"Lives: {lives}", x, y + 40)
        self.draw_text(screen, f"Speed: {speed:.2f}", x, y + 80)


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0
        self.speed = 2
        self.obstacles = []
        self.road_width = self.width // 4
        self.num_road = self.width // self.road_width
        self.ui_manager = UIManager()

        self.player = Player(self.road_width * 2, self.height - 100, 60, 100, RED)

        self.obstacle_types = {
            "car": {"width": 60, "height": 120, "speed": 1, "colors": LIST_COLOR},
            "bike": {"width": 40, "height": 100, "speed": 1.5, "colors": LIST_COLOR},
            "truck": {"width": 100, "height": 150, "speed": 0.75, "colors": LIST_COLOR},
        }

    def spawn_obstacle(self):

        obj_type = random.choice(list(self.obstacle_types.keys()))
        obstacle_type = self.obstacle_types[obj_type]

        lane = random.randint(1, self.num_road - 1)
        x = (lane + 1) * (self.width // 4) + obstacle_type["width"] // 2
        y = -obstacle_type["height"]
        speed = self.speed * obstacle_type["speed"]
        obstacle = Obstacle(obj_type, x, y, obstacle_type["width"], obstacle_type["height"], speed, obstacle_type["colors"])

        self.obstacles.append(obstacle)

    def handle_collisions(self):
        for obstacle in self.obstacles:
            if (self.player.x < obstacle.x + obstacle.width and
                    self.player.x + self.player.width > obstacle.x and
                    self.player.y < obstacle.y + obstacle.height and
                    self.player.y + self.player.height > obstacle.y):
                self.player.lives -= 1
                self.obstacles.remove(obstacle)
                if self.player.lives <= 0:
                    self.running = False

    def update_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.move()
            if obstacle.y > self.height:
                self.obstacles.remove(obstacle)
                self.score += 1

    def render(self):

        row_width = self.width // 4
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, GRAY, pygame.Rect(row_width, 0, row_width * 4, self.height))

        for i in range(1, 4):
            pygame.draw.line(self.screen, WHITE, (i * row_width, 0), (i * row_width, self.height), 6)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        self.player.draw(self.screen)

        self.ui_manager.draw_game_info(self.screen, self.score, self.player.lives, self.speed, 100, 50)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move(-5, 0, (self.road_width, self.road_width*self.num_road-1, self.height))
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move(5, 0, (self.road_width, self.road_width*self.num_road-1, self.height))
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.player.move(0, -5, (self.road_width, self.road_width*self.num_road-1, self.height))
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player.move(0, 5, (self.road_width, self.road_width*self.num_road-1, self.height))

            self.update_obstacles()
            self.handle_collisions()

            if random.random() < 0.02:
                self.spawn_obstacle()

            self.render()

            self.speed += 0.001
            self.clock.tick(60)


if __name__ == "__main__":
    game = GameManager()
    game.run()
    pygame.quit()
    sys.exit()
