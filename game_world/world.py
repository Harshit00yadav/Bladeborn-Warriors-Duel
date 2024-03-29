from game_world.weapons.sword import Sword
from game_world.ragdoll.player import Player


class World:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
        self.weapon = Sword(self.Width//2, self.Height//2)
        self.player = Player(self.Width//2, self.Height//2 + 100)

    def update(self, dt, stats_board):
        self.weapon.update(stats_board.frontview.get_cursor(), stats_board.attack)
        self.player.update(dt, self.weapon)

    def render(self, display):
        self.weapon.render(display)
        self.player.render(display)
