from game_world.ragdoll.verlet import Verlet
from game_world.ragdoll.constrain import Constrain
from pygame.math import Vector2
from pygame.draw import line


class Player:
    def __init__(self, px, py):
        self.x = px
        self.y = py
        self.f_arm_nodes = [
                Verlet(self.x, self.y - 100),
                Verlet(self.x, self.y - 70),
                Verlet(self.x, self.y - 40)
            ]
        self.b_arm_nodes = [
                Verlet(self.x, self.y - 100),
                Verlet(self.x, self.y - 70),
                Verlet(self.x, self.y - 40)
                ]
        self.constrains = [
                Constrain(20, self.f_arm_nodes[0], self.f_arm_nodes[1], 0),
                Constrain(20, self.f_arm_nodes[1], self.f_arm_nodes[2], 1),
                Constrain(20, self.b_arm_nodes[0], self.b_arm_nodes[1], 0),
                Constrain(20, self.b_arm_nodes[1], self.b_arm_nodes[2], 1)
            ]

    def equipe(self, wep):
        handle = wep.get_handle_cords()
        shoulders = wep.get_shoulders_cords()
        self.f_arm_nodes[0].add_forces(
            (shoulders[0] - self.f_arm_nodes[0].pos) / 2
        )
        self.f_arm_nodes[-1].add_forces(
            (handle[0] - self.f_arm_nodes[-1].pos) / 2
        )
        self.b_arm_nodes[0].add_forces(
            (shoulders[1] - self.b_arm_nodes[0].pos) / 2
        )
        self.b_arm_nodes[-1].add_forces(
            (handle[1] - self.b_arm_nodes[-1].pos) / 2
        )

    def update_constrain(self):
        for c in self.constrains:
            c.solve()

    def update(self, dt, wep):
        for n in self.f_arm_nodes:
            n.add_forces(Vector2(0, 0.98))
        for n in self.b_arm_nodes:
            n.add_forces(Vector2(0, 0.98))

        self.equipe(wep)
        self.update_constrain()

        for n in self.f_arm_nodes:
            n.update(dt)
        for n in self.b_arm_nodes:
            n.update(dt)

    def render(self, display):
        for n in self.f_arm_nodes:
            n.render(display)
        for n in self.b_arm_nodes:
            n.render(display)

        for c in self.constrains:
            line(display, (100, 100, 100), c.n1.pos, c.n2.pos, 2)
