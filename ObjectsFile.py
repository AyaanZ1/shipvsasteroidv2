import pygame
import random
from sys import exit as quit



pygame.init()


#make a background class
class background(pygame.sprite.Sprite):
    def __init__(self,size,image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,size)

    def draw(self,screen):
        screen.blit(self.image,(0,0))


class ship(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 254
        self.y = 286


    def update(self,enemy):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 1
        if keys[pygame.K_DOWN]:
            self.y += 1
        self.rect.x = self.x
        self.rect.y = self.y

        #boundaries
        if self.y < 0:
            self.y = 0
        if self.y > 536:
            self.y = 536
        if pygame.sprite.collide_mask(self,enemy):
            quit()
    def draw(self,screen):
        screen.blit(self.image,self.rect)


class asteroid(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 1018
        self.y = random.randint(0,586)
        self.image = pygame.transform.scale(self.image,(125,98))


    def update(self):
        self.x -= 1
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x < 0:
            self.x = 1018
            self.y = random.randint(0,586)
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))


