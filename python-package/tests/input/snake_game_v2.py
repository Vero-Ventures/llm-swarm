# Model: Llama3
# Context: terminal
# Prompt: Please write, in Python, the Snake Game. As you write it,
# double-check that the logic is correct, so the game plays as it should

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 0)

dis_width = 600
dis_height = 400

display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)

def Your_score(score):
    text = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(text, [0, 10])

def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, "black", [x[0], x[1], 10, 10])
        pygame.display.update()

def message_to_screen(msg, color):
    screen_text = font_style.render(msg, True, color)
    display.blit(screen_text, [dis_width/6, dis_height/3])

def gameLoop():
    global clock
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    foodx = round(random.randint(0, (dis_width-10))/10.0)*10.0
    foody = round(random.randint(0, (dis_height-10))/10.0)*10.0

    while not game_over:
        while game_close:
            display.fill(white)
            message_to_screen("You Lost! Press C-Play Again or Q-Quit", "red")
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                x1_change = -10
                y1_change = 0
            elif keys[pygame.K_RIGHT]:
                x1_change = 10
                y1_change = 0
            elif keys[pygame.K_UP]:
                y1_change = -10
                x1_change = 0
            elif keys[pygame.K_DOWN]:
                y1_change = 10
                x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change

            display.fill(white)
            pygame.draw.rect(display, "green", [foodx, foody, 10, 10])
            Your_score(Length_of_snake - 1)

            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > Length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_list)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randint(0, (dis_width-10))/10.0)*10.0
                foody = round(random.randint(0, (dis_height-10))/10.0)*10.0
                Length_of_snake += 1

            clock.tick(10)

    pygame.quit()
    quit()

gameLoop()
