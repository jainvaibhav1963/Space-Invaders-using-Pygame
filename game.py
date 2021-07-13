# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:00:15 2021

@author: jain
"""

import pygame
import random

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
enemy_img = pygame.image.load('enemy_1.png')
enemy_x = random.randint(0,800)
enemy_y = random.randint(0,200)
enemy_x_change = 0.2
enemy_y_change = 40
#############################
#############################
def player(x,y):
    screen.blit(player_ship_img,(player_ship_x,player_ship_y))  
  
def enemy(x,y):
    screen.blit(enemy_img,(enemy_x,enemy_y))  

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                # print('Move key released')
                player_ship_x_change = 0
                
##########################################
    player_ship_x += player_ship_x_change
    
    # bounderies
    if player_ship_x >= 742:
        player_ship_x = 0
    elif player_ship_x <= 0:
        player_ship_x = 742

    enemy_x += enemy_x_change
    
    # bounderies
    if enemy_x >= 742:
        enemy_x_change = -enemy_x_change
        enemy_y += enemy_y_change
    elif enemy_x <= 0:
        enemy_x_change = -enemy_x_change
        enemy_y += enemy_y_change
##########################################    
    # spawns player ship to given co-cordinates
    player(player_ship_x,player_ship_y)
    enemy(enemy_x,enemy_y)
    pygame.display.update()
    
    
    
    
    
    
    
pygame.quit()    