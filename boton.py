import pygame,sys
import threading
from time import sleep
from fabricas import *


class boton:
	def __init__(self, texto, alto, ancho, posicion,screen):
		self.str = texto
		fuente1=pygame.font.Font(None,40)
		self.texto = fuente1.render(texto,0,(0,0,0)) 
		self.alto = alto
		self.ancho = ancho
		self.screen = screen
		self.posicion =posicion
		self.Rectangulo = pygame.Rect(posicion[0],posicion[1],self.ancho,self.alto)
		
		
	def setBoton(self):
		if self.Rectangulo.collidepoint(pygame.mouse.get_pos())==1:
			color = (100,100,100)
			
		else:
			color = (255,255,255)	
		pygame.draw.rect(self.screen, color, self.Rectangulo)
		self.screen.blit(self.texto, [self.posicion[0] +10,self.posicion[1] +10])
		
	def presionado(self):
		if pygame.mouse.get_pressed()[0]==1 and self.Rectangulo.collidepoint(pygame.mouse.get_pos())==1:
			return True
		else:
			return False
			
		
				
 
  
class botonConstruir(boton):
	def presionado(self, Madera, Roca):
		proxy = None
		if pygame.mouse.get_pressed()[0]==1 and self.Rectangulo.collidepoint(pygame.mouse.get_pos())==1:
			proxy = proxyConstrucion(Madera,Roca, self.screen)
			#temp = proxy.Construir()
		return proxy	
		
	    		 
	    		 
	    		 
