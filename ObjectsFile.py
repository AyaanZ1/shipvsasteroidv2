import pygame
import random
from sys import exit as quit



pygame.init()


#make a background class
class Background(pygame.sprite.Sprite):
    def __init__(self,size,image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,size)

    def draw(self,screen):
        screen.blit(self.image,(0,0))


class Ship(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 254
        self.rect.y = 286
        self.speed = 3


    def update(self,enemy):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


        #boundaries
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 536:
            self.rect.y = 536
        if pygame.sprite.collide_mask(self,enemy):
            quit()
    def draw(self,screen):
        screen.blit(self.image,self.rect)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 1018
        self.rect.y = random.randint(0,586)
        self.image = pygame.transform.scale(self.image,(125,98))
        self.speed = 3


    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 1018
            self.rect.y = random.randint(0,586)
        if self.rect.x >= 1018:
            self.rect.x = 1018
            self.rect.y = random.randint(0,586)
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 1018:
            self.kill()

    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))




