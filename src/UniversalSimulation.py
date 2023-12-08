from OpenGL.GL import *
from OpenGL.GLU import *
from Star import Star
import numpy as np
import random
import pygame
import time


class Universal_simulation:
    def __init__(self, 
                star_count = 200, 
                x_range = (-800, 800),
                y_range = (-500, 500), 
                z_range = (-500, 500), 
                size_range = (0.1, 2.0)):

        self.WINDOW_SIZE = (1400, 750)
        self.perspective = np.identity(4)
        self.stars = []

        x_min, x_max = x_range
        y_min, y_max = y_range
        z_min, z_max = z_range
        size_min, size_max = size_range

        for i in range(star_count):
            new_star = Star(
                random.uniform(x_min, x_max),
                random.uniform(y_min, y_max),
                random.uniform(z_min, z_max),
                random.uniform(size_min, size_max)
            )
            self.stars.append(new_star)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.WINDOW_SIZE, pygame.OPENGL | pygame.DOUBLEBUF)
        self.init()
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            for star in self.stars:
                self.draw(star)
            
            self.update_stars_size()
            self.handle_keys()

            pygame.display.flip()
            clock.tick(60)
    
    def update_stars_size(self):
        for star in self.stars:
            star.update_size()

    def init(self):
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.WINDOW_SIZE[0] / self.WINDOW_SIZE[1]), 0.1, 2000.0)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.perspective[3][2] += 5
        elif keys[pygame.K_DOWN]:
            self.perspective[3][2] -= 5
        
        elif keys[pygame.K_LEFT]:
            angle = np.radians(1)
            rotation = np.array([
                [np.cos(angle), 0, np.sin(angle), 0],
                [0, 1, 0, 0],
                [-np.sin(angle), 0, np.cos(angle), 0],
                [0, 0, 0, 1]
            ])
            self.perspective = np.dot(rotation, self.perspective)
        elif keys[pygame.K_RIGHT]:
            angle = np.radians(-1)
            rotation = np.array([
                [np.cos(angle), 0, np.sin(angle), 0],
                [0, 1, 0, 0],
                [-np.sin(angle), 0, np.cos(angle), 0],
                [0, 0, 0, 1]
            ])
            self.perspective = np.dot(rotation, self.perspective)

        elif keys[pygame.K_w]:
            self.perspective[3][1] -= 5
        elif keys[pygame.K_s]:
            self.perspective[3][1] += 5
        elif keys[pygame.K_d]:
            self.perspective[3][0] -= 5
        elif keys[pygame.K_a]:
            self.perspective[3][0] += 5


    def draw(self, star):
        glLoadIdentity()
        glMultMatrixf(self.perspective)
        glPushMatrix()
        glTranslatef(star.x, star.y, star.z)

        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, [1.0, 1.0, 0.0, 1.0]) 

        quadric = gluNewQuadric()
        gluSphere(quadric, star.size, 32, 32)
        gluDeleteQuadric(quadric)
        glPopMatrix()

