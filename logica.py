import time
import pygame,sys,random
from personaje import *
from aura import *
import threading
from materiales import *
import math
from fabricas import *
		
		
class mediadorLogico:
	def __init__(self, Mapa, MapaLogico, Orda, Botones):
		self.index = 0
		self.Mapa = Mapa
		self.MapaLogico = MapaLogico
		self.Personajes = Orda.personajes
		self.Botones = Botones
		self.ListaMateriales = []
		self.ListaFabricas = []
		self.ListaPersonajesRect = []
		for i in self.Personajes:
			self.ListaPersonajesRect.append(i.Rectangulo)
			
		self.Cursor = Mouse()
		self.Orda = Orda	
		self.nivel = 1

		
	def actualizacion():
		Mapa.MatrizLogica =	Mapa.MatrizLogica2
		 
	def generarMateriales(self):
		for j in range (0,1500):
		  for i in range (1,3):
		    x = random.randint(3,480)
		    y = random.randint(3,480)
		    self.Mapa.MatrizLogica[y][x] = i
		    self.Mapa.MatrizLogica[y+1][x] = i
		    self.Mapa.MatrizLogica[y][x+1] = i
		    self.Mapa.MatrizLogica[y+1][x+1] = i
		    self.Mapa.MatrizLogica[y+2][x] = i
		    self.Mapa.MatrizLogica[y][x+2] = i
		    self.Mapa.MatrizLogica[y+2][x+2] = i
	
	def crearLogicaRestrictiva(self):
		
		temp = None
		for i in range (0,self.Mapa.dimension):
		
		   for j in range (0,self.Mapa.dimension):
			   self.MapaLogico.MapaVida [i][j] =0
			   if self.Mapa.MatrizLogica[i][j] ==1:
				   temp = Arbol()
				   self.MapaLogico.MapaVida [i][j] = 1
				   self.ListaMateriales.append(temp)
				   temp.Rectangulo =pygame.Rect(j*46,i*64,46,64)
				   self.MapaLogico.ListRect.append(temp.Rectangulo)
				   temp.setPosicion(j,i)	  
			   
			   if self.Mapa.MatrizLogica[i][j]==2:
				   
				   temp = Roca()
				   self.MapaLogico.MapaVida [i][j] = 2
				   self.ListaMateriales.append(temp)
				   temp.Rectangulo =pygame.Rect(j*46,i*64,46,64)
				   self.MapaLogico.ListRect.append(temp.Rectangulo)
				   temp.setPosicion(j,i)
	
	def mediarImpresionPersonajes(self):
	   self.Mapa.imprimirMapa(self.Mapa.screen)
	   
	   i = self.Personajes[self.index]
		   
	   elem = i.movimiento(self.MapaLogico)
	   self.Mapa.screen.blit(elem[0],elem[1],(elem[2],elem[3],elem[4],elem[5]))
		   
		   
	   if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] < 820:
			   i.setPosicionDestino(pygame.mouse.get_pos())
			
			   if i.Rectangulo.collidelist(self.MapaLogico.ListRect) != -1:
				   i.setPosicionDestino(i.posicionInicial)
				   
				   
	   for j in self.Personajes:
		   elem = j.Impresion
		   self.Mapa.screen.blit(elem[0],elem[1],(elem[2],elem[3],elem[4],elem[5]))
		   		   
	   			   
	
	def mediarEstado(self):
		if pygame.mouse.get_pressed()[0]==1:
		  R = Recolectando()	
		  a = pygame.mouse.get_pos()	
		  for i in self.Personajes:
			  if i.Rectangulo.collidepoint(a):
				  
				  R.actuar(i)
				  R = Construyendo()
				  R.actuar(i)
				  R = Atacando() 
				  R.actuar(i)
				  				  
	def mediarBotones(self):
		for i in self.Botones:
			i.setBoton()
			if(i.presionado()):
				for j in self.Personajes:
					self.Mapa.moverMapa(self.Botones.index(i),j)
					self.Mapa.imprimirMapa(self.Mapa.screen)
					time.sleep(0.05)
		
		
	def mediarMaterialesMadera(self, Madera):
		temp = None
		for i in self.Personajes:
			
			if (i.Rectangulo.collidelist(self.MapaLogico.ListRect) != -1):
				temp = self.ListaMateriales[i.Rectangulo.collidelist(self.MapaLogico.ListRect)]
				if self.MapaLogico.MapaVida [temp.y][temp.x]==1:
					Madera += temp.perderVida()
					
					
				
					
		return Madera
			
	def mediarMaterialesRoca(self,Roca):
		temp = None
		for i in self.Personajes:
			if (i.Rectangulo.collidelist(self.MapaLogico.ListRect) != -1):
				temp = self.ListaMateriales[i.Rectangulo.collidelist(self.MapaLogico.ListRect)]
				if self.MapaLogico.MapaVida [temp.y][temp.x]==2:
					Roca += temp.perderVida() 
					
		for i in self.ListaMateriales:
			if i.vida <=0:
				self.MapaLogico.ListRect.remove(i.Rectangulo)
				self.MapaLogico.MapaVida [i.y][i.x]=0
				self.Mapa.MatrizLogica [i.y][i.x]=0
				self.ListaMateriales.remove(i)
					
				
					
		return Roca		
					
	def mediarConstruccion(self, Madera, Roca, Boton):
		Obreros = pygame.image.load('media/Obreros.png')
		Fabrica = None
		Boton.setBoton()
		Fabrica = Boton.presionado(Madera,Roca)
		if Fabrica != None:
			Fabrica.setRectangulo(getPosicion(pygame.Rect(self.Mapa.posicionImpresion[0]*46,self.Mapa.posicionImpresion[1]*64,135,128),0,self.MapaLogico.ListRect))
			#self.MapaLogico.ListRect.append(Fabrica.Rect)
			self.Mapa.MatrizLogica[int(Fabrica.Rect.top/64)] [int (Fabrica.Rect.left/46)] = Fabrica.Identificacion 
			self.ListaFabricas.append([Obreros,Fabrica.Rect.left,Fabrica.Rect.top])
			self.Mapa.imprimirMapa(self.Mapa.screen)
			Fabrica.crear(self.nivel,self.ListaPersonajesRect, self.Personajes)
			self.nivel +=1
			if self.nivel == 2 :
				Visitor.VisitorPersonajes(self.Personajes)
				Visitor.VisitorCasa(self.Mapa)
			if	self.nivel == 3:
				Visitor.VisitorPersonajes2(self.Personajes)
			
	def llevarIndex(self):
		
		for i in pygame.key.get_pressed():
			if i==1:
				if 49 <= pygame.key.get_pressed().index(i) <=57 and len(self.Personajes) >= pygame.key.get_pressed().index(i)-48:
					self.index = pygame.key.get_pressed().index(i)-49
					
				
			
		
		
			    
				  
					

			   




class IEstadoPersonaje:
	def actuar(self,personaje):
		pass



class Recolectando(IEstadoPersonaje):
	
	def actuar (self,personaje):
		print ("soldado en posicion: " + str(personaje.posicionInicial) + " 	Recolectando materiales" )
		


class Atacando(IEstadoPersonaje):
	
	def actuar (self,personaje):
		print ("soldado en posicion: " + str(personaje.posicionInicial) + " Atacando" )



class Construyendo(IEstadoPersonaje):
	
	def actuar (self, personaje):
		print ("soldado en posicion: " + str(personaje.posicionInicial) + " Construyendo" )



def getPosicion(Rectangulo, iteracion,Lista ):
	tempLeft =Rectangulo.left
	y = math.ceil(iteracion/4)
	if (Rectangulo.collidelist(Lista) != -1):
		Rectangulo.left +=46
		
		if ((Rectangulo.left-tempLeft)/46 > 4):
			iteracion  += 1
		Rectangulo.top += (iteracion*64)
		Rectangulo = getPosicion(Rectangulo,iteracion,Lista)
		
	
	return Rectangulo

