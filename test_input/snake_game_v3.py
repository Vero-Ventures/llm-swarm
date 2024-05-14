import os
import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SNAKE_LENGTH = 1
APPLE_SIZE = 1
FPS = 30

class SnakeGame:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.snake = []
        self.apple = None
        self.score = 0

    def setup(self):
        os.mkdir('Snake Game')
        os.chdir('Snake Game')
        open('snake_game.py', 'w').close()
        open('game_settings.py', 'w').close()

    def game_settings(self, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT):
        with open("game_settings.py", "a") as file:
            file.write(f"\nSCREEN_WIDTH = {screen_width}\n")
            file.write(f"SCREEN_HEIGHT = {screen_height}\n")
            file.write(f"SNAKE_LENGTH = {SNAKE_LENGTH}\n")
            file.write(f"APPLE_SIZE = {APPLE_SIZE}\n")
            file.write(f"FPS = {FPS}\n")

    def init_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = [pygame.Rect(x*10, 0, 10, 10) for x in range(SNAKE_LENGTH)]

    def draw_grid(self):
        for i in range(SCREEN_WIDTH//10):
            pygame.draw.line(self.screen, (255, 255, 255), (i*10, 0), (i*10, SCREEN_HEIGHT))
        for i in range(SCREEN_HEIGHT//10):
            pygame.draw.line(self.screen, (255, 255, 255), (0, i*10), (SCREEN_WIDTH, i*10))

    def move_snake(self, direction):
        if direction == 'up':
            self.snake[0].move_ip(0, -10)
        elif direction == 'down':
            self.snake[0].move_ip(0, 10)
        elif direction == 'left':
            self.snake[0].move_ip(-10, 0)
        elif direction == 'right':
            self.snake[0].move_ip(10, 0)

    def check_collisions(self):
        if self.snake[0].x < 0 or self.snake[0].y < 0 or self.snake[0].x >= SCREEN_WIDTH or self.snake[0].y >= SCREEN_HEIGHT:
            self.game_over()
        for i in range(1, len(self.snake)):
            if self.snake[0].colliderect(self.snake[i]):
                self.game_over()

    def game_over(self):
        pygame.quit()

    def main_loop(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.move_snake('up')
            elif keys[pygame.K_DOWN]:
                self.move_snake('down')
            elif keys[pygame.K_LEFT]:
                self.move_snake('left')
            elif keys[pygame.K_RIGHT]:
                self.move_snake('right')
            self.check_collisions()
            pygame.display.flip()


game = SnakeGame()
game.main_loop()
