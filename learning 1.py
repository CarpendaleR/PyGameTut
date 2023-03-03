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

# time.sleep(5)
quit_game = False
while quit_game == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
pygame.quit()
quit()
