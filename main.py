import pygame
from time import time
from stats_board.Board import Board
from game_world.world import World


class App:
    def __init__(self):
        self.running = True
        self.FPS = 60
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Samurai")
        self.Width, self.Height = self.display.get_size()
        self._initialize_()

    def _initialize_(self):
        self.world = World(self.Width, self.Height - 130)
        self.stats_board = Board(self.Width, 130)

    def update(self, dt):
        self.stats_board.update(dt)
        self.world.update(dt, self.stats_board)

    def render(self):
        self.display.fill((10, 10, 10))
        self.world.render(self.display)
        self.stats_board.render(self.display)

    def run(self):
        clock = pygame.time.Clock()
        last_time = time()
        while self.running:
            dt = time() - last_time
            dt *= 60
            last_time = time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    self.FPS = 20
                elif event.type == pygame.KEYUP:
                    self.FPS = 60
            self.update(dt)
            self.render()
            pygame.display.update()
            clock.tick(self.FPS)


if __name__ == "__main__":
    app = App()
    app.run()
    quit()
