from typing import List

import pygame

from classes.blocks import MapBlock


class Tech:
    @staticmethod
    def is_mouse_inside_block(block):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (block.screen_pos[0] <= mouse_x <= block.screen_pos[0] + block.screen_pos[2]) and \
                block.screen_pos[1] <= mouse_y <= block.screen_pos[1] + block.screen_pos[3]:
            return True
        return False

    @staticmethod
    def get_piece_max_y(piece):
        return sorted(piece, key=lambda x: x.y, reverse=True)[0].y

    @staticmethod
    def get_piece_min_x(piece):
        return sorted(piece, key=lambda x: x.y)[0].x

    @staticmethod
    def get_piece_max_x(piece):
        return sorted(piece, key=lambda x: x.y)[-1].x

    @staticmethod
    def get_xs_of_max_y_piece(piece: List[MapBlock], y):
        xxx = []
        for block in piece:
            if block.y == y:
                xxx.append(block.x)
        return xxx

    @staticmethod
    def check_if_there_is_block_under(obstacles_list, list_x, y):
        for block in obstacles_list:
            if block.y == y+1:
                if block.x in list_x:
                    return True
        return False