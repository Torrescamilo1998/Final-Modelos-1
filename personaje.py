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
		self.Rectangulo = pygame.Rect(posicionInicial[0],posicionInicial[1]+30,20,20)
		self.List = []
		self.Impresion=(self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	

		
		
		
		
	def getSpawn(self , Mapa): 
		self.Impresion = (self.imagen,(self.posicionInicial),self.derecha*self.largo,self.derecha*self.largo,self.ancho,self.largo)	
		return self.Impresion

	def movimiento(self , Mapa):
   		    
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
				
		if self.posicionDestino[0] > self.posicionInicial[0] and self.inX  and permitirPaso([(self.posicionInicial[0]+self.limX+ self.velocidad), self.posicionInicial[1]+self.limY ] , Mapa.ListRect):
			
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
		self.Rectangulo.left,self.Rectangulo.top = self.posicionInicial[0] + self.limX , self.posicionInicial[1]+30+ self.limY
		
		
		sleep(0.05)
		return self.Impresion	
	
	
	def setPosicionDestino(self, posicionDestino):
		print (posicionDestino)
		self.posicionDestino = [math.ceil(posicionDestino[0]/46)*46, math.ceil(posicionDestino[1]/64)*64] 
		print (self.posicionDestino)		
		
				

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
	def __init__(self):
		self.estado = False
		self.Rectangulo= pygame.Rect(0,0,0,0)
		self.a=(0,0)
	
	def seleccion(self,screen, personajes, orda, limX, limY):
		
		
		if pygame.mouse.get_pressed()[0]==1 and self.estado ==False :
				self.a = pygame.mouse.get_pos()
				print (self.a)
				self.estado=True
		if pygame.mouse.get_pressed()[0]==0 and self.estado==True and pygame.key.get_pressed()[275] == 1:
					b=pygame.mouse.get_pos()
					self.estado = False
					if (self.a[0]<b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],self.a[1],(b[0]-self.a[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]<b[1]):
						self.Rectangulo = pygame.Rect(b[0],self.a[1],(self.a[0]-b[0]),(b[1]-self.a[1]))
						
					if 	(self.a[0]<b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(self.a[0],b[1],(b[0]-self.a[0]),(self.a[1]-b[1]))
						
					if 	(self.a[0]>b[0] and self.a[1]>b[1]):
						self.Rectangulo = pygame.Rect(b[0],b[1],(self.a[0]-b[0]),(self.a[1]-b[1]))
						
					self.Rectangulo.left += (limX*46)
					self.Rectangulo.top += (limY*64) 	
					
					for i in personajes:
                       
						if self.Rectangulo.contains(i.Rectangulo)==1:
							print("True")
							orda.setPersonaje(i)
							screen.blit(pygame.image.load('media/Imagenes/seleccion.png'),i.posicionInicial)

							
						    							    
							    
		
		 			 			 
					 
				
def permitirPaso(posicion, Lista):
	if (pygame.Rect(posicion[0]+10,posicion[1]+30,20,20).collidelist(Lista) == -1):
		return True 
	else:
		return False					
