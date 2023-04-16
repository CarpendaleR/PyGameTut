# Pygame tutorial from level 3 workbook
# Carpendale 2023

import pygame
import time

pygame.init()
screen_size_x = 800
screen_size_y = 600
# game_icon = pygame.image.load(' name of image file ')
# pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game, oh yeah")
screen_size = pygame.display.set_mode((screen_size_x, screen_size_y), pygame.RESIZABLE)

green = (205, 225, 200)
red = (5, 225, 200)
blue = (5, 25, 200)
black = (105, 125, 200)
white = (105, 225, 200)

snake_x = 400 # screen_size_x / 2
snake_y = 300 # screen_size_y / 2

snake_x_change = 0
snake_y_change = 0

pygame.draw.rect(screen_size, blue, [snake_x, snake_y, 20, 20])
pygame.display.update()

clock = pygame.time.Clock()
# time.sleep(5)
quit_game = False
while quit_game == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # -----FOLLOWING GUIDE DID NOT WORK WITH THE BELOW CODE
    #    if event.type == pygame.KEYDOWN:
    #        if event.type == pygame.K_LEFT:
    #            snake_x_change = -20
    #            snake_y_change = 0
    #        elif event.type == pygame.K_RIGHT:
    #            snake_x_change = 20
    #            snake_y_change = 0
    #        elif event.type == pygame.K_UP:
    #            snake_x_change = 0
    #            snake_y_change = 20
    #        elif event.type == pygame.K_DOWN:
    #            snake_x_change = 0
    #           snake_y_change = -20

    # -----FIXED VERSION OF CODE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
                snake_x_change = -20
                snake_y_change = 0
    if keys[pygame.K_RIGHT]:
                snake_x_change = 20
                snake_y_change = 0
    if keys[pygame.K_DOWN]:
                snake_x_change = 0
                snake_y_change = 20
    if keys[pygame.K_UP]:
                snake_x_change = 0
                snake_y_change = -20


    snake_x += snake_x_change
    snake_y += snake_y_change

    screen_size.fill(green) # ------screen_size.fill NOT screen.fill
    pygame.draw.rect(screen_size, red, [snake_x, snake_y, 20, 20]) # Need to redraw the snake
    clock.tick(10) # Sets speed of snake
    pygame.display.update() # ------Need to update the display


pygame.quit()
quit()
