from tkinter import *
import sqlite3 as sql
import datetime
from datetime import datetime as DateTime, timedelta as TimeDelta


root=Tk()
root.title("Base de Datos ")
root.geometry("792x500")
# funciones del menu bar ---------------------------------------------------------
def donothing():
    pass

# Menu Bar -----------------------------------------------------------------------
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

#botones de Ventanas -----------------------------------------------------------------------

datos = StringVar()
Lb1 = StringVar()
today_date = datetime.date.today()
Label(text=today_date,font=("Algerian",15)).place(x=5,y=15)
Label(text="Cedula o Pasaporte :",font=("Algerian",15)).place(x=5,y=40)
identificador = StringVar()
id_box = Entry(textvariable=identificador).place(width=140,x=160,y=40)

#Funciones del programa --------------------------------------------------------------------
def createDB():
    conn = sql.connect("database_sell.db")
    conn.commit()
    conn.close()
    
def createTable():
    conn = sql.connect("database_sell.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE ventas (
            identificador text,
            fecha_venta text,
            fecha_proxima text
        )"""
    )
    conn.commit()
    conn.close()



def verificar():
    #codigo para verificar
    var1=str()
    fecha_1=str()
    fecha_3=str()
    ide = identificador.get()
    print("el valor a buscar:",ide)
    conn = sql.connect("database_sell.db")
    cursor = conn.cursor()
    instruccion = f" SELECT * FROM ventas WHERE identificador='{ide}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    for i in datos:
        print(i[0]+"    "+str(i[1])+"    "+str(i[2]))
        var1=i[0]
        fecha_1=str(i[1])
        fecha_3=str(i[2])
    
    Label(text=var1,font=("Algerian",15)).place(x=5,y=90)
    Label(text=fecha_1,font=("Algerian",15)).place(x=160,y=90)
    Label(text=fecha_3,font=("Algerian",15)).place(x=260,y=90)
    
    Label(text=rest,font=("Algerian",15)).place(x=350,y=90)
    print(datos)
    conn.close()
    
def vender():
    #codigo para verificar
    id = str(identificador.get())
    fecha_1 =today_date
    end_date = today_date + TimeDelta(days=7)
    conn = sql.connect("database_sell.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO ventas Values ('{id}','{fecha_1}','{end_date}' )"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    #print(id,fecha_1,fecha_2)
    
def readRows():
    conn = sql.connect("database_sell.db")
    cursor = conn.cursor()
    instruccion = f" SELECT * FROM ventas"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    #Lb1 = Listbox(root,width=50,height=20)
    #for i in datos:
    #    print(i[0]+"    "+str(i[1])+"    "+str(i[2]))
    #    val1=i[0]
    #    val2=str(i[1])
    #    val3=str(i[2])
     #   total=val1 +val2 +val3
    #    Lb1.insert("1",total)
    #Lb1.place(x=60,y=100)
    conn.close()
    print(datos)
    
    #listbox.set(datos)
    #Lb1 = Listbox(ventana)
    #Lb1.insert("",datos,"")
    #Lb1.pack()
    #Lb1.place(x=60,y=100)
    
    
#Funcion principal despues de cargar la ventana  -----------------------------------------------    
if __name__ == '__main__':
        
    #createDB()
    #createTable()
    readRows()

    
    
    Button(root,text="Verificar",bg="blue",width=10,height=1,command=verificar).place(x=310,y=30)
    b2 = Button(text="Vender", bg="gray",width=10,height=1, command=vender).place(x=460,y=30)
    


root.mainloop()
