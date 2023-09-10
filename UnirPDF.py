## Librerias Usadas##
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PyPDF2
import os
def main():
    
    ##Lista que almacenara los paths de pdfs##
    Archivos = []

    def Actualizar():
        separados = ""
        for i in Archivos:
            separados += i+"\n"
        NombresRutas.delete(0.0,END)
        NombresRutas.insert(END, separados)
        for widget in v.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)
    
    ##Metodo de combinacion##
    def Unificador(nombre:str):
        if nombre != "":
            ##Ruta del archivo final##
            salida = nombre +".pdf"    
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
                    messagebox.showinfo("Exito", f"El Archivo {nombre}.pdf ha sido creado existosamente")
            else:
                messagebox.showerror("Archivo existente","El archivo ya existe, cambia el nombre")
        else:
            messagebox.showerror("Sin Nombre","Asigne nombre para el nuevo pdf")

    def Buscar():
        global Archivosstr
        ##Buscador de archivos##
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        pdf_path = os.path.abspath(file_path)
        if pdf_path[-4:] == ".pdf":
            if str(pdf_path) in Archivos:
                messagebox.showerror("Archivo existente","El archivo ya esta en la lista")
            else:
                Archivos.append(str(pdf_path))
                Actualizar()
                
    def Quitar():
        pass
    
    def Borrar():
        Archivos.clear()
        Actualizar()
    ##Creacion de la mini interfaz Grafica TK##
    box = Tk()
    box.resizable(0,0)
    box.title("Combinador de PDFs")

    ##Creacion del Frame##
    v = Frame(box)
    v.pack()

    ##Creacion de Widgets##
    w = Label(v, text="Nombre Que le colocara al nuevo archivo: ")
    w.grid(row=0,column=4)
    entrada = Entry(v)
    entrada.grid(row=1, column=4)
    boton = Button(v, text="Crear Archivo", command=lambda:Unificador(entrada.get()))
    boton.grid(row = 2, column= 4)
    NombresRutas = Text(v)
    NombresRutas.grid(row=0, column=0, rowspan=3,columnspan=3)
    Buscador = Button(v, text="Buscar Archivo", command= Buscar)
    Buscador.grid(row = 4, column=0)
    Quitador = Button(v, text="Quitar Archivo", command=Quitar)
    Quitador.grid(row=4, column=1)
    BorrarLista = Button(v, text="Sacar Todo", command=Borrar)
    BorrarLista.grid(row=4, column=2)
    Actualizar()
    ##Separador de widgets##
    
            
    ##Loop principal##
    box.mainloop()
    
main()