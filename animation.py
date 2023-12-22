#muhammed siyad p

from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 
import playsound
from math import *
import time
import random
import threading

hx = 0  # max600
hy = 0
left_leg_x = 0
restricted_area_for_rain = [0+50,100+80,200,435]

def doanimation():
    glClear(GL_COLOR_BUFFER_BIT)
    
    #floor
    glColor3f(223/255, 129/255, 21/255)
    glLineWidth(9)
    glBegin(GL_LINES)
    glVertex2f(00,200)
    glVertex2f(800,200)
    glEnd()
    
    #mountains
    glColor3f(63/255, 181/255, 97/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(100,200)
    glVertex2f(600,200)
    glVertex2f(300,600)
    glEnd()
    glColor3f(255/255, 250/255, 255/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(250,500)
    glVertex2f(375,500)
    glVertex2f(300,600)
    glEnd()
    
    glColor3f(63/255, 220/255, 97/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(100-300,200)
    glVertex2f(600-300,200)
    glVertex2f(300-300,600)
    glEnd()
    glColor3f(255/255, 250/255, 255/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(250-300,500)
    glVertex2f(375-300,500)
    glVertex2f(300-300,600)
    glEnd()
    
    #clouds
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(79/255, 198/255, 240/255)
    for i in range(0,360,1):
        glVertex2f(700+70*cos(pi*i/180),650+40*sin(pi*i/180))
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        glVertex2f(780+70*cos(pi*i/180),650+40*sin(pi*i/180))
    glEnd()
    
    
    #left leg
    glColor3f(161/255, 133/255, 8/255)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(hx+50+left_leg_x,200)
    glVertex2f(hx+80,270)
    glEnd()
    
    #right leg
    #glColor3f(0/255, 200/255, 0/255)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(hx+110-left_leg_x,200)
    glVertex2f(hx+80,270)
    glEnd()
    
    #body 
    #glColor3f(0/255, 200/255, 0/255)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(hx+80,340+hy)
    glVertex2f(hx+80,250+hy)
    glEnd()
    
    #hands
    #glColor3f(0/255, 200/255, 0/255)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(hx+80,315+hy)
    glVertex2f(hx+100,290+hy)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(hx+80,315+hy)
    glVertex2f(hx+100,280+hy)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(hx+120,315+hy)
    glVertex2f(hx+100,290+hy)
    glEnd()
    
    glBegin(GL_LINES)
    glVertex2f(hx+120,315+hy)
    glVertex2f(hx+100,280+hy)
    glEnd()
    
    #head
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        glVertex2f(hx+80+18*cos(pi*i/180),360+hy+25*sin(pi*i/180))
    glEnd()
    
    #umbrella handle
    glColor3f(240/255, 26/255, 69/255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(hx+120,400+hy)
    glVertex2f(hx+120,285+hy)
    glEnd()
    
    
    #umbrella
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,180,1):
        glVertex2f(hx+120+70*cos(pi*i/180),400+hy+35*sin(pi*i/180))
    glEnd()
    
    #rain
    glColor3f(3/255, 252/255, 244/255)
    glLineWidth(1)
    glBegin(GL_LINES)
    
    for j in range(80):
        if (not((rain_cordinates_x[j] > restricted_area_for_rain[0] and rain_cordinates_x[j] < restricted_area_for_rain [1]) and (rain_cordinates_y[j] > restricted_area_for_rain[2] and rain_cordinates_y[j] < restricted_area_for_rain [3]))):
            glVertex2f(rain_cordinates_x[j],rain_cordinates_y[j])
            glVertex2f(rain_cordinates_x[j],rain_cordinates_y[j]+10)
    
    
    
    glEnd()
    
    
    


def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    doanimation()
    glFlush()



glutInit()

def a():
    playsound.playsound('rain.wav')
    playsound.playsound('rain.wav')
    playsound.playsound('rain.wav')
t1 = threading.Thread(target=a, args=())
t1.start()

glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800,800)
glutInitWindowPosition(0,0)
wind = glutCreateWindow("Animation by Muhammed siyad")
gluOrtho2D(0,800,0,800)
glutDisplayFunc(showscreen)
rain_cordinates_x = []
rain_cordinates_y = []
for j in range(100):
    rain_cordinates_x.append(random.randint(0, 800))
    rain_cordinates_y.append(random.randint(200, 800))

while (1):
    for i in range (0,600):
        hx  = i
        hy += .3
        if (hy >10):
            hy = 0;
        restricted_area_for_rain[0] +=1
        restricted_area_for_rain[1] +=1
        left_leg_x +=1
        if (left_leg_x >= 60):
            left_leg_x = 0
        showscreen()
        rain_cordinates_x = []
        rain_cordinates_y = []
        for j in range(80):
            rain_cordinates_x.append(random.randint(0, 800))
            rain_cordinates_y.append(random.randint(200, 800))
        time.sleep(.03)
    hy = 0
    for i in range (600,0,-1):
        hx  = i
        restricted_area_for_rain[0] -=1
        restricted_area_for_rain[1] -=1
        left_leg_x +=1
        if (left_leg_x >= 60):
            left_leg_x = 0
        showscreen()
        rain_cordinates_x = []
        rain_cordinates_y = []
        for j in range(80):
            rain_cordinates_x.append(random.randint(0, 800))
            rain_cordinates_y.append(random.randint(200, 800))
        time.sleep(.03)
glutMainLoop()

