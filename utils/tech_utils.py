from typing import List

import pygame

from classes.blocks import MapBlock, Side
from user_settings import Settings


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
    def get_piece_min_y(piece):
        return sorted(piece, key=lambda x: x.y, reverse=True)[-1].y

    @staticmethod
    def get_piece_min_x(piece):
        return sorted(piece, key=lambda x: x.x)[0].x

    @staticmethod
    def get_piece_max_x(piece):
        return sorted(piece, key=lambda x: x.x)[-1].x

    @classmethod
    def is_there_block_on_the_side_of_piece(cls, piece, side: Side, obstacle_list):
        blocks_to_check = cls.piece_blocks_visible_from(piece, side)

        if side is Side.BOTTOM:
            for block in blocks_to_check:
                if cls.check_if_is_block_under(obstacle_list, block.x, block.y):
                    return True
        elif side is Side.LEFT:
            for block in blocks_to_check:
                if cls.check_if_is_block_on_the_left(obstacle_list, block.x, block.y):
                    return True
        elif side is Side.RIGHT:
            for block in blocks_to_check:
                if cls.check_if_is_block_on_the_right(obstacle_list, block.x, block.y):
                    return True
        return False

    @classmethod
    def piece_blocks_visible_from(cls, piece: List[MapBlock], side: Side):
        blocks_to_check = []
        if side is Side.BOTTOM:
            for block in piece:
                if not cls.check_if_is_block_under(piece, x=block.x, y=block.y):
                    blocks_to_check.append(block)
        elif side is Side.LEFT:
            for block in piece:
                if not cls.check_if_is_block_on_the_left(piece, x=block.x, y=block.y):
                    blocks_to_check.append(block)
        elif side is Side.RIGHT:
            for block in piece:
                if not cls.check_if_is_block_on_the_right(piece, x=block.x, y=block.y):
                    blocks_to_check.append(block)
        return blocks_to_check

    @staticmethod
    def check_if_is_block_under(obstacles_list, x, y):
        for block in obstacles_list:
            if block.y == y + 1:
                if block.x == x:
                    return True
        return False

    @staticmethod
    def check_if_is_block_on_the_left(obstacles_list, x, y):
        for block in obstacles_list:
            if block.x == x - 1:
                if block.y == y:
                    return True
        return False

    @staticmethod
    def check_if_is_block_on_the_right(obstacles_list, x, y):
        for block in obstacles_list:
            if block.x == x + 1:
                if block.y == y:
                    return True
        return False

    @staticmethod
    def is_piece_inside_obstacles(obstacles: List[MapBlock], piece: List[MapBlock]):
        for piece_block in piece:
            for block in obstacles:
                if piece_block.x == block.x and piece_block.y == block.y:
                    return True
        return False

    @staticmethod
    def is_piece_out_of_bounds(piece):
        min_x = Tech.get_piece_min_x(piece)
        if min_x < 0:
            return True

        max_x = Tech.get_piece_max_x(piece)
        if max_x > Settings.horizontal_blocks_amount-1:
            return True

        max_y = Tech.get_piece_max_y(piece)
        if max_y > Settings.vertical_blocks_amount-1:
            return True
        return False
