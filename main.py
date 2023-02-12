import pygame

from pygame_utils import PygameScreen, Colors
from tech_utils import Tech

screen_width = 600
screen_height = 900

pygame.init()
screen = PygameScreen(screen_width, screen_height, 10, 20)

screen.color_screen_grey()
screen.refresh_screen()
screen.draw_map()
screen.get_map_blocks()
print(screen.block_height, screen.block_width)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for block in screen.map_blocks:
                if Tech.is_mouse_inside_block(block):
                    block.color = Colors.black
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            for block in screen.map_blocks:
                if Tech.is_mouse_inside_block(block):
                    block.color = Colors.white
    screen.draw_squares(screen.map_blocks)
    screen.refresh_screen()


