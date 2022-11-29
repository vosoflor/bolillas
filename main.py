import pygame as pg
from figura import Rectangulo, Circulo
import random 

#Inicializar todos los módulos de pygame (Pantalla, sonidos, teclados, etc)
pg.init()

#Creamos pantalla o surface para trabajar
pantalla_principal = pg.display.set_mode( (800,600) ) #ventana y tamaño de ventana
pg.display.set_caption("Bolillas juguetonas") #título de la ventana

game_over = False #Variable para controlar bucle
figuras = []

for i in range(1,26):
    figuras.append(Rectangulo((random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                                    random.randint(0, pantalla_principal.get_width()),
                                    random.randint(0, pantalla_principal.get_height()),
                                    random.randint(1, 20),
                                    random.randint(1, 20),
                                    random.uniform(0.2, 1.0),
                                    random.uniform(0.2, 1.0)))
    figuras.append(Circulo((random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                                    random.randint(0, pantalla_principal.get_width()),
                                    random.randint(0, pantalla_principal.get_height()),
                                    random.randint(1, 20),
                                    random.uniform(0.2, 1.0),
                                    random.uniform(0.2, 1.0)))

while not game_over: #Bucle para ejecutar los fotogramas para el repintado de pantalla
    
    for eventos in pg.event.get(): #Captura todos los eventos en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
        
    pantalla_principal.fill( (52,152,219) ) #Asignar color a la pantalla con formato de color RGB
    
    for figura in figuras:
        figura.mover(pantalla_principal.get_width(), pantalla_principal.get_height())
        figura.dibujar(pantalla_principal)
    
    pg.display.flip() #Método que añade a la pantalla los recursos que se van incluyendo
        
pg.quit()
