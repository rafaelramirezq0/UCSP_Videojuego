import pygame, sys, random
from jugador import Player
ancho=800
largo=600
screen=pygame.display.set_mode([ancho,largo])
reloj=pygame.time.Clock()
background=pygame.image.load("game/forest_loop.png")
#colores
blanco=(255,255,255)
negro=(0,0,0)
#===========
pygame.init()

listade_todoslos_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
enemigo_rat= pygame.image.load("game/Sprites/rat/rat_idle.png")
enemigo_rat_inv= pygame.transform.flip(enemigo_rat,True,False)
rats=[enemigo_rat,enemigo_rat_inv]
enemigo_spider=pygame.image.load("game/Sprites/spider/idle1.png")
enemigo_spider2=pygame.image.load("game/Sprites/spider/idle2.png")
enemigo_spider3=pygame.image.load("game/Sprites/spider/idle3.png")
enemigo_spider4=pygame.image.load("game/Sprites/spider/idle4.png")
spiders=[enemigo_spider,enemigo_spider2,enemigo_spider3,enemigo_spider4]
class Enemy(pygame.sprite.Sprite):
    def __init__(self,movs,velocidad):
        super().__init__()
        self.imagen=0
        self.image = movs[self.imagen]
        self.speed = velocidad
        self.rect=self.image.get_rect()
        self.size=self.image.get_size()
        self.movs=movs   
class Spider(Enemy):
    def __init__(self,movs,velocidad):
        super().__init__(movs,velocidad)
    def mover(self):
        self.rect.y+=self.speed
        self.image = self.movs[self.imagen]
        #cuando choca arriba
        if self.rect.y <= 0:
            self.speed*=-1
        #cuando choca abajo 
        elif self.rect.y >= random.randint(400, largo-self.size[0]):#alto- spider_size[0]
            self.speed*=-1
        self.imagen+=1
        if self.imagen>=len(self.movs)-2:
            self.imagen=0
class Rat(Enemy):
    def __init__(self,movs,velocidad,paredes):
        super().__init__(movs,velocidad)
        self.paredes=paredes
    def mover(self):
        self.rect.x-=self.speed
        #izquierda
        if self.rect.x <= self.paredes[0]:
            self.speed*=-1
            self.imagen = 1
        #derecha
        elif self.rect.x >= self.paredes[1]- self.size[0]:
            self.speed*=-1
            self.imagen = 0
        self.image = self.movs[self.imagen]

