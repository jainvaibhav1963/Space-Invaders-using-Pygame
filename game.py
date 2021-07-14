# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:00:15 2021

@author: jain
"""

import pygame
import random
import math

# initailise pygame
pygame.init()

# create a window
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption('Horny Invaders')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
#############################
#############################
# Player ship
player_ship_img = pygame.image.load('player_ship.png')
player_ship_x = 368
player_ship_y = 500
player_ship_x_change = 0
# Enemy ship
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 10
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy_1.png'))
    enemy_x.append(random.randint(0,800))
    enemy_y.append(random.randint(0,200))
    enemy_x_change.append(0.1)
    enemy_y_change.append(30)
# Laser
laser_img = pygame.image.load('laser.png')
laser_x = 0
laser_y = 500
laser_x_change = 0
laser_y_change = -.5
laser_state = False  #false state - laser not fired
# Score
score = 0
#############################
#############################
def player(x,y):
    screen.blit(player_ship_img,(player_ship_x,player_ship_y))  
  
def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))  

def fire_laser(x,y):
    # global laser_state
    # laser_state = True
    screen.blit(laser_img,(x+16,y-20))
    
def isCollision(laser_x,laser_y,enemy_x,enemy_y):
    distance = math.sqrt(((laser_x-enemy_x)**2)+((laser_y-enemy_y)**2))
    if distance < 32:
        return True
#############################
#############################
# Game loop
running = True
while running:
    
    # window background
    dark_pink = (230,10,140)        
    screen.fill(dark_pink)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # keybord keystrike check
        if event.type == pygame.KEYDOWN:
            # print('Key pressed')
            if event.key == pygame.K_a:
                # print('left move key pressed')
                player_ship_x_change = -.5
            if event.key == pygame.K_d:
                # print('right move key pressed')
                player_ship_x_change = .5
            if event.key == pygame.K_SPACE and laser_state == False:
                # fire_laser(player_ship_x,laser_y)
                laser_x = player_ship_x
                laser_state = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                # print('Move key released')
                player_ship_x_change = 0
                
##########################################
    player_ship_x += player_ship_x_change
    
    # bounderies player
    if player_ship_x >= 742:
        player_ship_x = 0
    elif player_ship_x <= 0:
        player_ship_x = 742


    
    # enemy movement
    for i in range(num_of_enemies):
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] >= 742:
            enemy_x_change[i] = -enemy_x_change[i]
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] < 0:
            enemy_x_change[i] = -enemy_x_change[i]
            enemy_y[i] += enemy_y_change[i]
            
    # collision
        collision = isCollision(laser_x,laser_y,enemy_x[i],enemy_y[i])
        if collision:
            laser_y = 500
            laser_state = False
            score += 1
            enemy_x[i] = 0
            enemy_y[i] = 0
        
        enemy(enemy_x[i],enemy_y[i],i)
        
    # laser movement
    if laser_y <= 0:  #laser resets after leaving top of screen
        laser_y = player_ship_y - 20
        laser_state = False
        
    if laser_state == True:
        fire_laser(laser_x,laser_y)
        laser_y += laser_y_change
        

  
    # spawns player ship to given co-cordinates
    player(player_ship_x,player_ship_y)

    pygame.display.update()
    
    
    
    
    
    
    
pygame.quit()    
