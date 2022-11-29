import pygame as pg

class Rectangulo():
    def __init__(self, color, posx, posy, tamañox, tamañoy, saltox, saltoy):
        self.color = color
        self.x = posx
        self.y = posy
        self.ancho = tamañox
        self.alto = tamañoy
        self.velocidadx = saltox
        self.velocidady = saltoy
    
    def mover(self, anchoPantalla, altoPantalla):

        self.x += self.velocidadx
        self.y += self.velocidady

        if self.x + self.ancho >= anchoPantalla or self.x <= 0:
            self.velocidadx *= -1
        if self.y + self.alto >= altoPantalla or self.y <= 0:
            self.velocidady *= -1
    
    def dibujar(self, pantalla):
        pg.draw.rect(pantalla,self.color,(self.x,self.y,self.ancho,self.alto)) #Se agrega rectángulo a la pantalla y los parámetros entregados son pantalla, color, ubicación y tamaño (ancho ubicación, alto uubicación, ancho tamaño, alto tamaño)

class Circulo():
    def __init__(self, color, posx, posy, radio, saltox, saltoy):
        self.color = color
        self.x = posx
        self.y = posy
        self.radio = radio
        self.velocidadx = saltox
        self.velocidady = saltoy

    def mover(self, anchoPantalla, altoPantalla):

        self.x += self.velocidadx
        self.y += self.velocidady

        if self.x + self.radio >= anchoPantalla or self.x - self.radio <= 0:
            self.velocidadx *= -1
        if self.y + self.radio >= altoPantalla or self.y - self.radio <= 0:
            self.velocidady *= -1

    def dibujar(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)