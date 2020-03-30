import time
import pygame,sys,random
from personaje import *
from aura import *
from time import sleep 

class material:
	def __init__(self):
		pass
		
	def perderVida(self):
		pass
		
	def setPosicion(self,x,y):
		pass	
		

class Arbol (material):
	def __init__(self):
		self.vida = 100
		self.imagen = pygame.image.load('media/Imagenes/arbol.png')
		self.Rectangulo = None
		self.x =None
		self.y = None
	
	def perderVida(self):
		self.vida -= 10
		sleep(0.5)
		return 10
		
	def setPosicion(self, x,y):
		self.x = x
		self.y = y
		
class Roca (material):
	def __init__(self):
		self.vida = 200
		self.imagen = pygame.image.load('media/Imagenes/roca.png')
		self.Rectangulo = None 
	
	def perderVida(self):
		self.vida -= 5
		sleep (0.5)
		return 5
		
	def setPosicion(self, x,y):
		self.x = x
		self.y = y		
