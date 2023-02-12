import pygame


class Tech:
    @staticmethod
    def is_mouse_inside_block(block):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (block.screen_pos[0] <= mouse_x <= block.screen_pos[0] + block.screen_pos[2]) and \
                block.screen_pos[1] <= mouse_y <= block.screen_pos[1] + block.screen_pos[3]:
            return True
        return False
