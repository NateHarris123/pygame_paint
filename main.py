import pygame
from pygame.locals import *
# PSEUDOCODE FOR GAME:
# Track cursor
# On mouse1 hold: change cursor color


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True 
    dt = 0 #delta time, change in time
    while(running):
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                run = False
    
main()