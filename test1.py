import pygame, math, sys
from pygame.locals import *

class Color(object):
    black = (0, 0, 0)
    white = (255, 255, 255)


screen = pygame.display.set_mode((800, 600))
player = pygame.image.load('data/images/dude.png')
clock = pygame.time.Clock()

direction = 0
position = (300, 300) #not sure why we're starting here. Maybe each cell is 300px?

def main():
    global position
    while 1:
        hor = 0
        vert = 0

        # so it turns out you have to call get
        # in order for pygame.keys.get_pressed() to work
        for event in pygame.event.get():
            pass

        # get smooth input
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]: sys.exit(0)
        if keys[K_LEFT]: hor = -25
        if keys[K_RIGHT]: hor = 25
        if keys[K_UP]: vert = -25
        if keys[K_DOWN]: vert = 25


        x, y = position
        x = x + hor
        y = y + vert
        position = (x, y)
        screen.fill(Color.black)
        screen.blit(player, position)
        pygame.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()
