#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from math import *

ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")
ventana.configure(background="gray")
color_boton=("gray20")

#DEFINIMOS LAS DIMENSIONES DE LOS BOTONES
ancho_boton=11
alto_boton=3
input_text=StringVar()

#VISUALIZAR LA OPERACION EN LA PANTALLA
def btnClik(num):
    input_text.set(num)

#LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador=("")
    input_text.set("0")
    

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=2,insertwidth=4,bg="yellow",justify="right")
Salida.place(x=10,y=60)
#CREAMOS NUESTROS BOTONES
boton0=Button(ventana,text="Calcular", width=ancho_boton,height=alto_boton).place(x=17,y=180)
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=20,y=200)
 
clear()
ventana.mainloop()
