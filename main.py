import numpy as np
import pygame
from colors import *
from settings import *


class FractalFern:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.x_off = X_OFF
        self.y_off = Y_OFF
        self.game_win_width = GAMEWIN_WIDTH
        self.game_win_height = GAMEWIN_HEIGHT
        self.fps = FPS
        self.clock = None
        self.win = None
        self.game_win = None
        self.title_font = None
        self.is_paused = True

    def win_init(self):
        pygame.init()
        pygame.font.init()

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Barnsley Fern')

        game_win_rect = pygame.Rect(self.x_off, self.y_off, self.game_win_width, self.game_win_height)
        self.game_win = self.win.subsurface(game_win_rect)

        self.win.fill(MID_BLACK)
        self.game_win.fill(BLACK)

        self.title_font = pygame.font.SysFont(TITLE_FONT, FONT_SIZE)
        title = self.title_font.render(TITLE, 1, GOLD)
        w, h = title.get_size()
        blit_X = (self.width - w) // 2
        blit_Y = (self.y_off - h) // 2
        self.win.blit(title, (blit_X, blit_Y))

        self.clock = pygame.time.Clock()
        pygame.display.update()

    @staticmethod
    def close():
        pygame.font.quit()
        pygame.quit()

    def draw(self):
        pass

    def run(self):
        if not pygame.display.init():
            self.win_init()

        run = True
        while run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        self.is_paused = not self.is_paused

                    if keys[pygame.K_ESCAPE]:
                        pass

        FractalFern.close()


if __name__ == '__main__':
    fractal = FractalFern()
    fractal.run()

