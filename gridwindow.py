# -*- coding: utf-8 -*-
import framework
from color import Color
import sys

class GridWindow(object):
    def __init__(self, screen, position, grid_size):
        self._position = position
        self._grid_size = grid_size
        self._screen = screen

    def write(self, pos, string, color):
        self._screen.write(self._convert_pos(pos), string, color)

    def _convert_pos(self, pos):
        (px, py), (x, y), (w, h) = self._position, pos, self._grid_size
        return (px + x * w, py + y * h)

if __name__ == '__main__':
    class GridWindowDemo(framework.Application):
        POSITION = (0, 0)
        GRID_SIZE = (10, 18)
        LEFT  = (-1, 0)
        DOWN  = ( 0, 1)
        UP    = (0, -1)
        RIGHT = (1,  0)
        def __init__(self):
            framework.Application.__init__(self)
            self._window = None
            self._character_pos = (1, 1)

        def update(self):
            down_keys =  self._keyboard.down_keys()
            if not down_keys: return
            key = down_keys[0]
            if key == ord('h'): self._move(self.LEFT)
            if key == ord('j'): self._move(self.DOWN)
            if key == ord('k'): self._move(self.UP)
            if key == ord('l'): self._move(self.RIGHT)
            if key == ord('q'): sys.exit()

        def _move(self, direction):
            (x, y), (dx, dy) = self._character_pos, direction
            self._character_pos = (x+dx, y+dy)

        def set_screen(self, screen):
            self._screen = screen
            self._window = GridWindow(screen, self.POSITION, self.GRID_SIZE)

        def draw(self):
            self._screen.fill()
            self._window.write(self._character_pos, '@', Color.LIME)

    framework.GameRunner(GridWindowDemo())\
        .initialize_system()\
        .initialize_screen(640, 480, 16)\
        .set_fps(30)\
        .set_font('Courier New', 18)\
        .set_caption('KeyConfig')\
        .run()
