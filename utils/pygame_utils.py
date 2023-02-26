import copy
from typing import List
from random import randint

import pygame

from classes.blocks import MapBlock, RotateGridBlock, RotationType, Side
from classes.colors import Colors
from user_settings import Settings
from utils.tech_utils import Tech


class PygameScreen:
    def __init__(self, screen_witdh, screen_height, blocks_horizontally=0, blocks_vertically=0):
        self.screen_width = screen_witdh
        self.screen_height = screen_height
        self.blocks_horizontally = blocks_horizontally
        self.blocks_vertically = blocks_vertically
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.map_height = self.screen_height - 300
        self.map_width = self.map_height/2
        self.padding_horizontal = (self.screen_width - self.map_width) / 2
        self.padding_vertical = (self.screen_height - self.map_height) / 2
        self.block_height = 0
        self.block_width = 0
        self.map_blocks: List[MapBlock] = []
        self.obstacles: List[MapBlock] = []
        self.falling_block: List[MapBlock] = []
        self.rotate_grid: List[RotateGridBlock] = []
        self.piece_shadow: List[MapBlock] = []

    def color_screen_white(self):
        self.screen.fill(Colors.white)

    def color_screen_grey(self):
        self.screen.fill(Colors.grey)

    @staticmethod
    def refresh_screen():
        pygame.display.flip()

    def draw_map(self):
        self.draw_map_borders()
        self.draw_map_inside()

        self.refresh_screen()

    def draw_map_borders(self):
        pygame.draw.line(self.screen, Colors.black, (self.padding_horizontal - 6, self.padding_vertical), (self.padding_horizontal - 6, self.screen_height - self.padding_vertical + 11), 11)
        pygame.draw.line(self.screen, Colors.black, (self.screen_width - self.padding_horizontal + 6, self.padding_vertical), (self.screen_width - self.padding_horizontal + 6, self.screen_height - self.padding_vertical + 11), 11)

        pygame.draw.line(self.screen, Colors.black, (self.padding_horizontal, self.screen_height - self.padding_vertical + 6), (self.screen_width - self.padding_horizontal, self.screen_height - self.padding_vertical + 6), 11)

    def draw_map_inside(self):
        self.block_width = self.map_width/self.blocks_horizontally
        print("block width", self.block_width)
        for i in range(self.blocks_horizontally+1):
            pygame.draw.line(self.screen, Colors.black, (self.padding_horizontal + i*self.block_width, self.padding_vertical), (self.padding_horizontal + i*self.block_width, self.screen_height - self.padding_vertical), 1)

        self.block_height = self.map_height/self.blocks_vertically
        print("block height", self.block_height)
        for i in range(self.blocks_vertically+1):
            pygame.draw.line(self.screen, Colors.black, (self.padding_horizontal, self.screen_height - self.padding_vertical - i*self.block_height), (self.screen_width - self.padding_horizontal, self.screen_height - self.padding_vertical - i*self.block_height), 1)

    def draw_play_area_test_borders(self):
        pygame.draw.line(self.screen, Colors.yellow, (self.padding_horizontal, self.padding_vertical), (self.padding_horizontal, self.screen_height - self.padding_vertical), 3)
        pygame.draw.line(self.screen, Colors.yellow, (self.screen_width - self.padding_horizontal, self.padding_vertical), (self.screen_width - self.padding_horizontal, self.screen_height - self.padding_vertical), 3)

        pygame.draw.line(self.screen, Colors.yellow, (self.padding_horizontal, self.screen_height - self.padding_vertical), (self.screen_width - self.padding_horizontal, self.screen_height - self.padding_vertical), 3)
        pygame.draw.line(self.screen, Colors.yellow, (self.padding_horizontal, self.padding_vertical), (self.screen_width - self.padding_horizontal, self.padding_vertical), 3)

    def create_map_blocks(self):
        for y in range(-3, self.blocks_vertically):
            for x in range(self.blocks_horizontally):
                if y < 0:
                    self.map_blocks.append(MapBlock(x=x, y=y, color=Settings.background_color))
                else:
                    self.map_blocks.append(MapBlock(x=x, y=y, color=Settings.map_color))
        print(self.map_blocks)

    def draw_squares(self):
        for rect in self.map_blocks:
            pygame.draw.rect(surface=self.screen,
                             color=rect.color,
                             rect=pygame.Rect(self.padding_horizontal + rect.x * self.block_width + 1,
                                              self.padding_vertical + rect.y * self.block_height + 1,
                                              self.block_width - 1,
                                              self.block_height - 1))
        for rect in self.obstacles:
            pygame.draw.rect(surface=self.screen,
                             color=rect.color,
                             rect=pygame.Rect(self.padding_horizontal + rect.x * self.block_width + 1,
                                              self.padding_vertical + rect.y * self.block_height + 1,
                                              self.block_width - 1,
                                              self.block_height - 1))

        for rect in self.piece_shadow:
            pygame.draw.rect(surface=self.screen,
                             color=Colors.light_grey,
                             rect=pygame.Rect(self.padding_horizontal + rect.x * self.block_width + 1,
                                              self.padding_vertical + rect.y * self.block_height + 1,
                                              self.block_width - 1,
                                              self.block_height - 1))

        for rect in self.falling_block:
            pygame.draw.rect(surface=self.screen,
                             color=rect.color,
                             rect=pygame.Rect(self.padding_horizontal + rect.x * self.block_width + 1,
                                              self.padding_vertical + rect.y * self.block_height + 1,
                                              self.block_width - 1,
                                              self.block_height - 1))

    def spawn_random_block(self):
        self.falling_block = []
        self.rotate_grid = []

        value = randint(1, 7)
        if value == 1: #long 4 block
            blocks_to_change = list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+2))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.light_blue))

            for y in range(0, 4):
                for x in range(0, 4):
                    grid_block = RotateGridBlock(x=x, y=y, color=None, map_x=list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+2))[x], map_y=y-4)
                    if y == 2:
                        grid_block.color = Colors.light_blue
                    else:
                        grid_block.color = Colors.white
                    self.rotate_grid.append(grid_block)


        if value == 2: #orange L
            blocks_to_change = list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.orange))
            self.falling_block.append(MapBlock(x=blocks_to_change[-1], y=-3, color=Colors.orange))

            for y in range(3):
                for x in range(3):
                    grid_block = RotateGridBlock(x=x, y=y, color=None, map_x=list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+1))[x], map_y=y-3)
                    if y == 1:
                        grid_block.color = Colors.orange
                    elif y == 0 and x == 2:
                        grid_block.color = Colors.orange
                    else:
                        grid_block.color = Colors.white
                    self.rotate_grid.append(grid_block)

        if value == 3: #dark blue L
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2) + 1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.dark_blue))
            self.falling_block.append(MapBlock(x=blocks_to_change[0], y=-3, color=Colors.dark_blue))

            for y in range(3):
                for x in range(3):
                    grid_block = RotateGridBlock(x=x, y=y, color=None, map_x=list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+1))[x], map_y=y-3)
                    if y == 1:
                        grid_block.color = Colors.dark_blue
                    elif y == 0 and x == 0:
                        grid_block.color = Colors.dark_blue
                    else:
                        grid_block.color = Colors.white
                    self.rotate_grid.append(grid_block)

        if value == 4: #lime Z
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2)))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.lime))

            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2)+1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-3, color=Colors.lime))

            for y in range(3):
                for x in range(3):
                    grid_block = RotateGridBlock(x=x, y=y, color=None, map_x=list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2)+1))[x], map_y=y-3)

                    if y == 0 and x > 0:
                        grid_block.color = Colors.lime
                    elif y == 1 and x < 2:
                        grid_block.color = Colors.lime
                    else:
                        grid_block.color = Colors.white
                    self.rotate_grid.append(grid_block)


        if value == 5: #red Z
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2)))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-3, color=Colors.red))

            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2)+1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.red))

            for y in range(3):
                for x in range(3):
                    grid_block = RotateGridBlock(x=x, y=y, color=None, map_x=list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2) + 1))[x], map_y=y - 3)

                    if y == 0 and x < 2:
                        grid_block.color = Colors.red
                    elif y == 1 and x > 0:
                        grid_block.color = Colors.red
                    else:
                        grid_block.color = Colors.white
                    self.rotate_grid.append(grid_block)

        if value == 6: #pink T
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2) + 1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.pink))
            self.falling_block.append(MapBlock(x=blocks_to_change[1], y=-3, color=Colors.pink))

            for y in range(3):
                for x in range(3):
                    grid_block = RotateGridBlock(x=x, y=y, color=None, map_x=list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2) + 1))[x], map_y=y - 3)

                    if y == 0 and x == 1:
                        grid_block.color = Colors.pink
                    elif y == 1:
                        grid_block.color = Colors.pink
                    else:
                        grid_block.color = Colors.white
                    self.rotate_grid.append(grid_block)

        if value == 7: #yellow square
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2) + 1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.yellow))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-3, color=Colors.yellow))

            for y in range(2):
                for x in range(2):
                    grid_block = RotateGridBlock(x=x, y=y, color=Colors.yellow, map_x=list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2) + 1))[x], map_y=y - 3)
                    self.rotate_grid.append(grid_block)

    def rotate_piece_clockwise(self):
        self.rotate_piece_90_degrees(RotationType.CLOCKWISE)

    def rotate_piece_counter_clockwise(self):
        self.rotate_piece_90_degrees(RotationType.COUNTERCLOCKWISE)

    def rotate_piece_flip(self):
        self.rotate_piece_90_degrees(RotationType.FLIP)

    def rotate_piece_90_degrees(self, times: RotationType):
        falling_block_color = self.falling_block[0].color
        old_falling_block = self.falling_block
        self.falling_block = []
        temp_list = []
        cord_list = sorted(self.rotate_grid, key=lambda x: (x.y, x.x))
        yyy = []
        for block in cord_list:
            yyy.append([block.map_x, block.map_y])

        max_x = Tech.get_piece_max_x(self.rotate_grid)
        max_y = Tech.get_piece_max_y(self.rotate_grid)
        iteration = 0
        for i in range(max_y+1):
            xxx = []
            for j in range(max_x+1):
                xxx.append(self.rotate_grid[iteration].color)
                iteration += 1
            temp_list.append(xxx)
        N = len(temp_list[0])
        for rotate in range(times.value):
            for i in range(N // 2):
                for j in range(i, N - i - 1):
                    temp = temp_list[i][j]
                    temp_list[i][j] = temp_list[N - 1 - j][i]
                    temp_list[N - 1 - j][i] = temp_list[N - 1 - i][N - 1 - j]
                    temp_list[N - 1 - i][N - 1 - j] = temp_list[j][N - 1 - i]
                    temp_list[j][N - 1 - i] = temp

        colors_list = []
        for y in temp_list:
            for x in y:
                colors_list.append(x)
        for index, block in enumerate(colors_list):
            if block == falling_block_color:
                self.falling_block.append(MapBlock(x=yyy[index][0], y=yyy[index][1], color=falling_block_color))
        if Tech.is_piece_inside_obstacles(self.obstacles, self.falling_block) or Tech.is_piece_out_of_bounds(self.falling_block):
            self.falling_block = old_falling_block
        else:
            for index, color in enumerate(colors_list):
                if color == falling_block_color:
                    self.rotate_grid[index].color = color
                else:
                    self.rotate_grid[index].color = Colors.white

    def get_piece_shadow(self):
        self.piece_shadow = copy.deepcopy(self.falling_block)
        while True:
            if Tech.is_there_block_on_the_side_of_piece(self.piece_shadow, Side.BOTTOM, self.obstacles) or Tech.get_piece_max_y(self.piece_shadow) >= Settings.vertical_blocks_amount - 1:
                break
            for block in self.piece_shadow:
                block.y += 1