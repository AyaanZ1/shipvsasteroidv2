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
        self.speed = 1
        self.height = self.rect.height
        self.width = self.rect.width


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.centery -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.centery += self.speed


        #boundaries
        if self.rect.centery < 0:
            self.rect.centery = 0
        if self.rect.centery > 536:
            self.rect.centery = 536

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
        self.speed = 1


    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 1018
            self.rect.y = random.randint(0,586)
        if self.rect.x >= 1018:
            self.rect.x = 1018
            self.rect.y = random.randint(0,586)

    def draw(self,screen):
        screen.blit(self.image,(self.rect.centerx,self.rect.centery))

class Bullet(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.image = pygame.transform.scale(self.image,(25,25))


    def update(self,enemy):
        self.rect.x += self.speed
        if self.rect.x > 1018 or pygame.sprite.collide_mask(self,enemy):
            self.kill()

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        print(self.rect.x,self.rect.y)






