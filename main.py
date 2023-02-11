import pygame

from pygame_utils import PygameScreen

screen_width = 600
screen_height = 900

pygame.init()
screen = PygameScreen(screen_width, screen_height)
screen.color_screen_white()
screen.refresh_screen()
screen.draw_map()
input()

