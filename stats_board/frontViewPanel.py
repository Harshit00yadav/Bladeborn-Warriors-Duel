from pygame import Surface
from pygame.draw import circle, line
from pygame import mouse
from pygame.math import Vector2


class FVP:
    def __init__(self):
        self.surface = Surface((100, 100))
        self.cursor = Vector2(50, 50)
        self.mouse = Vector2(50, 50)
        self.cursor_weight = 0.15
        mouse.set_visible(False)

    def update(self, dt):
        self.mouse += Vector2(mouse.get_rel()) * self.cursor_weight
        if self.mouse.x < 0:
            self.mouse.x = 0
        elif self.mouse.x > self.surface.get_width():
            self.mouse.x = self.surface.get_width()
        if self.mouse.y < 0:
            self.mouse.y = 0
        elif self.mouse.y > self.surface.get_height():
            self.mouse.y = self.surface.get_height()

    def update_cursor(self, dt):
        self.cursor += ((self.mouse - self.cursor) / 8) * dt
        if (self.mouse - self.cursor).magnitude() < 10:
            return False
        return True

    def get_cursor(self):
        return self.cursor

    def render(self, display):
        width, height = display.get_size()
        self.surface.fill((0, 0, 0))
        line(self.surface, (200, 200, 10), (0, 73), (100, 73), 1)
        circle(self.surface, (100, 100, 100), self.mouse, 5, 1)
        circle(self.surface, (100, 0, 0), self.cursor, 3)
        display.blit(self.surface, (width // 2 - self.surface.get_width() // 2, height - 110))
