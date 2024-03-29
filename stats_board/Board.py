from pygame import Surface
from pygame import mouse
from stats_board.staminabar import StaminaBar
from stats_board.frontViewPanel import FVP


class Board:
    def __init__(self, width, height):
        self.surface = Surface((width, height))
        self.width = width
        self.height = height
        self.attack = False
        self._initialize_()

    def _initialize_(self):
        self.stamina_bar = StaminaBar(self.width // 2 - 50, 5)
        self.frontview = FVP()

    def update(self, dt):
        mouse_buttons = mouse.get_pressed()
        self.attack = self.frontview.update_cursor(dt)
        self.frontview.update(dt)

    def render(self, display):
        self.surface.fill((15, 15, 15))

        self.stamina_bar.render(self.surface)
        self.frontview.render(self.surface)

        display.blit(self.surface, (0, display.get_height() - self.height))
