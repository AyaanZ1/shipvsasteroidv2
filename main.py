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
bg = Background((w,h),"./image/space bg.jpg")
ship = Ship("./image/ship.png")
asteroid = Asteroid ("./image/asteroid.png")

#main loop
running = True
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True




    ship.update()
    asteroid.update()



    #draw
    bg.draw(window)
    ship.draw(window)
    asteroid.draw(window)

    pygame.display.flip()


