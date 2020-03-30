import random
import pygame
 
pygame.init()



def main():
	

		screen = pygame.display.set_mode((300,300), pygame.RESIZABLE)
		c=True
		while(c):
			for i in pygame.key.get_pressed():
				if i == 1:
					print (pygame.key.get_pressed().index(i))
					
					
					
			for evento in pygame.event.get():
				
				if evento.type == 12:
					c=False 
					
					
			pygame.display.flip()
			pygame.display.update()
 


	
main()
