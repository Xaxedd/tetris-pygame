from dataclasses import dataclass

import pygame


@dataclass
class Colors:
    black = [0, 0, 0]
    white = [255, 255, 255]
    yellow = [230, 172, 37]


class PygameScreen:
    def __init__(self, screen_witdh, screen_height):
        self.screen_width = screen_witdh
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])

    def color_screen_white(self):
        self.screen.fill(Colors.white)

    @staticmethod
    def refresh_screen():
        pygame.display.flip()


    def draw_map(self):
        map_height = self.screen_height - 200
        map_width = map_height/2
        padding_horizontal = (self.screen_width - map_width)/2
        padding_vertical = (self.screen_height - map_height)/2

        pygame.draw.line(self.screen, Colors.black, (padding_horizontal-6, padding_vertical), (padding_horizontal-6, self.screen_height-padding_vertical+11), 11)
        pygame.draw.line(self.screen, Colors.black, (self.screen_width - padding_horizontal+6, padding_vertical), (self.screen_width - padding_horizontal+6, self.screen_height-padding_vertical+11), 11)

        pygame.draw.line(self.screen, Colors.black, (padding_horizontal, self.screen_height-padding_vertical+6), (self.screen_width - padding_horizontal, self.screen_height-padding_vertical+6), 11)

        # pygame.draw.line(self.screen, Colors.yellow, (padding_horizontal, padding_vertical), (padding_horizontal, self.screen_height - padding_vertical), 1)
        # pygame.draw.line(self.screen, Colors.yellow, (self.screen_width - padding_horizontal, padding_vertical), (self.screen_width - padding_horizontal, self.screen_height - padding_vertical), 1)

        # pygame.draw.line(self.screen, Colors.yellow, (padding_horizontal, self.screen_height - padding_vertical), (self.screen_width - padding_horizontal, self.screen_height - padding_vertical), 1)

        block_width = map_width/10
        print("block width", block_width)
        for i in range(1, 10):
            pygame.draw.line(self.screen, Colors.black, (padding_horizontal + i*block_width, padding_vertical), (padding_horizontal + i*block_width, self.screen_height - padding_vertical), 1)
        block_height = map_height/20
        print("block height", block_height)
        for i in range(1, 21):
            pygame.draw.line(self.screen, Colors.black, (padding_horizontal, self.screen_height - padding_vertical - i*block_height), (self.screen_width - padding_horizontal, self.screen_height - padding_vertical - i*block_height), 1)
        self.refresh_screen()

