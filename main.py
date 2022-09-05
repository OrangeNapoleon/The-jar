#!/usr/bin/env python3

import pygame
from pygame.locals import *
import random
import pytomlpp

pygame.init()
pygame.font.init()

data = pytomlpp.load('config.toml')

swidth = data['video']['screen']['width']
sheight = data['video']['screen']['height']

clock = pygame.time.Clock()

screen = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption("The jar")

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

FPS = 60

x_change = 0

player = pygame.Rect(swidth/2, sheight/2, ((swidth/2)/8), ((swidth/2)/8))

enemy_length=random.randint((swidth/4)-player.width, (((swidth/2)-player.width)-player.width/2))
enemy_pos=0
enemy = pygame.Rect((swidth/4)+5, 0, enemy_length, int(sheight/3)/8)
enemy_spd = 1

points = 0
point_gain = False

font = pygame.font.SysFont('MathJax_Typewriter', 30)
text = font.render('Points:\n'+str(points), False, black)

y_change = 0

print(K_RIGHT)

while True:
    clock.tick(FPS)
    
    enemy.y += enemy_spd

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == data['controls']['right']:
                x_change = player.width/5
            if event.key == data['controls']['left']:
                x_change = -(player.width/5)
            if event.key == data['controls']['jump']:
                y_change = 0
                player.y -= (player.width/5)*3
        if event.type == KEYUP:
            if event.key == data['controls']['right'] or event.key == data['controls']['left']:
                x_change = 0

    if player.y >= (sheight/4)*3 or player.x <= (swidth/4) or player.x >= (((swidth/4)*3)-player.width) or player.y <= 0:
        pygame.quit()
        print(f"YOU LOST!\npoints:{points}")
        exit()

    screen.fill(white)

    #screen updates: START
    #enemy bullshit
    if (enemy_pos % 2) == 0:
        enemy.x = ((swidth/4)+5)
        enemy.width = enemy_length
    else:
        enemy.width = enemy_length
        enemy.x = ((swidth/4)+((swidth/2)-enemy_length))
        
    pygame.draw.rect(screen,blue,enemy)

    if player.colliderect(enemy):
        pygame.quit()
        print(f"YOU LOST!\nPoints:{points}")
        exit()

    if enemy.y >= (sheight/4)*3:
        enemy.y = 0
        enemy_length=random.randint((swidth/4)-player.width, (((swidth/2)-player.width)-player.width/2))
        enemy_pos += 1
        point_gain = False
        enemy_spd += 0.1

    if player.y < enemy.y-player.width and not point_gain:
        points += 1
        point_gain = True
    #enemy bullshit

    player.x += x_change
    player.y += y_change

    pygame.draw.rect(screen,green,player)

    #BOUNDARIES
    pygame.draw.rect(screen,black, (swidth/4,0,5,sheight))
    pygame.draw.rect(screen,black, ((swidth/4)*3,0,5,sheight))
    pygame.draw.rect(screen,red, ((swidth/4)+5,((sheight/4)*3)+player.height,(swidth/2)-5,((sheight/4)*3)))
    #BOUNDARIES

    y_change += 0.1

    text = font.render('Points:'+str(points), False, black)

    screen.blit(text,(0,0))

    #screen updates: END

    pygame.display.update()
