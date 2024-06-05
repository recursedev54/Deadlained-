from OpenGL.GL import *
from entities.blawg import Blawg

class World:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(height)] for _ in range(width)]
        self.init_blawgs()

    def init_blawgs(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x + y) % 2 == 0:  # Add Blawg at alternate positions for example
                    self.grid[x][y] = Blawg(x, 0, y)

    def draw(self):
        glColor3f(1, 0, 0)  # Set color for Blawg outlines
        glBegin(GL_LINES)
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] is not None:
                    self.draw_outline(x, y)
        glEnd()

    def draw_outline(self, x, y):
        if x > 0 and self.grid[x - 1][y] is None:
            glVertex3f(x, 0, y)
            glVertex3f(x, 1, y)
        if x < self.width - 1 and self.grid[x + 1][y] is None:
            glVertex3f(x + 1, 0, y)
            glVertex3f(x + 1, 1, y)
        if y > 0 and self.grid[x][y - 1] is None:
            glVertex3f(x, 0, y)
            glVertex3f(x, 0, y + 1)
        if y < self.height - 1 and self.grid[x][y + 1] is None:
            glVertex3f(x, 0, y + 1)
            glVertex3f(x, 1, y + 1)

    def update(self):
        pass  # Placeholder for future updates
