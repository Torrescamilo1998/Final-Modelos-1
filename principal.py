import time
import pygame,sys,random
from personaje import *
from aura import *
import threading
from logica  import *
from boton import *






class IEstrategiaAnimaciones:
	def evaluar (self, numero):
		pass
	
	def limpiar(self, posicion):
		pass
		
	def imprimir(self):
		pass
		
	def animarEspecifico(self, a):
		pass
		
				




class MapaEstandar(IEstrategiaAnimaciones):
	
	def __init__(self, screen):
		self.posicionImpresion = [0,0]
		self.dimension=500
		self.MatrizLogica=[[0 for x in range(self.dimension)] for y in range(self.dimension)]
		self.MatrizLogica2=[[0 for x in range(self.dimension)] for y in range(self.dimension)]
		for i in range (0,self.dimension):
		   for j in range (0,self.dimension):
			   self.MatrizLogica[0][0] = 0
			   self.MatrizLogica2[0][0]= 0
			   
		self.anchoImpresion = 46
		self.altoImpresion 	=64   

			   
		self.ListaImagenes =  [ 
		pygame.image.load('media/Obreros.png'), 
		pygame.image.load('media/Soldados.png'),
		pygame.image.load('media/Casa.png')
		 ]  
				   
		self.screen = screen

	def evaluar(self,numero):
		hierba= pygame.image.load('media/Imagenes/hierba.jpg')
		arbol= pygame.image.load('media/Imagenes/arbol.png')
		roca= pygame.image.load('media/Imagenes/roca.png')
		if numero == 0:
			return hierba
			
		elif numero == 1:
			return arbol
			
		elif numero == 2:
			return roca
		else:
			return int
			
		
			
	def limpiar(self, posicion):
		hierba= pygame.image.load('media/Imagenes/hierba.jpg')
		arbol= pygame.image.load('media/Imagenes/arbol.png')
		roca= pygame.image.load('media/Imagenes/roca.png')
		for i in range (round(posicion[1]/self.altoImpresion)-2,round(posicion[1]/self.altoImpresion)+2):
			for j in range (round(posicion[0]/self.anchoImpresion)-2,round(posicion[0]/self.anchoImpresion)+2):
				self.screen.blit(hierba,(j*self.anchoImpresion,i*self.altoImpresion))
				if  self.MatrizLogica2[i][j] == 1:
					self.screen.blit(arbol,(j*self.anchoImpresion,i*self.altoImpresion))
				elif  self.MatrizLogica2[i][j] == 2:
					self.screen.blit(roca,(j*self.anchoImpresion,i*self.altoImpresion))
					
			
 
			
	def setMatriz(self,Matriz):
		self.MatrizLogica = Matriz
				   
	     	
	     	
	def moverMapa(self, caso, personaje):
		if caso== 0 and self.posicionImpresion[0]+1<482:
			self.posicionImpresion[0] += 1
			for i in personaje:
				i.left -= (46)
			
			
			
			
		if caso== 1 and self.posicionImpresion[0]-1>0:
			self.posicionImpresion[0] -= 1
			for i in personaje:
				i.left += (46)
				
			
			
				
		if caso== 2 and self.posicionImpresion[1]+1<480:
			self.posicionImpresion[1] += 1
			for i in personaje:
				i.top -= (64)		
			
			
		if caso== 3 and self.posicionImpresion[1]-1>0:
			self.posicionImpresion[1] -= 1
			for i in personaje:
				i.top += (64)

		
		
			
		 
			
	
	
	def imprimirMapa(self, screen):		 
	 hierba= pygame.image.load('media/Imagenes/hierba.jpg')
	 arbol= pygame.image.load('media/Imagenes/arbol.png')
	 roca= pygame.image.load('media/Imagenes/roca.png') 
	 temX=0
	 temY=0
	 for i in range (self.posicionImpresion[1],self.posicionImpresion[1]+20):
		 for j in range (self.posicionImpresion[0],self.posicionImpresion[0]+18):
			 screen.blit(hierba,(temX*self.anchoImpresion,temY*self.altoImpresion))
				
				
			 if  self.MatrizLogica[i][j] == 1:
				 screen.blit(arbol,(temX*self.anchoImpresion,temY*self.altoImpresion))
				
			 elif  self.MatrizLogica[i][j] == 2:
				 screen.blit(roca,(temX*self.anchoImpresion,temY*self.altoImpresion))
				 
			 
			 
			 temX +=1
		
		 temX = 0	 
		 temY +=1
	
	 temX=0
	 temY=0	 
	 for i in range (self.posicionImpresion[1],self.posicionImpresion[1]+20):
		  for j in range (self.posicionImpresion[0],self.posicionImpresion[0]+18):
			   if  self.MatrizLogica[i][j] == 3:
				   screen.blit(self.ListaImagenes[0],(temX*self.anchoImpresion,temY*self.altoImpresion))
			   if  self.MatrizLogica[i][j] == 4:
				   screen.blit(self.ListaImagenes[1],(temX*self.anchoImpresion,temY*self.altoImpresion))

			   if  self.MatrizLogica[i][j] == 5:
				   screen.blit(self.ListaImagenes[2],(temX*self.anchoImpresion,temY*self.altoImpresion))   
			      
			   temX +=1 
		  temX = 0	 
		  temY +=1	 	
	
				     	 
				
					

class MapaEventos(IEstrategiaAnimaciones):
	def __init__(self):
		d=500	
		self.MapaVida=[[0 for x in range(d)] for y in range(d)]
		self.ListRect = []
		




def main():

	
	Madera = 1000
	Roca = 1000
	Comida = 1000
	inicio = time.time()
	posX=0
	posY=0
	pygame.init()
	screen = pygame.display.set_mode((1120,640), pygame.RESIZABLE)
	pygame.display.get_caption()
	principal_personaje = personaje(3,0,1,2,45,64,2,[posX,posY],'kono.png', 1)
	mapa1 = MapaEstandar(screen)
	mapa2 = MapaEventos()
	
	
	Rect = pygame.Rect(0,0,10,10)
	principal_personaje.getSpawn(mapa1)
	personajes = []
	Botones = []
	Orda1 = Orda(personajes)
	
	

	Botones.append (boton(">",50,170,[835,180],screen))
	Botones.append ( boton("<",50,170,[835,260],screen))
	Botones.append(boton("Abajo",50,170,[835,320],screen))
	Botones.append(boton("Arriba",50,170,[835,390],screen))
	btn = botonConstruir("Construir",50,170,[835,120],screen)
	personajes.append(principal_personaje)
	m = Mouse()
	mediator = mediadorLogico(mapa1,mapa2,Orda1, Botones)
	mediator.generarMateriales()	
	mediator.crearLogicaRestrictiva()
	fuente1=pygame.font.Font(None,40)
		
	mediator.actualizacion()
	while(True):
		tiempoEjecucion =round( time.time() - inicio)
		mediator.mediarImpresionPersonajes()
		mediator.mediarEstado()
		mediator.mediarBotones()
  

		for evento in pygame.event.get():
			
			
			if evento.type == 12:

				for i in mediator.Personajes:
					i.c=False
				mediator.c=False
				sys.exit(0)
				
		
		
		
		pygame.display.flip()
		pygame.display.update()	
		screen.fill((0,0,0))	
		screen.blit(pygame.image.load('media/Imagenes/madera.png'),(835,0))
		screen.blit(pygame.image.load('media/Imagenes/metal.png'),(835,55))
		screen.blit(fuente1.render("x"+ str(mediator.Madera),0,(255,255,255)) ,(885,0))
		screen.blit(fuente1.render("x"+ str(mediator.Roca) ,0,(255,255,255)) ,(885, 55))
		mediator.mediarConstruccion(Madera,Roca,btn)
		
		
	return 0 

main()









 
