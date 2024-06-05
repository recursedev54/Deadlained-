import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from camera import Camera
from world import World
from entities.player import Player  # Correct import path

# Initialize Pygame
pygame.init()

# Constants
FPS = 48
MOUSE_SENSITIVITY = 0.1

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN)
pygame.display.set_caption("4D Hydrogel Game")
clock = pygame.time.Clock()

# Initialize player, camera, and world
player = Player(x=5, y=5, z=10)
camera = Camera(player=player)
world = World(width=10, height=10)

# OpenGL settings
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (screen.get_width() / screen.get_height()), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Hide mouse cursor and capture it
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# Game loop
running = True
while running:
    delta_time = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            camera.handle_mouse(event.rel[0], event.rel[1])
    
    # Update player
    player.update(delta_time)

    # Render
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(
        player.position.x, player.position.y, player.position.z,
        player.position.x + camera.get_front()[0], player.position.y + camera.get_front()[1], player.position.z + camera.get_front()[2],
        0, 1, 0
    )

    world.draw()

    # Display update
    pygame.display.flip()

pygame.quit()
sys.exit()
