from dataclasses import dataclass
from typing import List

import pygame


@dataclass
class Colors:
    black = [0, 0, 0]
    white = [255, 255, 255]
    grey = [142, 147, 156]
    yellow = [230, 172, 37]


@dataclass
class MapBlock:
    x: int
    y: int
    color: List[int]
    screen_pos: pygame.Rect


class PygameScreen:
    def __init__(self, screen_witdh, screen_height, blocks_horizontally=0, blocks_vertically=0):
        self.screen_width = screen_witdh
        self.screen_height = screen_height
        self.blocks_horizontally = blocks_horizontally
        self.blocks_vertically = blocks_vertically
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.map_height = self.screen_height - 200
        self.map_width = self.map_height/2
        self.padding_horizontal = (self.screen_width - self.map_width) / 2
        self.padding_vertical = (self.screen_height - self.map_height) / 2
        self.block_height = 0
        self.block_width = 0
        self.map_blocks: List[MapBlock] = []

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

    def get_map_blocks(self):
        for y in range(self.blocks_vertically):
            for x in range(self.blocks_horizontally):
                self.map_blocks.append(MapBlock(x=x, y=y, color=Colors.white,
                                                screen_pos=pygame.Rect(self.padding_horizontal + x*self.block_width+1,
                                                                       self.padding_vertical + y*self.block_height + 1,
                                                                       self.block_width-1,
                                                                       self.block_height-1)))
        print(self.map_blocks)

    def test_squares_fillings(self):
        for rect in self.map_blocks:
            pygame.draw.rect(surface=self.screen,
                             color=Colors.yellow,
                             rect=rect.screen_pos)
            print("drawing")
        self.refresh_screen()

    def draw_squares(self, map_blocks):
        for rect in map_blocks:
            pygame.draw.rect(surface=self.screen,
                             color=rect.color,
                             rect=rect.screen_pos)
