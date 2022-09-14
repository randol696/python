import random2
from tkinter import *
ventana = Tk()
ventana.geometry("470x220")
ventana.config(bg="whitesmoke")
ventana.title("Room Test")
ancho_boton=9
alto_boton=3
color_boton=("gray75")

movies_list = ['Ahir Ahir Henil',
'Ahir Ahir Mihir Arvind',
'Ahir Herry Hiteshbhai',
'Armelino Rivera Israel Nicolas',
'Baso Jaen Alex Gabriel',
'Batista Rivera Montserrat Johana',
'Carmona Guillen Maria Gabriela',
'Castillo Diaz Ariel Augusto',
'Chong Feng Ricardo Joe',
'Concepción Macías Diego Alejandro',
'Duran De Gracia Librada Del Carmen',
'Erne Athanasiadis Jorge Alexis',
'Lopez Ledezma Renata Marcela',
'Monterrey Correa Ana Daniela',
'Murillo Quijada Ilzedith Alejandra',
'Pan Luo Daniel Jonathan',
'Polo Arosemena Juan Pablo',
'Pul Liu Terry',
'Reyes Vergara Gabriela Lucia',
'Rodriguez Norato Andre Enrique',
'Sarasqueta Castillo Yanina Yarelis',
'Serrano Diana Rosa',
'Valdivieso Da Silva Paulo Cesar',
'Vera Morales Angelice',
'Villarreal Batista Gustavo Shemuel',
'Villarreal Isabella Nicole',
'Young Parbhu Gabriel Alexander',]





def calcular():
    
    for i in range(1):
        movie = random2.choice(movies_list)
        print(i,"Estudiante...:",movie)
        Label(text=movie,font=("Broadway",15),fg="blue").place(width=330,x=120,y=100)
        

Button(ventana,text="Random List",bg=color_boton,width=ancho_boton,height=alto_boton,command=calcular).place(x=150,y=30)
    
ventana.mainloop()