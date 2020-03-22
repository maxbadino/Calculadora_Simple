from tkinter import *


root= Tk()
root.geometry("420x500")
root.config(bd=20)
####################################################################
def sumar():
    r.set( float(n1.get()) + float(n2.get()) )
    borrar()

def resta():
    r.set( float(n1.get()) - float(n2.get()) )
    borrar()

def producto():
    r.set( float(n1.get()) * float(n2.get()) )
    borrar()

def division():
    r.set( float(n1.get()) / float(n2.get()) )
    borrar()

def borrar():
    n1.set("")
    n2.set("")
#######################################################################

n1 = StringVar()
n2 = StringVar()
r = StringVar()

imagen=PhotoImage(file="1.gif")
fondo=Label (root,image=imagen).pack()

etiqueta = Label(text = "Calcu Max")
etiqueta.pack()
etiqueta.config(font=("Verdana",18))

Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r).pack()

Label(root, text="").pack()  # Separador

Button(root, text="Sumar", command=sumar).pack()
Button(root, text="Resta", command=resta).pack()
Button(root, text="Producto", command=producto).pack()
Button(root, text="División", command=division).pack()


root.mainloop()