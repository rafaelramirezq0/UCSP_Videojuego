import pygame, sys

screen=pygame.display.set_mode([800,600])
reloj=pygame.time.Clock()
#colores
blanco=(255,255,255)
negro=(0,0,0)
#===========
pygame.init()

listade_todoslos_sprites = pygame.sprite.Group()
#Jugador (o sea el perrito)
class Player(pygame.sprite.Sprite):
    #velocidad inicial
    speed_x=0
    speed_y=0
    #constructor
    def __init__(self): 
        super().__init__() 
        # reemplazar con el sprite:
        self.image = pygame.image.load("game/run1.png")
        # rectángulo que ocupa
        self.rect = self.image.get_rect()
    #esto efectúa el movimiento, va "actualizando" la velocidad
    def update(self):
        self.gravity()
        #moverse
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #falta aquí chocar (o sea, poner lo que pasa si choca)   
    #gravedad
    def gravity(self):
        if self.speed_y == 0:
            self.speed_y = 5
        else:#aceleración de la gravedad
            self.speed_y += 0.35
        #tocar el suelo
        if self.rect.y >= 600 - self.rect.height and self.speed_y >= 0:
            self.speed_y = 0
            self.rect.y = 600 - self.rect.height
        #paredes
        if self.rect.right >=800:
            self.rect.x = 800 - self.rect.width
        if self.rect.left <=0:
            self.rect.x = 0
            
    #movimientos sin considerar plataformas
    def izquierda(self):
        self.speed_x = -5
    def derecha(self):
        self.speed_x = 5
    def saltar(self):
        if self.rect.bottom >= 600:
            self.speed_y = -10
    def stop(self):
        self.speed_x = 0
        self.gravity()
    
jugador=Player()
listade_todoslos_sprites.add(jugador)
done=False
jugador.rect.x=0
jugador.rect.y=600-jugador.rect.height
while not done:
    screen.fill(blanco)
    jugador.update()
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
                
                
        #detenerse            
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT and jugador.speed_x < 0: 
                jugador.stop()
                                
            if event.key == pygame.K_RIGHT and jugador.speed_x > 0:
                jugador.stop()
                
                
        
        
    
    
    listade_todoslos_sprites.draw(screen)
    
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()