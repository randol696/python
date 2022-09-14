from tkinter import *
ventana = Tk()
ventana.geometry("370x120")
ventana.config(bg="whitesmoke")
ventana.title("CALCULADORA DE PROMEDIOS FINALES")

ancho_boton=9
alto_boton=3
color_boton=("gray75")

resultado=0
numero1 = IntVar()
numero2 = IntVar()

def calcular():
   a= int(numero1.get())
   b= int(numero2.get())
   resultado = ((b / a)* 4+1)
   resultado = str(round(resultado, 3))
   Label(text=resultado,font=("Broadway",15),fg="blue").place(width=130,x=120,y=90)
   
   

#VISUALIZAR LA OPERACION EN LA PANTALLA
titulo = Label(text="CALCULADORA PROMEDIO",font=("Algerian",15)).place(x=150,y=0)
Label(text="Base de puntaje",font=("Algerian",15)).place(x=1,y=30)
Label(text="Puntaje obtenido",font=("Algerian",15)).place(x=1,y=60)
Label(text="Resultado",font=("Algerian",15)).place(x=1,y=90)
nu1 = Entry(textvariable=numero1,bg=color_boton).place(width=130,x=120,y=30)
nu2 = Entry(textvariable=numero2).place(width=130,x=120,y=60)
Button(ventana,text="Calcular",bg=color_boton,width=ancho_boton,height=alto_boton,command=calcular).place(x=250,y=30)

ventana.mainloop()