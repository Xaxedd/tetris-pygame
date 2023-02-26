import pygame

from classes.blocks import Side
from utils.pygame_utils import PygameScreen
from utils.tech_utils import Tech
from user_settings import Settings


def add_falling_block_to_obstacles():
    global screen
    for block in screen.falling_block:
        screen.obstacles.append(block)


pygame.init()
pygame.font.init()
screen = PygameScreen(Settings.screen_width, Settings.screen_height, Settings.horizontal_blocks_amount, Settings.vertical_blocks_amount)
max_fps = 60
fps_clock = pygame.time.Clock()

screen.color_screen_grey()
screen.refresh_screen()
screen.draw_map()
screen.create_map_blocks()
screen.spawn_random_block()
screen.get_piece_shadow()
print(screen.block_height, screen.block_width)
iteration = 0
while True:
    xxx = False

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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            screen.falling_block = screen.piece_shadow
            xxx = True

    if iteration % 40 == 0 or xxx:
        max_y = Tech.get_piece_max_y(screen.falling_block)
        if max_y < Settings.vertical_blocks_amount - 1:
            if not Tech.is_there_block_on_the_side_of_piece(screen.falling_block, Side.BOTTOM, screen.obstacles):
                for block in screen.falling_block:
                    block.y += 1
                for block in screen.rotate_grid:
                    block.map_y += 1
            else:
                add_falling_block_to_obstacles()
                screen.spawn_random_block()
        elif max_y == Settings.vertical_blocks_amount - 1:
            add_falling_block_to_obstacles()
            screen.spawn_random_block()

        if len(screen.obstacles) > Settings.horizontal_blocks_amount:
            screen.try_to_delete_full_lines()

    screen.get_piece_shadow()
    screen.draw_squares()
    screen.refresh_screen()
    fps_clock.tick(max_fps)
    iteration += 1




