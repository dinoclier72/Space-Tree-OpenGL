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
def draw_textured_cylinder(top_texture_id, bottom_texture_id, side_texture_id, radius=2.0, height=1.0):
    glu_quad = gluNewQuadric()
    gluQuadricTexture(glu_quad, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, side_texture_id)
    glPushMatrix()
    gluCylinder(glu_quad, radius, radius, height, 32, 32)
    glTranslatef(0.0, 0.0, height)  # Translate to the top of the cylinder
    glBindTexture(GL_TEXTURE_2D, top_texture_id)
    gluDisk(glu_quad, 0.0, radius, 32, 32)  # Draw the top face
    glTranslatef(0.0, 0.0, -height)  # Translate to the bottom of the cylinder
    glBindTexture(GL_TEXTURE_2D, bottom_texture_id)
    gluDisk(glu_quad, 0.0, radius, 32, 32)  # Draw the bottom face
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def draw_christmas_tree(trunk_texture_id, leaves_texture_id):
    treeLayer = 5
    treeHeight = 1.0
    trunk_radius = 0.5
    trunk_height = 2.0
    tree = gluNewQuadric()
    gluQuadricTexture(tree, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, trunk_texture_id)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 1.0)
    gluCylinder(tree, trunk_radius, trunk_radius, trunk_height, 32, 32)
    glTranslatef(0.0, 0.0, trunk_height)
    glBindTexture(GL_TEXTURE_2D, leaves_texture_id)
    for layer in range(treeLayer):
        outter_radius = trunk_radius
        if(layer == treeLayer-1):
            outter_radius = 0.0
        gluCylinder(tree, trunk_radius*(treeLayer-layer), outter_radius, treeHeight, 32, 32)
        gluDisk(tree, 0.0, trunk_radius*(treeLayer-layer), 32, 32)
        glTranslatef(0.0, 0.0, treeHeight)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

# Draw a textured cube
def draw_textured_cube(texture_id1,texture_id2,texture_id3,texture_id4,texture_id5,texture_id6):
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

def draw_christmas_present(texture, size,x,y,z):
    glPushMatrix()
    glScalef(size,size,size)
    glTranslatef(x,y,z+1)
    glEnable(GL_TEXTURE_2D)
    draw_textured_cube(texture,texture,texture,texture,texture,texture)
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | GLUT_DEPTH)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    gluLookAt(0, 15, 5,
              0, 0, 4, 
              0, 0, 1)  # Add this line

    files = ["textures/brick.jpg",
             "textures/wood.jpg",
             "textures/leaves.jpg",
             "textures/present_blue.jpg",
             "textures/present_yellow.jpg",
             "textures/present_green.jpg"]
    texture_id = [load_texture(f) for f in files]

    camera_angle = 0.0
    camera_height = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RIGHT]):
            camera_angle += 1.0
        elif(keys[pygame.K_LEFT]):
            camera_angle += -1.0
        elif(keys[pygame.K_UP]):
            camera_height += 1.0
        elif(keys[pygame.K_DOWN]):
            camera_height += -1.0

        glRotatef(camera_angle, 0, 0, 1)
        glTranslatef(0, 0, camera_height)
        camera_angle = 0
        camera_height = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the textured cube
        # Draw the textured cylinder
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        draw_textured_cylinder(top_texture_id=texture_id[0], bottom_texture_id=texture_id[0], side_texture_id=texture_id[0], radius=4.0, height=1.0)
        draw_christmas_tree(trunk_texture_id=texture_id[1], leaves_texture_id=texture_id[2])
        draw_christmas_present(texture_id[3],0.33,2.5,5,3)
        draw_christmas_present(texture_id[4],0.5,-2.5,5,2)
        draw_christmas_present(texture_id[5],0.66,0,-3,1.66)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()



