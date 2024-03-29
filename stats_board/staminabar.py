from pygame import Surface
from pygame.draw import polygon


class StaminaBar:
    def __init__(self, x, y):
        self.stamina = 100
        self.x, self.y = x, y
        self.staminaBar = Surface((100, 10))

    def render(self, display):
        self.staminaBar.fill((15, 15, 15))
        polygon(self.staminaBar, (255, 200, 200), [(15, 10), (25, 0), (40, 0), (45, 5), (100, 5), (100, 10)])
        polygon(self.staminaBar, (255, 200, 200), [(0, 10), (10, 0), (20, 0), (10, 10)])
        display.blit(self.staminaBar, (self.x, self.y))
