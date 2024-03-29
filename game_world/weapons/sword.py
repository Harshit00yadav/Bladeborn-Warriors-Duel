from pygame.draw import circle, line
from pygame.math import Vector2
from math import sin, cos, pi


class SwordMovement:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pivot = Vector2(x, y)
        self.DFP = 35  # distance from pivot
        self.sword_length = 70
        self.attack = False
        self.gama_end = 0

    def update(self, cursor, attack):
        theta = (3*pi/2) * (cursor.x/100) - pi/4
        gama = (pi) * (cursor.y/100) - pi/4
        self.attack = attack
        if (attack):
            self.gama_end += (gama - self.gama_end) / 2
            self.DFP += (50 - self.DFP) / 2
            self.sword_length = 100
        else:
            self.gama_end += (gama - pi/4 - self.gama_end) / 5
            self.DFP += (35 - self.DFP) / 2
            self.sword_length = 70
        self.projection_begin = Vector2(
                self.pivot.x + (self.DFP * sin(gama)) * sin(theta),
                self.pivot.y - self.DFP * cos(gama)
                )
        self.projection_end = Vector2(
                self.pivot.x + ((self.DFP + self.sword_length) * sin(self.gama_end)) * sin(theta),
                self.pivot.y - (self.DFP + self.sword_length) * cos(self.gama_end)
                )
        self.depth = int(- 100 * cos(theta))
        self.SF = Vector2(self.pivot.x - 20 * (cursor.x - 50) / 100, self.pivot.y)
        self.SB = Vector2(self.pivot.x + 20 * (cursor.x - 50) / 100, self.pivot.y)

    def render(self, display):
        circle(display, (255, 255, 255), self.pivot, 2)
        circle(display, (0, 0, 255), self.SB, 4)
        circle(display, (255, 0, 0), self.SF, 4)


class Sword(SwordMovement):
    def __init__(self, x, y):
        super().__init__(x, y)

    def get_shoulders_cords(self):
        return (self.SF, self.SB)

    def get_handle_cords(self):
        return (
                self.projection_begin,
                self.projection_begin + (self.projection_end - self.projection_begin) * 2 / 10
                )

    def render(self, display):
        super().render(display)
        line(
                display,
                (155 + self.depth, 155 + self.depth, 155 + self.depth),
                self.projection_begin,
                self.projection_end,
                2
            )
        line(
                display,
                (95, 10, 10),
                self.projection_begin,
                self.projection_begin + (self.projection_end - self.projection_begin) * 2 / 10,
                3
            )
        line(
                display,
                (95, 55, 10),
                self.projection_begin + (self.projection_end - self.projection_begin) * 2 / 10,
                self.projection_begin + (self.projection_end - self.projection_begin) * (2.25) / 10,
                12
            )
