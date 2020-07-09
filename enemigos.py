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
    def muerte(self):
        self.imagen=movs[len(movs)-1]
class Spider(Enemy):
    def __init__(self,movs,velocidad):
        super().__init__(movs,velocidad)
    def mover(self):
        self.rect.y+=self.speed
        self.image = self.movs[self.imagen]
        #cuando choca arriba
        if self.rect.y <= 0:
            self.speed = 3
        #cuando choca abajo 
        elif self.rect.y >= random.randint(400, ancho):#alto- spider_size[0]:
            self.speed = -3
        self.imagen+=1
        if self.imagen>=len(self.movs)-2:
            self.imagen=0
class Rat(Enemy):
    def __init__(self,movs,velocidad):
        super().__init__(movs,velocidad)
    def mover(self):
        self.rect.x-=self.speed
        #izquierda
        if self.rect.x <= 0:
            self.speed = -3
            self.imagen = 1
        #derecha
        elif self.rect.x >= ancho- self.size[0]:
            self.speed = 3
            self.imagen = 0
        self.image = self.movs[self.imagen]

def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col

def mostrar_vidas(x,y):
    vidas_render =  tipo_letra1.render("Vidas : "+ str
    (vidas), True, (255,255,255))
    screen.blit(vidas_render,(x,y))

def game_over(x,y):
    imprimir= tipo_letra2.render("GAME OVER ", True, (255,255,255))
    screen.blit(imprimir,(x,y))
    
#JUEGO
tipo_letra1 = pygame.font.Font('freesansbold.ttf', 28)
tipo_letra2 = pygame.font.Font('freesansbold.ttf', 100)
vidas=1000
jugador=Player()
rat=Rat(rats,3)
spider=Spider(spiders,3)
enemigos.add(rat,spider)
listade_todoslos_sprites.add(jugador,enemigos)
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height
rat.rect.x=800//2-(rat.size[0]//2)
rat.rect.y=600-(rat.size[1])
spider.rect.x= random.randint(0,largo-spider.rect.width)
spider.rect.y= random.randint(0,ancho-spider.rect.height)
gets_hit = False
done=False
while not done:
    screen.blit(background,(0,0))
    jugador.update(gets_hit,vidas)
    rat.mover()
    spider.mover()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        #movimiento del perrito
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador.izquierda()
            if event.key == pygame.K_RIGHT:
                jugador.derecha()                
            if event.key == pygame.K_UP:
                jugador.saltar()
            if event.key == pygame.K_SPACE:
                jugador.ataque()                             
        #detenerse            
        if event.type == pygame.KEYUP:           
            if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
                jugador.stop()                                
            if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
                jugador.stop()
    #Vidas
    if vidas > 0:
        mostrar_vidas(10,10)
    elif vidas <=0:
        game_over(100,250)
        jugador.die()
    if checkCollision(spider,jugador)==True:
        if jugador.imagen!=7:
            gets_hit=True
            vidas-=1
            if vidas>0:
                jugador.get_hurt()
    else:
        gets_hit=False
    if checkCollision(rat,jugador)==True:
        if jugador.imagen!=7:
            gets_hit=True
            vidas-=3
            if vidas>0:
                jugador.get_hurt()
    else:
        gets_hit=False
    listade_todoslos_sprites.draw(screen)
    pygame.display.flip()
    reloj.tick(50)
pygame.quit()