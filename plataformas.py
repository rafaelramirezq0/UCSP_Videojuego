import pygame, sys, random
from jugador import Player
from enemigos import Enemy, Rat, Spider

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

tronco=pygame.image.load("game/Sprites/tronco.jpg")
class Plataforma(pygame.sprite.Sprite):
 
    def __init__(self, largo, alto, x, y):
        super().__init__()
        self.image=pygame.transform.scale(tronco,(largo,alto))
        self.rect = self.image.get_rect()                    
        self.rect.x = x
        self.rect.y = y
    def mover(self,dfx):
        self.rect.x += dfx
plat1=Plataforma(150,40,200,220)
plat2=Plataforma(150,40,600,450)
plat3=Plataforma(100,30,400,350)
plataformas=pygame.sprite.Group()

'''
def checkCollision(sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col

def mostrar_vidas(x,y):
    vidas_render =  tipo_letra1.render("Vidas : "+ str
    (vidas), True, blanco)
    screen.blit(vidas_render,(x,y))

def game_over(x,y):
    imprimir= tipo_letra2.render("GAME OVER ", True, blanco)
    screen.blit(imprimir,(x,y))

def win(x,y):
    imprimir= tipo_letra2.render("YOU WIN ", True, blanco)
    screen.blit(imprimir,(x,y))

#JUEGO
tipo_letra1 = pygame.font.Font('freesansbold.ttf', 28)
tipo_letra2 = pygame.font.Font('freesansbold.ttf', 100)
vidas=1000
jugador=Player()
rat=Rat(rats,3)
spider=Spider(spiders,3)
enemigos.add(rat,spider)
plataformas.add(plat1,plat2,plat3)
listade_todoslos_sprites.add(jugador,enemigos,plataformas)
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
    jugador.update(gets_hit,vidas,plataformas)
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
        if jugador.imagen!=7:#imagen cuando está atacando
            gets_hit=True
            vidas-=1
            if vidas>0:
                jugador.get_hurt()
    else:
        gets_hit=False
    if checkCollision(rat,jugador)==True and rat in listade_todoslos_sprites:
        if jugador.imagen!=7: 
            gets_hit=True
            vidas-=3
            if vidas>0:
                jugador.get_hurt()
        else:
            listade_todoslos_sprites.remove(rat)
            
    else:
        gets_hit=False
    listade_todoslos_sprites.draw(screen)
    pygame.display.flip()
    reloj.tick(50)
pygame.quit()
'''