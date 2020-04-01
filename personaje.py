import pygame,sys
import threading
from time import sleep 
ruta = 'media/Imagenes/Sprites/'
import math

class personaje:
	
	

	def __init__(self, arriba, abajo, izquierda , derecha, ancho, largo,limite ,posicionInicial, skin, iden):
		self.iden = iden
		self.limX = 0
		self.limY = 0
		self.inY = False 
		self.inX = True
		self.imagen = pygame.image.load(ruta+skin)
		self.posicionInicial = posicionInicial
		self.posicionDestino = posicionInicial
		self.derecha = derecha
		self.izquierda = izquierda
		self.abajo = abajo
		self.limite = limite
		self.arriba = arriba 
		self.identacion =0
		self.ancho=ancho 
		self.largo=largo
		self.velocidad = 10
		self.Rectangulo = pygame.Rect(posicionInicial[0],posicionInicial[1],30,64)
		self.List = []
		self.Impresion=(self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	
		self.c =True

		
		
		
		
	def getSpawn(self , Mapa): 
		self.Impresion = (self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	
		return self.Impresion

	def movimiento(self , Mapa):
		
		while (self.c):

   		    
		 if self.posicionDestino[0] < self.posicionInicial[0] and self.inX and  permitirPaso([(self.posicionInicial[0]+self.limX), self.posicionInicial[1]+self.limY ] , Mapa.ListRect) :
			
			
			 self.identacion = self.identacion +1
			 self.posicionInicial[0] -=self.velocidad
			 self.Impresion= (self.imagen,self.posicionInicial,self.identacion*self.ancho,self.izquierda*self.largo,self.ancho,self.largo)
			 #sleep(0.05)
			
		 if self.posicionDestino[1] > self.posicionInicial[1] and self.inY and permitirPaso([(self.posicionInicial[0]+self.limX), self.posicionInicial[1]+self.limY ] , Mapa.ListRect):
			
			 #screen.fill((255,255,255))
			
			 self.identacion = self.identacion +1
			 self.posicionInicial[1] +=self.velocidad
			 self.Impresion = (self.imagen,self.posicionInicial,self.identacion*self.ancho,self.abajo*self.largo,self.ancho,self.largo)
			 #sleep(0.05)					
				
		 if self.posicionDestino[0] > self.posicionInicial[0] and self.inX  and permitirPaso([(self.posicionInicial[0]+self.limX), self.posicionInicial[1]+self.limY ] , Mapa.ListRect):
			
			 #screen.fill((255,255,255))
			 self.identacion = self.identacion +1
			 self.posicionInicial[0] +=self.velocidad
			 self.Impresion=(self.imagen,self.posicionInicial,self.identacion*self.ancho,self.derecha*self.largo,self.ancho,self.largo)
			
			 #sleep(0.05)
			
		 if self.posicionDestino[1] < self.posicionInicial[1]  and self.inY and permitirPaso([(self.posicionInicial[0]+self.limX), self.posicionInicial[1]-self.limY] , Mapa.ListRect):
			
			 self.identacion = self.identacion +1
			 self.posicionInicial[1] -=self.velocidad
			 self.Impresion=(self.imagen,(self.posicionInicial),self.identacion*self.ancho,self.arriba*self.largo,self.ancho,self.largo)
			
				
		 if self.identacion >= self.limite:
			 self.identacion = 0	
			
		 if math.ceil(self.posicionInicial[0]/46)*46 == self.posicionDestino[0]:
			 self.posicionInicial[0] = self.posicionDestino[0]
		 if math.ceil(self.posicionInicial[1]/64)*64 == self.posicionDestino[1]:
			 self.posicionInicial[1] = self.posicionDestino[1]
		
		 if (self.posicionDestino[1] == self.posicionInicial[1]):
			 self.inY = False
			 self.inX = True
		 if (self.posicionDestino[0] == self.posicionInicial[0]):
			 self.inY = True
			 self.inX = False
		#print (str(self.posicionInicial[1]) +"->" + str(self.posicionDestino[1]))	
		 self.Rectangulo.left,self.Rectangulo.top = self.posicionInicial[0] + self.limX , self.posicionInicial[1]+ self.limY
		 
		 
		 sleep(0.05)
		 
		 	
	
	
	def setPosicionDestino(self, posicionDestino):
		self.posicionDestino = [math.ceil(posicionDestino[0]/46)*46, math.ceil(posicionDestino[1]/64)*64] 
				
		
				

class Orda:
	def __init__(self, personajes):
		self.personajes = personajes 
		
	
	def movimiento(self, Matriz):	    
		test = Matriz
		for i in self.personajes:   
	    
		    i.movimiento(test)
	
	def setPersonaje(self, personaje ):
		self.personajes.append(personaje)
		
	def borrarOrda(self):
		self.personajes = []			 	





class Mouse:

	
	def seleccion(screen, personajes, orda):
		#if 
		for i in orda:
			

			 if pygame.mouse.get_pressed()[0]==1 and i.Rectangulo.collidepoint(pygame.mouse.get_pos())==1:
				 pass

		
		
		
									
						    							    
							    
		
		 			 			 
					 
				
def permitirPaso(posicion, Lista):
	if (pygame.Rect(posicion[0],posicion[1],30,64).collidelist(Lista) == -1):
		return True 
	else:
		return False					
