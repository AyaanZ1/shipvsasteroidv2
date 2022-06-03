# import libraries and init
import pygame
import random
from sys import exit as quit
from ObjectsFile import *

pygame.init()

# set up
size = w, h = 1018, 573
c = pygame.time.Clock()
window = pygame.display.set_mode(size)
bg = Background((w, h), "./image/space bg.jpg")
ship = Ship("./image/ship.png")
asteroid = Asteroid("./image/asteroid.png")
not_hit = True
# main loop
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True

    if not_hit:
        ship.update()
        asteroid.update()
    if pygame.sprite.collide_mask(ship, asteroid):
        not_hit = False
        # display Game over font on pygame window
        font = pygame.font.SysFont("comicsansms", 100)
        text = font.render("Game Over", True, (255, 0, 0))
        window.blit(text, (w / 2 - text.get_width() / 2, h / 2 - text.get_height() / 2))
        pygame.display.update()
    # draw
    bg.draw(window)
    ship.draw(window)
    asteroid.draw(window)

    pygame.display.flip()
