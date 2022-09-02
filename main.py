import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("The jar")

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

custom_colour=[0,0,0]

FPS = 60

x_change = 0

enemy_length=random.randint(150, 350)
enemy_pos=0
enemy = pygame.Rect(205, 0, enemy_length, 25)

player = pygame.Rect(375, 300, 50, 50)

points = 0
point_gain = False

font = pygame.font.SysFont('MathJax_Typewriter', 30)
text = font.render('Points:\n'+str(points), False, black)

y_change = 0

while True:
    clock.tick(FPS)
    
    enemy.y += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x_change = 10
            if event.key == K_LEFT:
                x_change = -10
            if event.key == K_SPACE:
                y_change = 0
                player.y -= 30
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_LEFT:
                x_change = 0

    if player.y >= 400 or player.x <= 200 or player.x >= (600-50) or player.y <= 0:
        pygame.quit()
        print(f"YOU LOST!\npoints:{points}")
        exit()

    screen.fill(white)

    #screen updates: START
    #enemy bullshit
    if (enemy_pos % 2) == 0:
        enemy.x = 205 
        enemy.width = enemy_length
    else:
        enemy.width = enemy_length
        enemy.x = (200+(400-enemy_length))
        
    pygame.draw.rect(screen,blue,enemy)

    if player.colliderect(enemy):
        pygame.quit()
        print(f"YOU LOST!\nPoints:{points}")
        exit()

    if enemy.y >= 400:
        enemy.y = 0
        enemy_length=random.randint(150, 300)
        enemy_pos += 1
        point_gain = False

    if player.y < enemy.y-50 and not point_gain:
        points += 1
        point_gain = True
    #enemy bullshit

    player.x += x_change
    player.y += y_change

    pygame.draw.rect(screen,green,player)

    #BOUNDARIES
    pygame.draw.rect(screen,black, (200,0,5,600))
    pygame.draw.rect(screen,black, (600,0,5,600))
    pygame.draw.rect(screen,red, (205,450,395,200))
    #BOUNDARIES

    y_change += 0.1

    text = font.render('Points:'+str(points), False, black)

    screen.blit(text,(0,0))

    #screen updates: END

    pygame.display.update()

