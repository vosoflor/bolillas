import pygame as pg

#Inicializar todos los módulos de pygame (Pantalla, sonidos, teclados, etc)
pg.init()

#Creamos pantalla o surface para trabajar
pantalla_principal = pg.display.set_mode( (800,600) ) #ventana y tamaño de ventana
pg.display.set_caption("Bolillas juguetonas") #título de la ventana

game_over = False #Variable para controlar bucle

while not game_over: #Bucle para ejecutar los fotogramas para el repintado de pantalla
    for eventos in pg.event.get(): #Captura todos los eventos en forma de lista
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
        
        pantalla_principal.fill( (52,152,219) ) #Asignar color a la pantalla con formato de color RGB
        pg.draw.rect(pantalla_principal,(192,57,43), (400-10,300-10,20,20)) #Se agrega rectángulo a la pantalla y los parámetros entregados son pantalla, color, ubicación y tamaño (ancho ubicación, alto uubicación, ancho tamaño, alto tamaño)
        pg.display.flip() #Método que añade a la pantalla los recursos que se van incluyendo

pg.quit()
