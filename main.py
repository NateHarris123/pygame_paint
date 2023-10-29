import pygame
import math
from pygame.locals import *
# PSEUDOCODE FOR GAME:
# Track cursor
# On mouse1 hold: change cursor color
def fill_line(screen,color,previous,current):
    if not(current[0] - previous[0] == 0):
        slope = (current[1]-previous[1])/ ( current[0] - previous[0])
        if(abs(slope) < 1):
            if current[0] > previous[0]:
                x = previous[0]
                while x < current[0]:
                    x += 1
                    y = slope * (x - previous[0]) + previous[1]
                    pygame.draw.circle(screen,color,(x,y),4, 0)
            else:
                x = previous[0]
                while x > current[0]:
                    x -= 1
                    y = slope * (x -previous[0]) + previous[1]
                    pygame.draw.circle(screen,color,(x,y),4, 0)
        else:
            if (current[1] > previous[1]):
                y = previous[1]
                while y < current[1]:
                    y += 1
                    x = ((y - previous[1]) / slope) + previous[0]
                    pygame.draw.circle(screen,color,(x,y),4,0)
            else:
                y = previous[1]
                while y > current[1]:
                    y -= 1
                    x = ((y - previous[1])/ slope) + previous[0]
                    pygame.draw.circle(screen,color,(x,y),4,0) 
    else:
        y = previous[1]
        if y < current[1]:
            while y < current[1]:
                y += 1
                pygame.draw.circle(screen,color,(current[0],y),4,0) 
        else:
            while y > current[1]:
                y -= 1
                pygame.draw.circle(screen,color,(current[0],y),4,0) 
                
            
    
    
    

dic = {pygame.K_1 : pygame.Color(0,0,0), pygame.K_2 : pygame.Color(255,0,0), pygame.K_3 : pygame.Color(0,255,0), pygame.K_4 : pygame.Color(0,0,255), pygame.K_5 : pygame.Color(0,255,255)} #event.type = k_#
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True 
    is_painting = False
    dt = 0 #delta time, change in time
    screen.fill((255,255,255))
    x = (0,0,0) #permanent
    previous_mouse_pos = pygame.mouse.get_pos()
    while(running): #while running is true
        mouse_pos = pygame.mouse.get_pos() #returns a tuple for the x,y of mouse

        for event in pygame.event.get(): #gets a list of every single event that is done 
            #in each frame
            if event.type == pygame.QUIT:
                running = False #checking if you closed the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_painting = not is_painting #changes value of is_painting (false) to (true)
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_9]:
                    screen.fill((255,255,255))
                for i in range(pygame.K_1,pygame.K_5):
                    if keys[i]:
                        x = dic[i]
        if is_painting: #if true
            pygame.draw.circle(screen,x,(mouse_pos[0],mouse_pos[1]),4, 0) #built in function
            #function above takes (surface, color of surface, rectangle to surface (what its draw,
            # left most, right most, 2 and 2 is width)
            fill_line(screen,x,previous_mouse_pos,mouse_pos)
        pygame.display.flip()
        clock.tick(800)
        previous_mouse_pos = mouse_pos

            

        
    
main()