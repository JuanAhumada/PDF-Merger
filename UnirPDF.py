import PyPDF2
import os
from tkinter import *
from tkinter import messagebox

##Lista que almacenara los paths de pdfs##
Archivos = []

##Metodo de combinacion##
def Unificador():
    if entrada.get() != "":
        if len(os.listdir("PDFs Separados")) != 0:
            con = 0
            ##Ciclo para examinar cada elemento de la carpeta##
            for i in os.scandir("PDFs Separados"):
                ##Ver si es un archivo##
                if i.is_file():
                    x = f"{i.path}"
                    ##Selector de pdfs##
                    if x[-3:] == "pdf":
                        Archivos.append(x)
                        con += 1
            ##Evitar que cree un nuevo pdf si no hay pdfs##
            if con == 0:
                messagebox.showerror("Sin elementos","No contiene ningun pdf")
            ##Evitar que cree un nuevo pdf si solo hay un pdf##
            elif con == 1:
                messagebox.showerror("Solo un pdf","Esta carpeta solo tiene un pdf, asi que no puede combinar")
            else:
                ##Ruta del archivo final##
                salida = "PDFs Combinados/"+ entrada.get() +".pdf"
                
                ##Verificar si ese archivo existe para no sobreescribirlo##
                if not os.path.isdir(salida):

                    ##Funcion de combinar##
                    pdf = PyPDF2.PdfMerger()

                    ##Añadir cada pdf al archivo final##
                    for archivo in Archivos:
                        pdf.append(archivo)
                    
                    
                    ##Dar nombre al archivo final##
                    pdf.write(salida)
                    
                    ##Cerrar el pdf##
                    pdf.close()
                    messagebox.showinfo("Exito", f"El Archivo {entrada.get()}.pdf ha sido creado existosamente")
                else:
                    messagebox.showerror("Archivo existente","El archivo ya existe, cambia el nombre")
        else:
            messagebox.showerror("Sin elementos","La carpeta esta vacia, por favor añada elementos y reintente")
    else:
        messagebox.showerror("Sin Nombre","Asigne nombre para el nuevo pdf")
        
##Creacion de la mini interfaz Grafica TK##
box = Tk()
box.resizable(0,0)
box.title("Combinador de PDFs")

##Creacion del Frame##
v = Frame(box)
v.pack()

##Creacion de Widgets##
w = Label(v, text="Nombre Que le colocara al nuevo archivo: ")
w.grid(row=0)
entrada = Entry(v)
entrada.grid(row=1)
boton = Button(v, text="Crear Archivo", command=Unificador)
boton.grid(row = 2)

##Separador de widgets##
for widget in v.winfo_children():
        widget.grid_configure(padx = 10, pady = 5)
        
##Loop principal##
box.mainloop()