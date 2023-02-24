import pygame

from classes.blocks import Side
from utils.pygame_utils import PygameScreen
from utils.tech_utils import Tech
from user_settings import Settings

pygame.init()
screen = PygameScreen(Settings.screen_width, Settings.screen_height, Settings.horizontal_blocks_amount, Settings.vertical_blocks_amount)

max_fps = 60
fps_clock = pygame.time.Clock()

screen.color_screen_grey()
screen.refresh_screen()
screen.draw_map()
screen.create_map_blocks()
screen.spawn_random_block()
print(screen.block_height, screen.block_width)
iteration = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            min_x = Tech.get_piece_min_x(screen.falling_block)
            if min_x > 0:
                if not Tech.is_there_block_on_the_side_of_piece(screen.falling_block, Side.LEFT, screen.obstacles):
                    for block in screen.falling_block:
                        block.x -= 1
                    for block in screen.rotate_grid:
                        block.map_x -= 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            max_x = Tech.get_piece_max_x(screen.falling_block)
            if max_x < Settings.horizontal_blocks_amount-1:
                if not Tech.is_there_block_on_the_side_of_piece(screen.falling_block, Side.RIGHT, screen.obstacles):
                    for block in screen.falling_block:
                        block.x += 1
                    for block in screen.rotate_grid:
                        block.map_x += 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            screen.rotate_piece_clockwise()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            screen.rotate_piece_counter_clockwise()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            screen.rotate_piece_flip()

    if iteration % 20 == 0:
        max_y = Tech.get_piece_max_y(screen.falling_block)
        if max_y < Settings.vertical_blocks_amount - 1:
            if not Tech.is_there_block_on_the_side_of_piece(screen.falling_block, Side.BOTTOM, screen.obstacles):
                for block in screen.falling_block:
                    block.y += 1
                for block in screen.rotate_grid:
                    block.map_y += 1
            else:
                for block in screen.falling_block:
                    screen.obstacles.append(block)
                screen.spawn_random_block()
        elif max_y == Settings.vertical_blocks_amount - 1:
            for block in screen.falling_block:
                screen.obstacles.append(block)
            screen.spawn_random_block()

    screen.draw_squares()
    screen.refresh_screen()
    fps_clock.tick(max_fps)
    iteration += 1




