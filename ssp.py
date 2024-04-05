import numpy as np
import pygame
from pygame.locals import *
import random

#const
screen_width = 1000
screen_heigth = 1000
spd = 0.5
number_of_rect = 150 # Anz jeder Farbe

def draw_rect(src, color, pos_size):
    return pygame.draw.rect(src, color, pos_size)

def gen_pos():
    return (random.randint(0,screen_width - 10), random.randint(0,screen_heigth - 10), 10, 10)

def gen_rect(src, color, total):
    gen_rect_list = []
    for i in range(total):
        gen_rect_list.append([src, color, Rect(gen_pos())])
    return gen_rect_list

def main():

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_heigth))
    pygame.display.set_caption('SSP')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    screen.blit(background, (0,0))
    pygame.display.flip()

    #red
    red_lst = gen_rect(screen, (250,0,0), number_of_rect)

    #green
    green_lst = gen_rect(screen, (0,250,0), number_of_rect)

    #blue
    blue_lst = gen_rect(screen, (0,0,250), number_of_rect)
    
    color_obj = red_lst + green_lst + blue_lst

    total_obj = len(color_obj)

    #red -> green -> blue -> red
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.blit(background, (0,0))

        for ssp in color_obj:
            # RED
            if ssp[1] == (250,0,0):
                # if GREEN is EMTPY, SKIP
                if len(green_lst)  == 0:
                    continue    
                # Set Value
                index = 0
                min_dist_index = 0 
                min_dist = max(screen_width, screen_heigth)
                min_curr = max(screen_width, screen_heigth)
                # Manhantten Distance Calc
                for ssp_h in green_lst:
                    # Calc Manhatten Distance between RED & GREEN Rect
                    min_curr = min(min_dist, (abs(ssp[2][0] - ssp_h[2][0]) + abs(ssp[2][1] - ssp_h[2][1])))
                    # Set Value for Lowest Dist
                    if min_curr < min_dist:
                        min_dist = min_curr
                        min_dist_index = index
                    # Increase Index
                    index += 1

                pygame.draw.line(screen, (200,0,0), (ssp[2][0] + 5, ssp[2][1] + 5), (green_lst[min_dist_index][2][0] + 5, green_lst[min_dist_index][2][1] + 5))
                
                x = list(ssp[2])
                

                if (green_lst[min_dist_index][2][0] <= ssp[2][0] and ssp[2][0] > 0):
                    x[0] -= spd
                if (green_lst[min_dist_index][2][0] >= ssp[2][0] and ssp[2][0] < (screen_width - 10)):
                    x[0] += spd

                if (green_lst[min_dist_index][2][1] <= ssp[2][1] and ssp[2][1] > 0):
                    x[1] -= spd
                if (green_lst[min_dist_index][2][1] >= ssp[2][1] and ssp[2][1] < screen_heigth - 10):
                    x[1] += spd

                ssp[2] = tuple((x[0], x[1], 10, 10))

                if ssp != ssp_h and green_lst[min_dist_index][1] != ssp[1]:

                    if pygame.Rect.colliderect(Rect(ssp[2]), Rect(green_lst[min_dist_index][2])):
                        
                        green_lst[min_dist_index][1] = ssp[1]
                        red_lst.append(green_lst.pop(min_dist_index))
                        continue
                        
            # GREEN
            if ssp[1] == (0,250,0):
                # if BLUE is EMTPY, SKIP
                if len(blue_lst)  == 0:
                    continue    
                # Set Value
                index = 0
                min_dist_index = 0 
                min_dist = max(screen_width, screen_heigth)
                min_curr = max(screen_width, screen_heigth)
                # Manhantten Distance Calc
                for ssp_h in blue_lst:
                    # Calc Manhatten Distance between RED & GREEN Rect
                    min_curr = min(min_dist, (abs(ssp[2][0] - ssp_h[2][0]) + abs(ssp[2][1] - ssp_h[2][1])))
                    # Set Value for Lowest Dist
                    if min_curr < min_dist:
                        min_dist = min_curr
                        min_dist_index = index
                    # Increase Index
                    index += 1

                pygame.draw.line(screen, (0,200,0), (ssp[2][0] + 5,ssp[2][1] + 5), (blue_lst[min_dist_index][2][0] + 5, blue_lst[min_dist_index][2][1] + 5))
                
                x = list(ssp[2])
                

                if (blue_lst[min_dist_index][2][0] <= ssp[2][0] and ssp[2][0] > 0):
                    x[0] -= spd
                if (blue_lst[min_dist_index][2][0] >= ssp[2][0] and ssp[2][0] < (screen_width - 10)):
                    x[0] += spd

                if (blue_lst[min_dist_index][2][1] <= ssp[2][1] and ssp[2][1] > 0):
                    x[1] -= spd
                if (blue_lst[min_dist_index][2][1] >= ssp[2][1] and ssp[2][1] < screen_heigth - 10):
                    x[1] += spd

                ssp[2] = tuple((x[0], x[1], 10, 10))

                if ssp != ssp_h and blue_lst[min_dist_index][1] != ssp[1]:

                    if pygame.Rect.colliderect(Rect(ssp[2]), Rect(blue_lst[min_dist_index][2])):
                        
                        blue_lst[min_dist_index][1] = ssp[1]
                        green_lst.append(blue_lst.pop(min_dist_index))
                        continue

            # BLUE
            if ssp[1] == (0,0,250):
                # if BLUE is EMTPY, SKIP
                if len(red_lst)  == 0:
                    continue    
                # Set Value
                index = 0
                min_dist_index = 0 
                min_dist = max(screen_width, screen_heigth)
                min_curr = max(screen_width, screen_heigth)
                # Manhantten Distance Calc
                for ssp_h in red_lst:
                    # Calc Manhatten Distance between RED & GREEN Rect
                    min_curr = min(min_dist, (abs(ssp[2][0] - ssp_h[2][0]) + abs(ssp[2][1] - ssp_h[2][1])))
                    # Set Value for Lowest Dist
                    if min_curr < min_dist:
                        min_dist = min_curr
                        min_dist_index = index
                    # Increase Index
                    index += 1

                pygame.draw.line(screen, (0,0,200), (ssp[2][0] + 5, ssp[2][1] + 5), (red_lst[min_dist_index][2][0] + 5, red_lst[min_dist_index][2][1] + 5))
                
                x = list(ssp[2])
                

                if (red_lst[min_dist_index][2][0] <= ssp[2][0] and ssp[2][0] > 0):
                    x[0] -= spd
                if (red_lst[min_dist_index][2][0] >= ssp[2][0] and ssp[2][0] < (screen_width - 10)):
                    x[0] += spd

                if (red_lst[min_dist_index][2][1] <= ssp[2][1] and ssp[2][1] > 0):
                    x[1] -= spd
                if (red_lst[min_dist_index][2][1] >= ssp[2][1] and ssp[2][1] < screen_heigth - 10):
                    x[1] += spd

                ssp[2] = tuple((x[0], x[1], 10, 10))

                if ssp != ssp_h and red_lst[min_dist_index][1] != ssp[1]:

                    if pygame.Rect.colliderect(Rect(ssp[2]), Rect(red_lst[min_dist_index][2])):
                        
                        red_lst[min_dist_index][1] = ssp[1]
                        blue_lst.append(red_lst.pop(min_dist_index))
                        continue

        #screen.blit(background, (0,0))

        for i in range(total_obj):
            draw_rect(color_obj[i][0],color_obj[i][1],color_obj[i][2])

        pygame.display.flip()

if __name__ == '__main__': main()