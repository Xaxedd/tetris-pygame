import pygame

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
                for block in screen.falling_block:
                    block.x -= 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            max_x = Tech.get_piece_max_x(screen.falling_block)
            if max_x < Settings.horizontal_blocks_amount-1:
                for block in screen.falling_block:
                    block.x += 1

    if iteration % 5 == 0:
        print("essa")
        max_y = Tech.get_piece_max_y(screen.falling_block)
        if max_y < Settings.vertical_blocks_amount - 1:
            blocks_on_max_y = Tech.get_xs_of_max_y_piece(screen.falling_block, max_y)
            if not Tech.check_if_there_is_block_under(screen.obstacles, blocks_on_max_y, max_y):
                for block in screen.falling_block:
                    block.y += 1
            else:
                for block in screen.falling_block:
                    screen.obstacles.append(block)
                screen.spawn_random_block()
        if max_y == Settings.vertical_blocks_amount - 1:
            for block in screen.falling_block:
                screen.obstacles.append(block)
            screen.spawn_random_block()

    screen.draw_squares()
    screen.refresh_screen()
    fps_clock.tick(max_fps)
    iteration += 1
    print(iteration)




