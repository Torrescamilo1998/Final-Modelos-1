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
		self.PersonajesTotales = Orda.personajes
		self.Botones = Botones
		self.ListaMateriales = []
		self.ListaFabricas = []
		self.ListaPersonajesRect = []
		self.c = True
		for i in self.Personajes:
			self.ListaPersonajesRect.append(i.Rectangulo)

		self.Madera = 1000
		self.Roca =1000	
		self.Cursor = Mouse()
		self.Orda = Orda	
		self.nivel = 1
		self.hilos = []
		self.hilos.append(threading.Thread(target=self.mediarMateriales))
		for j in self.Personajes:
			self.hilos.append(threading.Thread(target=j.movimiento,args=(self.MapaLogico,)))
		

		
	def actualizacion(self):
		self.hilos = []
		self.hilos.append(threading.Thread(target=self.mediarMateriales))
		for i in self.Personajes:
			self.hilos.append(threading.Thread(target=i.movimiento,args=(self.MapaLogico,)))
		for j  in self.hilos:
		   j.start()

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
	   

	   for j in self.Personajes:
		   if pygame.mouse.get_pressed()[0]==1 and pygame.mouse.get_pos()[0] < 820:
			   j.setPosicionDestino(pygame.mouse.get_pos())
		   elem = j.Impresion
		   self.Mapa.screen.blit(elem[0],elem[1],(elem[2],elem[3],elem[4],elem[5]))
		   #pygame.draw.rect(self.Mapa.screen,(255,255,255),j.Rectangulo)

	   #for j in self.MapaLogico.ListRect:
		#   pygame.draw.rect(self.Mapa.screen,(255,255,255),j)
		   

	   

	"""   
	  i = self.Personajes[self.index]
		   
	   elem = i.movimiento(self.MapaLogico)
	   self.Mapa.screen.blit(elem[0],elem[1],(elem[2],elem[3],elem[4],elem[5]))
		"""      		   
	   			   
	
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
					self.Mapa.moverMapa(self.Botones.index(i),self.MapaLogico.ListRect)
					self.Mapa.imprimirMapa(self.Mapa.screen)
					
					self.organizar()

			
		
		
	def mediarMateriales(self):
		while (self.c):

		  temp = None
		  for i in self.Personajes:
			  if (i.Rectangulo.collidelist(self.MapaLogico.ListRect) != -1):
				  decorador.decorarEstado(self.Mapa.screen,i)
				  sleep(0.5)
				  temp = self.ListaMateriales[i.Rectangulo.collidelist(self.MapaLogico.ListRect)]
				  if self.MapaLogico.MapaVida [temp.y][temp.x]==1:
					  self.Madera += temp.perderVida()

				  if self.MapaLogico.MapaVida [temp.y][temp.x]==2:
					  self.Roca += temp.perderVida()

				  if temp.vida <=0:
					   self.MapaLogico.ListRect.remove(temp.Rectangulo)
					   self.MapaLogico.MapaVida [temp.y][temp.x]=0
					   self.Mapa.MatrizLogica [temp.y][temp.x] = 0
					   self.ListaMateriales.remove(temp) 
							

					
		  
					
				
						
					
	def mediarConstruccion(self, Madera, Roca, Boton):
		Obreros = pygame.image.load('media/Obreros.png')
		Fabrica = None
		Boton.setBoton()
		Fabrica = Boton.presionado(self.Madera,self.Roca)
		if Fabrica != None:
			Fabrica.setRectangulo(getPosicion(pygame.Rect(self.Mapa.posicionImpresion[0]*46,self.Mapa.posicionImpresion[1]*64,135,128),0,self.MapaLogico.ListRect))
			Fabrica.setRectangulo(getPosicion(pygame.Rect(self.Mapa.posicionImpresion[0]*46,self.Mapa.posicionImpresion[1]*64,135,128),0,self.ListaFabricas))
			self.ListaFabricas.append(Fabrica.Rect)
			
			self.Mapa.MatrizLogica[int(Fabrica.Rect.top/64)] [int (Fabrica.Rect.left/46)] = Fabrica.Identificacion 
			self.Mapa.imprimirMapa(self.Mapa.screen)
			Fabrica.crear(self.nivel,self.ListaPersonajesRect, self.Personajes)
			self.nivel +=1
			if self.nivel == 2 :
				Visitor.VisitorPersonajes(self.Personajes)
				Visitor.VisitorCasa(self.Mapa)
			if	self.nivel == 3:
				Visitor.VisitorPersonajes2(self.Personajes)
			self.actualizacion()
			#self.organizar()
			self.mediarImpresionPersonajes()	
			
	def llevarIndex(self):
		
		for i in pygame.key.get_pressed():
			if i==1:
				if 49 <= pygame.key.get_pressed().index(i) <=57 and len(self.Personajes) >= pygame.key.get_pressed().index(i)-48:
					self.index = pygame.key.get_pressed().index(i)-49
					
	def limpiar(self):
		for i in self.ListaMateriales:
			  if i.vida <=0:
				  self.MapaLogico.ListRect.remove(i.Rectangulo)
				  self.MapaLogico.MapaVida [i.y][i.x]=0
				  self.Mapa.MatrizLogica [i.y][i.x]=0
				  self.ListaMateriales.remove(i)

	def organizar(self):
		for i in self.Personajes:
			for j in self.Personajes:
				#print ( i.posicionInicial == j.posicionInicial)
				if ( i.posicionInicial == j.posicionInicial):
						 
						i.setPosicionDestino([i.posicionInicial[0]+(46*self.Personajes.index(i)),i.posicionInicial[1]])
						print(i.posicionInicial)

			if i.Rectangulo.collidelist(self.ListaFabricas) !=-1:
				i.posicionInicial = [i.posicionInicial[0]+46,i.posicionInicial[1]]
				i.setPosicionDestino(i.posicionInicial)

						




		
		
			    
				  
					

			   




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





