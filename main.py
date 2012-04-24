import pygame, math, sys
from pygame.locals import *


TILES_ACROSS = 20 - 1
TILES_DOWN = 15 - 1

class Color(object):
    """ named colors """
    black = (0, 0, 0)
    white = (255, 255, 255)


class Map(object):
    """
        The current map
    """
    def __init__(self):
        self.map = []
        for i in range(TILES_ACROSS + 1):
            row = []
            for j in range(TILES_DOWN + 1):
                row.append(0)
            self.map.append(row)

    def clear_block(self, position):
        x, y = position
        column = x/50
        row = y/50
        print "Column {}, row {}".format(column, row)
        self.map[column][row] = 1

    def print_ascii_map(self):
        for row in self.map:
            print row


class Game(object):
    def __init__(self):
        
        self.screen = pygame.display.set_mode((1024, 768))
        self.player = pygame.image.load('data/images/dude.png')
        self.clock = pygame.time.Clock()

        self.direction = 0
        self.position = (300, 300) 
    
        self.map = Map()

    def draw_board(self):
        for row in range(TILES_ACROSS + 1):
            for col in range(TILES_DOWN + 1):
                if self.map.map[row][col] == 0: # draw black only if it's not discvoered
                    pygame.draw.rect(self.screen, Color.black, (row*50, col*50, 49, 49))

    def move(self, hor, vert):
        x, y = self.position
        x = x + hor
        y = y + vert
        self.position = (x, y)
        self.map.clear_block(self.position)

    def run(self):
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

            self.move(hor, vert)
            self.screen.fill(Color.white)
            self.draw_board()
            self.screen.blit(self.player, self.position)
            pygame.display.flip()

            self.clock.tick(30)

if __name__ == "__main__":
    game = Game()
#    game.map.print_ascii_map()
    game.run()



