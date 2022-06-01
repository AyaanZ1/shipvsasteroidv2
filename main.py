#import libraries and init
import pygame
import random
from sys import exit as quit
from ObjectsFile import *
pygame.init()

#set up
size = w,h = 1018,573
c = pygame.time.Clock()
window = pygame.display.set_mode(size)
bg = background((w,h),"./image/space bg.jpg")
ship = ship("./image/ship.png")
asteroid = asteroid("./image/asteroid.png")
#main loop
running = True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update
    ship.update(asteroid)
    asteroid.update()


    #draw
    bg.draw(window)
    ship.draw(window)
    asteroid.draw(window)
    pygame.display.flip()


