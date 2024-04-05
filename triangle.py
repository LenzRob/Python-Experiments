import numpy as np
import pygame_widgets
import pygame
from pygame.locals import *
import random
import math
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

#const
screen_width = 550
screen_heigth = 500
spd = 3
number_of_rect = 30 # Anz jeder Farbe

def main():

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_heigth))
    pygame.display.set_caption('Triangle')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((50,50,50))
 
    #slider
    slider = Slider(screen, screen_width - 30, 20, 20, screen_heigth - 85, min=0, max=29, step=0.125, initial=0, vertical=True)
    output = TextBox(screen, screen_width - 40, screen_heigth - 40, 40, 40, frontSize=30)
    output.disable()  # Act as label instead of textbox

    screen.blit(background, (0,0))
    pygame.display.flip()

    #red rect
    red_lst = gen_rect(screen, (250,0,0), number_of_rect)
    color_obj = red_lst
    total_obj = len(color_obj)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.blit(background, (0,0))

        output.setText(slider.getValue())
        pygame_widgets.update(pygame.event.get())

        # Ball Movement & "BorderBounce"
        for ball in color_obj:
            if ball[2][0] - ball[3] * 0.5  < 0 or ball[2][0] + ball[3] * 0.5 > screen_width - 50:
                ball[4] = (-1 * ball[4][0], ball[4][1])

            if ball[2][1] - ball[3] * 0.5 < 0 or ball[2][1] + ball[3] * 0.5 > screen_heigth:
                ball[4] = (ball[4][0], -1 * ball[4][1])

            ball[2] = (ball[2][0] + ball[4][0], ball[2][1] + ball[4][1])

        # Draw Line in Between Points
        for ball_a in range(total_obj):

            for ball_b in range(total_obj):
                
                if ball_a == ball_b:
                    continue

                for ball_c in range(total_obj):

                    if ball_b == ball_c or ball_c == ball_a:
                        continue

                    ang_1 = math.degrees(math.atan2(color_obj[ball_a][2][1] - color_obj[ball_b][2][1], color_obj[ball_a][2][0] - color_obj[ball_b][2][0]) -
                                       math.atan2(color_obj[ball_c][2][1] - color_obj[ball_b][2][1], color_obj[ball_c][2][0] - color_obj[ball_b][2][0]))
                    ang_2 = math.degrees(math.atan2(color_obj[ball_b][2][1] - color_obj[ball_a][2][1], color_obj[ball_b][2][0] - color_obj[ball_a][2][0]) -
                                       math.atan2(color_obj[ball_c][2][1] - color_obj[ball_a][2][1], color_obj[ball_c][2][0] - color_obj[ball_a][2][0]))
                    
                    if ang_1 < 0:
                        ang_1 = abs(ang_1)
                    if ang_2 < 0:
                        ang_2 = abs(ang_2)

                    #print(f"arg_1 = {int(ang_1)}, arg_2 = {int(ang_2)}")
                    if ((int(ang_1) >= 60 - slider.getValue() and int(ang_1) <= 60 + slider.getValue()) and 
                        (int(ang_2) >= 60 - slider.getValue() and int(ang_2) <= 60 + slider.getValue())):
                        #print(f"ang1 = {int(ang_1)}, ang2 = {int(ang_2)}")
                        pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (color_obj[ball_a][2]), (color_obj[ball_b][2]), 3)
                        pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (color_obj[ball_c][2]), (color_obj[ball_b][2]), 3)
                        pygame.draw.line(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (color_obj[ball_c][2]), (color_obj[ball_a][2]), 3)
               
                #pygame.draw.line(screen, (100,200,200), (color_obj[ball_a][2]), (color_obj[ball_b][2]), 1)

        #screen.blit(background, (0,0))

        for i in range(total_obj):
            draw_rect(color_obj[i][0],color_obj[i][1],color_obj[i][2])

        pygame.draw.rect(screen, (100,100,100), (screen_width - 50, 0, 10, screen_heigth))

        pygame.display.flip()

def set_rnd_spd():
    # (-1 ^ 0 oder 1) * 0,xx
    x_spd = math.pow( -1, random.randint(0,1) ) * ( random.randint(1, 100) * 0.01 )
    y_spd = math.pow( -1, random.randint(0,1) ) * ( random.randint(1, 100) * 0.01 )

    return (x_spd, y_spd)

def draw_rect(src, color, pos_size):
    return pygame.draw.circle(src, color, pos_size, 4)

def gen_pos():
    return (random.randint(10,screen_width - 60), random.randint(10,screen_heigth - 10))

def gen_rect(src, color, total):
    gen_rect_list = []
    for i in range(total):
        gen_rect_list.append([src, color, gen_pos(), 10, set_rnd_spd()])
    return gen_rect_list

if __name__ == '__main__': main()