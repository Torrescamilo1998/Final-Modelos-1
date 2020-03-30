import pygame,sys
from time import sleep 
from logica import *
from personaje import *
ruta = 'media/Imagenes/Sprites/'

class Ifabrica():
	def __init__(self):
		pass
	
	def getSoldado(self, nivel):
		pass
		
	def getObrero(self, nivel):
		pass	



class fabricaSoldado(Ifabrica):
	def __init__(self):
		Ifabrica.__init__(self)
	
	
	def getSoldado(self, nivel):
		if (nivel == 1):
			return personaje(3,0,1,2,45,64,3,[0,0],'naruto.png',2)
			
		if (nivel == 2):
			return personaje(3,0,1,2,45,64,3,[0,0],'sasuke.png',2)
			
		if (nivel == 3):
			return personaje(3,0,1,2,45,64,3,[0,0],'pain.png',2)
	

class fabricaObrero(Ifabrica):
	def __init__(self):
		Ifabrica.__init__(self)
	
	def getObrero(self,nivel):
		if (nivel == 1):
			return personaje(3,0,1,2,45,64,2,[0,0],'kono.png',1)
			
		if (nivel == 2):
			return personaje(3,0,1,2,45,64,3,[0,0],'gaara.png',1)
			
		if (nivel == 3):
			return personaje(3,0,1,2,45,64,3,[0,0],'naruto-pro.png',1)
		

class casa:
	def __init__(self):
		self.costeMadera  = 1000
		self.costeRoca = 1000
		self.posicion = []
		self.Rect = None
		
	def setRectangulo(self, Rectangulo):
		    print (Rectangulo)
		    self.Rect = Rectangulo
		    self.posicion = [self.Rect.left, self.Rect.top]  


class casaObreros (casa):
	
	def __init__(self):
		casa.__init__(self)
		self.Imagen = pygame.image.load('media/Obreros.png')
		self.Identificacion =3 
	def crear(self, nivel,ListaPersonajes,Lista):
		F = fabricaObrero()
		a=None
		for i in range (0,2):
			a = F.getObrero(nivel)
			a.Rectangulo = pygame.Rect(self.posicion[0],self.posicion[1]+128,20,20)
			a.setPosicionDestino((a.Rectangulo.left/46,a.Rectangulo.top/64))
			ListaPersonajes.append(a.Rectangulo)
			Lista.append(a)
		
	
		
class casaSoldados (casa):
	def __init__(self):
		casa.__init__(self)
		self.Imagen = pygame.image.load('media/Soldados.png')
		self.Identificacion = 4
	def crear(self, nivel,ListaPersonajes,Lista):
		F = fabricaSoldado()
		a=None
		for i in range (0,3):
			a = F.getSoldado(nivel)
			a.Rectangulo = pygame.Rect(self.posicion[0],self.posicion[1]+128,20,20)
			a.setPosicionDestino((a.Rectangulo.left/46,a.Rectangulo.top/64))
			ListaPersonajes.append(a.Rectangulo)
			Lista.append(a)
	 
		





class proxyConstrucion:
	def __init__(self, Madera, Roca, screen):
		self.Madera = Madera
		self.Roca = Roca
		self.screen = screen
	
	def Construir(self):
		obreros = pygame.image.load('media/Obreros.png')
		soldados = pygame.image.load('media/Soldados.png')
		self.screen = pygame.display.set_mode((300,300), pygame.RESIZABLE)
		FabricaTemporal = None
		c=True
		while(c):
			self.screen.blit(obreros,(10,10))
			self.screen.blit(soldados,(155,10))
			for evento in pygame.event.get():
				
				if evento.type == 12:
					c=False
				if presionado(self.screen, [10,10]):
					c=False 
					FabricaTemporal = casaObreros() 
					
					if (self.Madera < FabricaTemporal.costeMadera or self.Roca < FabricaTemporal.costeRoca):
						FabricaTemporal = None
					
				if presionado(self.screen, [155,10]):
					c=False	
					FabricaTemporal = casaSoldados()
					if (self.Madera < FabricaTemporal.costeMadera or self.Roca < FabricaTemporal.costeRoca):
						FabricaTemporal = None
				pygame.display.flip()
				pygame.display.update()				
		
		pygame.display.set_mode((1120,640), pygame.RESIZABLE)
		return FabricaTemporal



def presionado(screen, pos):
	if pygame.mouse.get_pressed()[0]==1 and pygame.Rect(pos[0],pos[1],135,128).collidepoint(pygame.mouse.get_pos())==1:
			return True
			
	else:
			return False




class Visitor:
	
	
	def VisitorPersonajes(Lista):
		for i in Lista:
			if i.iden ==1:
				i.imagen =pygame.image.load (ruta + 'gaara.png')
				
			else:
				i.skin = pygame.image.load (ruta + 'sasuke.png')
				
				
	def VisitorPersonajes2(Lista):
		for i in Lista:
			if i.iden ==1:
				i.imagen =pygame.image.load (ruta + 'naruto-pro.png')
				
			else:
				i.skin = pygame.image.load (ruta + 'pain.png')
				
				
	def VisitorCasa (Mapa):
		Mapa.ListaImagenes[0] = pygame.image.load('media/Obreros2.png')
		Mapa.ListaImagenes[1] = pygame.image.load('media/Soldados2.png')
			
