import pygame,sys
import time 
ruta = 'media/Imagenes/Sprites/'
import threading
from time import sleep 

class decorador:
	def __init__(self, screen, personaje,limite ,skin):
		self.screen = screen
		self.personaje = personaje
		self.a= time.time()
		self.identacion = 0
		self.imagen = pygame.image.load(ruta+skin)
		self.limite = limite
		
	def decorarAura(self, screen):
		
		c=0
		while(c >= (-5) ):
			b = time.time()
			c = self.a-b
			self.personaje.movimiento(screen)
			screen.blit(self.imagen,(self.personaje.posicionInicial),(self.identacion*self.personaje.ancho,0,self.personaje.ancho,self.personaje.largo))
			self.identacion += 1
			if (self.identacion >= self.limite):
				self.identacion = 0
				
			sleep(0.05)	
          	        
