# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:12:46 2023

@author: User
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rotate_x = 0.0
rotate_y = 0.0

# Load a texture
def load_texture(filename):
    image = pygame.image.load(filename)
    texture_data = pygame.image.tostring(image, "RGBA", 1)
    width, height = image.get_width(), image.get_height()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

    return texture_id

# Draw a textured cylinder
def draw_textured_cylinder(top_texture_id, bottom_texture_id, side_texture_id):
    glu_quad = gluNewQuadric()
    gluQuadricTexture(glu_quad, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, side_texture_id)
    glPushMatrix()
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)
    gluCylinder(glu_quad, 2.0, 2.0, 1.0, 32, 32)
    glTranslatef(0.0, 0.0, 1.0)  # Translate to the top of the cylinder
    glBindTexture(GL_TEXTURE_2D, top_texture_id)
    gluDisk(glu_quad, 0.0, 2.0, 32, 32)  # Draw the top face
    glTranslatef(0.0, 0.0, -1.0)  # Translate to the bottom of the cylinder
    glBindTexture(GL_TEXTURE_2D, bottom_texture_id)
    gluDisk(glu_quad, 0.0, 2.0, 32, 32)  # Draw the bottom face
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

# Draw a textured cube
def draw_textured_cube(texture_id1,texture_id2,texture_id3,texture_id4,texture_id5,texture_id6):
    glPushMatrix()
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)
    # Load texture
    glBindTexture(GL_TEXTURE_2D, texture_id1)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, -1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, -1)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_id2)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_id3)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, -1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, -1, 1)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_id4)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, 1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 1)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_id5)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(-1, 1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(-1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(-1, -1, 1)
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture_id6)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3f(1, -1, -1)
    glTexCoord2f(1, 0)
    glVertex3f(1, 1, -1)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex3f(1, -1, 1)
    glEnd()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | GLUT_DEPTH)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    gluLookAt(0, 10, 5,
              0, 0, 0, 
              0, 0, 1)  # Add this line
    glTranslatef(0.0, 0.0, 0.0)

    files = ["textures/brick_texture.jpg","textures/wood.jpg"]
    texture_id = [load_texture(f) for f in files]

    while True:
        global rotate_x, rotate_y
        x, y = 0, 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.rel
            #rotate_x += x
            #rotate_y += y

        #glRotatef(1, 3, 2, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the textured cube
        # Draw the textured cylinder
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        draw_textured_cylinder(top_texture_id=texture_id[0], bottom_texture_id=texture_id[0], side_texture_id=texture_id[1])
        glDisable(GL_TEXTURE_2D)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()



