import pygame, sys

screen=pygame.display.set_mode([800,600])
reloj=pygame.time.Clock()
background=pygame.image.load("game/forest_loop.png")
#colores
blanco=(255,255,255)
negro=(0,0,0)
#===========
pygame.init()

listade_todoslos_sprites = pygame.sprite.Group()
#Jugador (o sea el perrito)
run1=pygame.image.load("game/run1.png")
run2=pygame.image.load("game/run2.png")
run3=pygame.image.load("game/run3.png")
run4=pygame.image.load("game/run4.png")
run5=pygame.image.load("game/run5.png")
run6=pygame.image.load("game/run6.png")
run7=pygame.image.load("game/run7.png")
attack=pygame.image.load("game/atack.png")
run1i=pygame.transform.flip(run1,True,False)
run2i=pygame.transform.flip(run2,True,False)
run3i=pygame.transform.flip(run3,True,False)
run4i=pygame.transform.flip(run4,True,False)
run5i=pygame.transform.flip(run5,True,False)
run6i=pygame.transform.flip(run6,True,False)
run7i=pygame.transform.flip(run7,True,False)
attack_inv=pygame.transform.flip(attack,True,False)
run=[run1,run2,run3,run4,run5,run6,run7,attack]
run_inv=[run1i,run2i,run3i,run4i,run5i,run6i,run7i,attack_inv]
runs=[run,run_inv]
#Atacado
hurt1=pygame.image.load("game/hurt1.png")
hurt2=pygame.image.load("game/hurt2.png")
hurt3=pygame.image.load("game/hurt3.png")

hurt1i=pygame.transform.flip(hurt1,True,False)
hurt2i=pygame.transform.flip(hurt2,True,False)
hurt3i=pygame.transform.flip(hurt3,True,False)

hurt=[hurt1,hurt2,hurt3]
hurt_inv=[hurt1i,hurt2i,hurt3i]
hurts=[hurt,hurt_inv]
#Muere
dead1=pygame.image.load("game/dead1.png")
dead2=pygame.image.load("game/dead2.png")
dead3=pygame.image.load("game/dead3.png")
dead4=pygame.image.load("game/dead4.png")
dead1i=pygame.transform.flip(dead1,True,False)
dead2i=pygame.transform.flip(dead2,True,False)
dead3i=pygame.transform.flip(dead3,True,False)
dead4i=pygame.transform.flip(dead4,True,False)
dead=[dead1,dead2,dead3,dead4]
dead_inv=[dead1i,dead2i,dead3i,dead4i]
dies=[dead,dead_inv]
#===========================================
def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        return col
#===========================================
class Player(pygame.sprite.Sprite):
    #velocidad inicial
    speed_x=0
    speed_y=0
    #animación base
    cambio=0
    imagen=0
    direc=0
    #constructor
    def __init__(self): 
        super().__init__() 
        # reemplazar con el sprite:
        self.image = runs[self.direc][self.imagen]
        # rectángulo que ocupa
        self.rect = self.image.get_rect()
        
    #esto efectúa el movimiento, va "actualizando" la velocidad e imagen
    def update(self,collision,vida):
        self.ancho=self.image.get_size()[1]
        self.largo=self.image.get_size()[0]
        self.gravity()
        self.deten_ataque()
        #moverse
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #animación
        self.imagen += self.cambio
        if self.imagen > len(run)-2 or (self.speed_x==0 and collision==False and vida>0):
            self.imagen = 0
        if self.speed_y!=0:
            self.imagen = 5
        if abs(self.speed_x)>5:
            self.imagen=len(run)-1
        self.image=runs[self.direc][self.imagen]
        #falta aquí chocar (o sea, poner lo que pasa si choca)   
    #gravedad
    def gravity(self):
        if self.speed_y == 0:
            self.speed_y = 5
        else:#aceleración de la gravedad
            self.speed_y += 0.35
        #tocar el suelo
        if self.rect.y >= 600 - self.ancho and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = 600 - self.ancho
        #paredes
        if self.rect.x >800-self.largo:
            self.rect.x = 800-self.largo
        if self.rect.x <0:
            self.rect.left =0       
    #movimientos sin considerar plataformas
    
    def izquierda(self):
        self.speed_x = -5
        self.cambio = 1
        self.direc=1
    def derecha(self):
        self.speed_x = 5
        self.cambio = 1
        self.direc=0
    def saltar(self):
        if self.rect.bottom >= 600:
            self.speed_y = -10
    def stop(self):
        self.speed_x = 0
        self.gravity()
    def ataque(self):
        if self.imagen!=len(run)-1:
            self.speed_x*=2
    #frenos (funciona de forma similar a la gravedad, solo que desacelera)
    def deten_ataque(self):
        if self.speed_x>5:
            self.speed_x-=0.15
        if self.speed_x<-5:
            self.speed_x+=0.15
    def get_hurt(self):
        self.cambio = 1
        if self.imagen>=len(hurt)-1:
            self.imagen=0
        self.image=hurts[self.direc][self.imagen]
    def die(self):
        self.cambio = 1
        if self.imagen>=len(dead)-1:
            self.imagen=len(dead)-1
        self.image=dies[self.direc][self.imagen]
        
    
jugador=Player()
listade_todoslos_sprites.add(jugador)
done=False
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height
vidas=1000
gets_hit = False
while not done:
    screen.blit(background,(0,0))
    jugador.update(False,1)
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
                
                
        
        
    
    
    listade_todoslos_sprites.draw(screen)
    pygame.display.flip()
    reloj.tick(50)
pygame.quit()
