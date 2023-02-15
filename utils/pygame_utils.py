from typing import List
from random import randint

import pygame

from classes.blocks import MapBlock
from classes.colors import Colors
from user_settings import Settings


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

    def xxx(self):
        pygame.draw.rect(surface=self.screen,
                         color=Colors.yellow,
                         rect=pygame.Rect(self.padding_horizontal, self.padding_vertical, self.map_width, self.map_height))
        self.draw_map_inside()
        self.refresh_screen()

    def create_map_blocks(self):
        for y in range(-3, self.blocks_vertically):
            for x in range(self.blocks_horizontally):
                if y < 0:
                    self.map_blocks.append(MapBlock(x=x, y=y, color=Settings.background_color))
                else:
                    self.map_blocks.append(MapBlock(x=x, y=y, color=Settings.map_color,))
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
        for rect in self.falling_block:
            pygame.draw.rect(surface=self.screen,
                             color=rect.color,
                             rect=pygame.Rect(self.padding_horizontal + rect.x * self.block_width + 1,
                                              self.padding_vertical + rect.y * self.block_height + 1,
                                              self.block_width - 1,
                                              self.block_height - 1))

    def spawn_random_block(self):
        self.falling_block = []

        value = randint(1, 7)
        if value == 1:
            blocks_to_change = list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+2))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.light_blue))

        if value == 2:
            blocks_to_change = list(range(round(self.blocks_horizontally/2)-2, round(self.blocks_horizontally/2)+1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.orange))
            self.falling_block.append(MapBlock(x=blocks_to_change[-1], y=-3, color=Colors.orange))

        if value == 3:
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2) + 1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.dark_blue))
            self.falling_block.append(MapBlock(x=blocks_to_change[0], y=-3, color=Colors.dark_blue))

        if value == 4:
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2)))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.lime))

            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2)+1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-3, color=Colors.lime))

        if value == 5:
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2)))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-3, color=Colors.red))

            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2)+1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.red))

        if value == 6:
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 2, round(self.blocks_horizontally / 2) + 1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.pink))
            self.falling_block.append(MapBlock(x=blocks_to_change[1], y=-3, color=Colors.pink))

        if value == 7:
            blocks_to_change = list(range(round(self.blocks_horizontally / 2) - 1, round(self.blocks_horizontally / 2) + 1))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-2, color=Colors.yellow))
            for i in blocks_to_change:
                self.falling_block.append(MapBlock(x=i, y=-3, color=Colors.yellow))
