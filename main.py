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
asteroid = Asteroid("./image/asteroid.png")
drawables = pygame.sprite.Group()
shoot = False
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


    #update
    ship.update(asteroid)
    asteroid.update()

    if shoot:    
        shoot = False
        bullet = Bullet("./image/bullet.png",ship.rect.x,ship.rect.y)
        drawables.add(bullet)
        while not pygame.sprite.collide_mask(bullet, asteroid) and bullet.rect.x < 1018:
            bullet.update()
            if pygame.sprite.collide_mask(bullet, asteroid):
                asteroid.rect.x = 1018
                drawables.remove(bullet)

    #draw
    bg.draw(window)
    ship.draw(window)
    asteroid.draw(window)
    drawables.draw(window)
    pygame.display.flip()


