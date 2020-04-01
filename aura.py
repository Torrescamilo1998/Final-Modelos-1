import pygame,sys
import time 
ruta = 'media/Imagenes/Sprites/'
import threading
from time import sleep 

class decorador:
	
		
	def decorarAura(screen,personaje):
		screen.blit(pygame.load.image("media/Imagenes/seleccion.png"), personaje.posicionInicial)
		
	def decorarEstado(screen,personaje):
		pygame.draw.rect(screen,(255,0,0), pygame.Rect(personaje.posicionInicial,(30,6))) 
		sleep(0.5)     	        
