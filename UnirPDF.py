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
    def Unificador():
        ##Comprobar si hay elementos##
        if len(Archivos) <= 1:
            messagebox.showerror("No hay Archivos suficientes","No has agregado o dejado archivos necesarios dentro de los archivo que usaras")
        else:
            ##Ruta del archivo final##
            salida = filedialog.asksaveasfilename(title="Save PDF", filetypes=[("PDF files", "*.pdf")])+".pdf"
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
                    messagebox.showinfo("Exito", f"El Archivo {os.path.basename(salida)} ha sido creado existosamente")
            else:
                messagebox.showerror("Archivo existente","El archivo ya existe, cambia el nombre")
            

    def Buscar():
        ##Buscador de archivos##
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        pdf_path = os.path.abspath(file_path)
        ##Prevenir que a la lista entren carpetas##
        if pdf_path[-4:] == ".pdf":
            ##Revisar si ya esta en la lista##
            if str(pdf_path) in Archivos:
                messagebox.showerror("Archivo existente","El archivo ya esta en la lista")
            else:
                Archivos.append(str(pdf_path))
                Actualizar()
                
    def Quitar(arc:str):
        ##Verificar si tiene elementos##
        if len(Archivos) == 0:
            messagebox.showerror("Vacio","La lista esta vacia")
        else:
            for i in range(len(Archivos)):
                ##Verificar el nombre del archivo este sin su ruta completa##
                if os.path.basename(Archivos[i]) == arc:
                    del Archivos[i]
                    messagebox.showinfo("Eliminado","El archivo con ese nombre ha sido eliminado de la lista")
                    Actualizar()
                    break
                elif i == len(Archivos)-1:
                    messagebox.showerror("No Encontrado","Ese archivo no estaba en la lista")
                
    def FrameQuitar():
        win = Tk()
        win.title("Sacar Archivo")
        t = Frame(win)
        t.pack()
        Label(t,text="Escribe el nombre exacto del archivo que quieres sacar: ").grid(row = 0, column=0, columnspan=2)
        sacar = Entry(t)
        sacar.grid(row=1, column=0, columnspan=2)
        Eliminar = Button(t, text="Sacar", command=lambda:Quitar(sacar.get()))
        Eliminar.grid(row =2, column=0)
        Cerrar = Button(t, text="Cerrar", command=win.destroy)
        Cerrar.grid(row=2,column=1)
        for widget in t.winfo_children():
            widget.grid_configure(padx = 10, pady = 5)
        win.mainloop()

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
    NombresRutas = Text(v)
    NombresRutas.grid(row=0, column=0, columnspan=3)
    Buscador = Button(v, text="Buscar Archivo", command= Buscar)
    Buscador.grid(row = 4, column=0)
    Quitador = Button(v, text="Quitar Archivo", command=FrameQuitar)
    Quitador.grid(row=4, column=1)
    BorrarLista = Button(v, text="Sacar Todo", command=Borrar)
    BorrarLista.grid(row=4, column=2)
    Crear = Button(v, text="Crear Archivo", command=Unificador)
    Crear.grid(row = 5, column= 1)
    Actualizar()
    ##Separador de widgets##
    
            
    ##Loop principal##
    box.mainloop()
    
main()