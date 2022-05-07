# a cleaner version
# could probably separate into different modules to keep things clean

import pygame, sys
from pygame.locals import *
from time import sleep, time

# defining constants
MS_PER_TICK = 1 / 90
MS_PER_RENDER = 1 / 60
SPEED = 3

# -- define rectangle --
x = 0
y = 0
surf1 = pygame.Surface((30, 30))
pygame.draw.rect(surf1, (255, 255, 255), (0, 0, 30, 30))
pygame.draw.circle(surf1, (0, 255, 255), (15, 15), 15)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 400))
pygame.display.set_caption("TITLE OF MY GAME")


# draws to the screen
def render():
    DISPLAYSURF.fill((0, 0, 0))
    DISPLAYSURF.blit(surf1, (x, y))
    pygame.display.update()

def movement(keys):
    'handles character movement'
    global x 
    global y
    if keys[K_s]:
        y += SPEED
    if keys[K_w]:
        y -= SPEED
    if keys[K_d]:
        x += SPEED
    if keys[K_a]:
        x -= SPEED
        
def tick():
    keys = pygame.key.get_pressed()
    movement(keys)

# the game loop

previous_time = time()
lag = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    current_time = time()
    elapsed = current_time - previous_time
    previous_time = current_time
    lag += elapsed

    if lag >= MS_PER_RENDER:
        render()
        lag -= MS_PER_RENDER
    
    tick()
    sleep(MS_PER_TICK)