from pygame.math import Vector2
from pygame.draw import circle


class Verlet:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.pre_pos = Vector2(x, y)
        self.acc = Vector2()

    def add_forces(self, force):
        self.acc += force

    def update(self, dt):
        velocity = (self.pos - self.pre_pos)
        self.pre_pos = self.pos
        self.pos += velocity + self.acc * dt * dt
        self.acc = Vector2()

    def render(self, display):
        circle(display, (100, 100, 100), self.pos, 3)
