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
            sorted_obstacles = sorted(screen.obstacles, key=lambda x: (x.y, x.x))
            amount_of_obstacles_in_line = 0
            to_delete = []
            current_y = sorted_obstacles[0].y

            for block in sorted_obstacles:
                if block.y != current_y:
                    current_y = block.y
                    amount_of_obstacles_in_line = 0
                amount_of_obstacles_in_line += 1

                if amount_of_obstacles_in_line == Settings.horizontal_blocks_amount:
                    screen.lines_cleared += 1
                    screen.draw_lines_cleared_text()
                    for index, xxx in enumerate(screen.obstacles):
                        if xxx.y == current_y:
                            to_delete.append(index)
                        if xxx.y < current_y:
                            xxx.y += 1

            to_delete.sort()
            for item in reversed(to_delete):
                screen.obstacles.pop(item)

    screen.get_piece_shadow()
    screen.draw_squares()
    screen.refresh_screen()
    fps_clock.tick(max_fps)
    iteration += 1




