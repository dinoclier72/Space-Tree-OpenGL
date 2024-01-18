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
from math import cos,sin

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

def draw_star(inner_radius, outter_radius):
    Points = []
    for i in range(18,360,36):
        angle = i*3.14/180
        if(len(Points)%2 == 0):
            radius = outter_radius
        else:
            radius = inner_radius
        Points.append([radius*cos(angle),radius*sin(angle)])
    #2d base
    glBegin(GL_TRIANGLES)
    for i in range(1,len(Points),2):
        processedPoints = []
        if(i+2 >= len(Points)): 
            processedPoints.append(Points[0])
            processedPoints.append(Points[1])
            processedPoints.append(Points[i])
        else:
            processedPoints.append(Points[i])
            processedPoints.append(Points[i+1])
            processedPoints.append(Points[i+2])
        glVertex3f(processedPoints[0][0],0,processedPoints[0][1])
        glVertex3f(processedPoints[1][0],0,processedPoints[1][1])
        glVertex3f(processedPoints[2][0],0,processedPoints[2][1])
    glEnd()
    glBegin(GL_POLYGON)
    for i in range(1,len(Points),2):
        glVertex3f(Points[i][0],0,Points[i][1])
    glEnd()

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
    glTranslatef(0.0, 0.0, 0.25)
    draw_star(0.25,0.5)
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

def draw_color_light_ball(light_id,position,color,size):
    glPushMatrix()
    
    glLightfv(light_id, GL_POSITION, position)
    glLightfv(light_id, GL_DIFFUSE, color)

    glColor3f(*color)
    glTranslatef(*position)
    sphere = gluNewQuadric()
    gluSphere(sphere,size,50,50)

    glPopMatrix()

def get_ball_position(angle, radius, axis, center=[0, 0, 0]):
    if axis == "x":
        return [center[0] + radius * cos(angle), center[1] + radius * sin(angle), center[2]]
    elif axis == "y":
        return [center[0], center[1] + radius * cos(angle), center[2] + radius * sin(angle)]
    elif axis == "z":
        return [center[0] + radius * cos(angle), center[1], center[2] + radius * sin(angle)]

def orbit_ball(angle, radius, axis,center,light_id,color,size):
    angle = angle*3.14/180
    position = get_ball_position(angle, radius,axis,center)
    draw_color_light_ball(light_id,position,color,size)

def set_material_properties():
    glMaterialfv(GL_FRONT, GL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE, GLfloat_4(0.0, 0.0, 0.0, 1.0))  # Set diffuse color to black
    glMaterialfv(GL_FRONT, GL_SPECULAR, GLfloat_4(1.0, 1.0, 1.0, 1.0))  # Set specular color to white
    glMaterialfv(GL_FRONT, GL_SHININESS, GLfloat(100.0))  # Increase shininess for high reflection

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | GLUT_DEPTH)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    gluLookAt(0,15,5,
            0, 0, 4,
            0, 0, 1)

    files = ["textures/brick.jpg",
             "textures/wood.jpg",
             "textures/leaves.jpg",
             "textures/present_blue.jpg",
             "textures/present_yellow.jpg",
             "textures/present_green.jpg"]
    texture_id = [load_texture(f) for f in files]

    camera_angle = 0.0
    camera_height = 5.0
    ball1_angle = 60.0
    ball2_angle = 120.0
    ball3_angle = 180.0

    ball1_velocity = 0.66
    ball2_velocity = 1
    ball3_velocity = 1.33

    lights_enabled = [True, True, True]

    while True:
        delta_camera_angle = 0.0
        delta_camera_height = 0.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RIGHT]):
            delta_camera_angle += 0.1
        elif(keys[pygame.K_LEFT]):
            delta_camera_angle += -0.1
        elif(keys[pygame.K_UP]):
            delta_camera_height += 1.0
        elif(keys[pygame.K_DOWN]):
            delta_camera_height += -1.0
        elif(keys[pygame.K_1]):
            lights_enabled[0] = not lights_enabled[0]
        elif(keys[pygame.K_2]):
            lights_enabled[1] = not lights_enabled[1]
        elif(keys[pygame.K_3]):
            lights_enabled[2] = not lights_enabled[2]
        

        camera_angle += delta_camera_angle
        camera_height += delta_camera_height

        glLoadIdentity()
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        gluLookAt(15*sin(camera_angle), 15*cos(camera_angle), camera_height,
              0, 0, 4,
              0, 0, 1)
        
        delta_camera_angle = 0
        delta_camera_height = 0

        ball1_angle = ((ball1_angle + ball1_velocity) % 360)
        ball2_angle = ((ball2_angle + ball2_velocity) % 360)
        ball3_angle = ((ball3_angle + ball3_velocity) % 360)

        glClearColor(0.5,0.5,0.5,1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glEnable(GL_LIGHTING)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, GLfloat_4(0.2, 0.2, 0.2, 1.0))

        if lights_enabled[0]:
            glEnable(GL_LIGHT0)
        else:
            glDisable(GL_LIGHT0)
        if lights_enabled[1]:
            glEnable(GL_LIGHT1)
        else:
            glDisable(GL_LIGHT1)
        if lights_enabled[2]:
            glEnable(GL_LIGHT2)
        else:
            glDisable(GL_LIGHT2)

        #set_material_properties()
        orbit_ball(ball1_angle, 6, "y",[0,0,4],GL_LIGHT0,[1.0,.0,.0],0.3)
        orbit_ball(ball2_angle, 6, "x",[0,0,4],GL_LIGHT1,[.0,1.0,.0],0.3)
        orbit_ball(ball3_angle, 6, "z",[0,0,4],GL_LIGHT2,[.0,.0,1.0],0.3)

        draw_textured_cylinder(top_texture_id=texture_id[0], bottom_texture_id=texture_id[0], side_texture_id=texture_id[0], radius=4.0, height=1.0)
        draw_christmas_tree(trunk_texture_id=texture_id[1], leaves_texture_id=texture_id[2])
        draw_christmas_present(texture_id[3],0.33,2.5,5,3)
        draw_christmas_present(texture_id[4],0.5,-2.5,5,2)
        draw_christmas_present(texture_id[5],0.66,0,-3,1.50)
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()