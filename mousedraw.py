import pygame
from pygame.locals import *
import random

# pygame setup
pygame.init()
pygame.display.set_caption("TicTacToe")
screen = pygame.display.set_mode((1200,1000))
clock = pygame.time.Clock()
running = True
dt = 0

class Pointer:
    def __init__(self, widht, height, x, y):
        self.widht = widht
        self.height = height
        self.x = x
        self.y = y
        self.color = (0,0,0)

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.widht, self.height))

dot = Pointer(5, 5, -10, -10)
run_y = 0

screen.fill("black")

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEMOTION:
            print(pygame.mouse.get_pos())
            mouse_pos = pygame.mouse.get_pos()
            dot = Pointer(5, 5, mouse_pos[0],  mouse_pos[1])
            dot.x = mouse_pos[0]
            dot.y = mouse_pos[1]
            dot.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        elif event.type == MOUSEWHEEL:
            print(event.x, event.y)
            if (event.y == 1):
                dot.widht += 1
                dot.height += 1
            if (event.y == -1 and dot.widht > 10):
                dot.widht -= 1
                dot.height -= 1

    #if run_y < 590:
    #    dot.y += 2

    #dot.x = random.randint(0,1200)
    #dot.y = random.randint(0,1000)
    dot.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


    # fill screen
    # screen.fill("gray")

    # RENDER THE GAME HERE
    dot.draw()
   


    # flip() the display
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
    