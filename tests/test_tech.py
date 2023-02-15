import unittest

from classes.blocks import MapBlock, Side
from classes.colors import Colors
from utils.tech_utils import Tech


class MyTestCase(unittest.TestCase):
    piece = [
        MapBlock(x=4, y=-3, color=Colors.white),
        MapBlock(x=4, y=-2, color=Colors.white),
        MapBlock(x=4, y=-1, color=Colors.white),
        MapBlock(x=4, y=0, color=Colors.white),
        MapBlock(x=3, y=-3, color=Colors.white),
        MapBlock(x=2, y=-3, color=Colors.white)
    ]

    obstacles = [
        MapBlock(x=5, y=-3, color=Colors.black),
        MapBlock(x=1, y=-3, color=Colors.black),
        MapBlock(x=4, y=5, color=Colors.black)
    ]

    def test_get_piece_max_y_success(self):
        max_y = Tech.get_piece_max_y(piece=self.piece)
        self.assertEqual(max_y, 0)

    def test_get_piece_max_y_fail(self):
        max_y = Tech.get_piece_max_y(piece=self.piece)
        self.assertNotEqual(max_y, -3)

    def test_get_piece_min_x_success(self):
        min_x = Tech.get_piece_min_x(piece=self.piece)
        self.assertEqual(min_x, 2)

    def test_get_piece_min_x_fail(self):
        min_x = Tech.get_piece_min_x(piece=self.piece)
        self.assertNotEqual(min_x, 4)

    def test_get_piece_max_x_success(self):
        max_x = Tech.get_piece_max_x(piece=self.piece)
        self.assertEqual(max_x, 4)

    def test_get_piece_max_x_fail(self):
        max_x = Tech.get_piece_max_x(piece=self.piece)
        self.assertNotEqual(max_x, 2)

    def test_piece_blocks_visible_from_bottom_success(self):
        pieces_visible = Tech.piece_blocks_visible_from(self.piece, Side.BOTTOM)
        self.assertEqual([
            MapBlock(x=4, y=0, color=Colors.white),
            MapBlock(x=3, y=-3, color=Colors.white),
            MapBlock(x=2, y=-3, color=Colors.white)],
            pieces_visible)

    def test_piece_blocks_visible_from_left_success(self):
        pieces_visible = Tech.piece_blocks_visible_from(self.piece, Side.LEFT)
        self.assertEqual([
            MapBlock(x=4, y=-2, color=Colors.white),
            MapBlock(x=4, y=-1, color=Colors.white),
            MapBlock(x=4, y=0, color=Colors.white),
            MapBlock(x=2, y=-3, color=Colors.white)],
            pieces_visible)

    def test_piece_blocks_visible_from_right_success(self):
        pieces_visible = Tech.piece_blocks_visible_from(self.piece, Side.RIGHT)
        self.assertEqual([
            MapBlock(x=4, y=-3, color=Colors.white),
            MapBlock(x=4, y=-2, color=Colors.white),
            MapBlock(x=4, y=-1, color=Colors.white),
            MapBlock(x=4, y=0, color=Colors.white)],
            pieces_visible)

    def test_is_there_block_on_the_side_of_piece_bottom_success(self):
        is_block_under = Tech.is_there_block_on_the_side_of_piece(self.piece, Side.BOTTOM, self.obstacles)
        self.assertFalse(is_block_under)

    def test_is_there_block_on_the_side_of_piece_left_success(self):
        is_block_under = Tech.is_there_block_on_the_side_of_piece(self.piece, Side.LEFT, self.obstacles)
        self.assertTrue(is_block_under)

    def test_is_there_block_on_the_side_of_piece_right_success(self):
        is_block_under = Tech.is_there_block_on_the_side_of_piece(self.piece, Side.RIGHT, self.obstacles)
        self.assertTrue(is_block_under)


if __name__ == '__main__':
    unittest.main()
