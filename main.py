from fileinput import filename
from tkinter import filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mb
import webbrowser
from analizador import Analizador_l
from analizador_sintactico import Analizador_sintactico

class Pantalla_Principal():
    def __init__(self):
        ventana = Tk()
        ventana.title('PROYECTO2 - LFP')
        ventana.geometry("1400x750+560+240")
        ventana.configure(bg = 'VioletRed1')
        titulo_entrada = tkinter.Label(ventana, text = 'Entrada', bg=ventana['bg'], fg = 'light cyan', font = ('italic', 12, 'bold'), highlightbackground=ventana['bg'])
        titulo_entrada.place(x = 85, y = 250)
        titulo_salida= tkinter.Label(ventana, text = 'Salida', bg=ventana['bg'], fg = 'light cyan', font = ('italic', 12, 'bold'), highlightbackground=ventana['bg'])
        titulo_salida.place(x = 765, y= 250)
        global analizador 
        analizador = Analizador_l() 
        global analizador_sintac
        analizador_sintac = Analizador_sintactico()
        self.botones(ventana)

    def botones(self, ventana):

        #Botones
        boton_abrir = Button(ventana, text = 'COMPILADOR', cursor= 'hand2', bg = 'dark turquoise', width= 12, height= 2, font= ('corabad', 10 , 'bold'))
        boton_abrir.place(x = 670, y = 20)

        boton_guardar = Button(ventana, command = self.limpiar_texto, text = 'Nuevo', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 320, y = 80)

        boton_guardar = Button(ventana, command = self.abrir_archivo, text = 'Abrir', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 205, y = 135)

        boton_guardar = Button(ventana, command = self.guardar_archivo, text = 'Guardar', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 425, y = 135)

        boton_guardar = Button(ventana, command = self.guardar_como, text = 'Guardar como', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 320, y = 190)

        boton_guardar = Button(ventana, command = self.analizar_texto, text = 'Analizar', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 950, y = 80)

        boton_guardar = Button(ventana, command = analizador.visualizar_token, text = 'Tokens', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 840, y = 135)

        boton_guardar = Button(ventana, command = analizador.visualizar_errores, text = 'Errores\nlexicos', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 1060, y = 135)

        boton_guardar = Button(ventana, command = analizador_sintac.ver_errores_sintacticos, text = 'Errores\nsintacticos', cursor= 'hand2', bg = 'SeaGreen1', width= 20, height= 2, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 950, y = 190)

        boton_guardar = Button(ventana, command = self.limpiar_texto_2, text = 'Limpiar', cursor= 'hand2', bg = 'SeaGreen1', width= 10, height= 1, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 1217, y = 250)

        boton_guardar = Button(ventana,  command = ventana.destroy, text = 'Salir', cursor= 'hand2', bg = 'SeaGreen1', width= 10, height= 1, font= ('corabad', 10 , 'bold'))
        boton_guardar.place(x = 650, y = 700)

        global area_texto
        area_texto = scrolledtext.ScrolledText(ventana, width = 65, height = 25)
        area_texto.place(x = 85, y = 280)

        global area_texto2
        area_texto2 = scrolledtext.ScrolledText(ventana, width = 65, height = 25)
        area_texto2.place(x = 765, y = 280)
        
        ventana.mainloop()
    
    def limpiar_texto(self):
        # Si el cuadro de texto no está vacío, preguntar al usuario si desea guardar el contenido
        if len(area_texto.get('1.0', tk.END)) > 1:
            respuesta = tk.messagebox.askyesnocancel('Guardar archivo', '¿Desea guardar la información antes de limpiar?')
            if respuesta is not None:
                if respuesta:
                    self.guardar_archivo()
                area_texto.delete('1.0', tk.END)
        else:
            area_texto.delete('1.0', tk.END)

    def limpiar_texto_2(self):
        # Si el cuadro de texto no está vacío, preguntar al usuario si desea guardar el contenido
        if len(area_texto2.get('1.0', tk.END)) > 1:
            respuesta = tk.messagebox.askyesnocancel('Guardar archivo', '¿Desea guardar la información antes de limpiar?')
            if respuesta is not None:
                if respuesta:
                    self.guardar_archivo()
                area_texto2.delete('1.0', tk.END)
        else:
            area_texto2.delete('1.0', tk.END)
    
    def guardar_archivo(self):
        # Abrir un diálogo de guardado de archivo
        archivo = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Archivo de texto', '*.txt'), ('Todos los archivos', '*.*')])
    
        # Si el usuario no cancela el diálogo, guardar el contenido del cuadro de texto en el archivo
        if archivo is not None:
            contenido = area_texto.get('1.0', tk.END)
            archivo.write(contenido)
            archivo.close()

    def abrir_archivo(self):
        x = ''
        Tk().withdraw()
        try:
            filename = askopenfilename(title = 'Seleccione un archivo', filetype = [('Archivos', f'*.*')])
            with open(filename, encoding= 'utf-8') as infile:
                x = infile.read()
        except:
            mensaje = 'Porfavor ingrese un archivo valido'
            mb.showinfo('Informacion', mensaje)
            return 
        
        self.texto = x
        global area_texto
        area_texto.insert('1.02', x)
        
    def analizar_texto(self):
        global area_texto
        texto = area_texto.get('0.1', END)
        analizado = analizador.analizar(texto)
        salida = analizador_sintac.analizar(analizado)
        area_texto2.insert('1.02', salida)


    def guardar_como(self):
        # Obtener el contenido del área de texto
        contenido = area_texto.get('1.0', tk.END)

        # Verificar si hay contenido en el área de texto
        if contenido.strip() == '':
            mb.showerror('Sin contenido', 'El archivo no se puede guardar porque no hay contenido.')
        else:
            # Abrir un diálogo de guardado de archivo
            archivo = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Archivo de texto', '*.txt'), ('Todos los archivos', '*.*')])

            # Si el usuario no cancela el diálogo, guardar el contenido del cuadro de texto en el archivo
            if archivo is not None:
                archivo.write(contenido)
                archivo.close()
                mb.showinfo('Guardado', 'El archivo ha sido guardado exitosamente.')
    
    def guardar_archivo(self):
        # Obtener el contenido del área de texto
        contenido = area_texto.get('1.0', tk.END)
    
        # Verificar que el contenido no esté vacío
        if contenido.strip() == '':
            mb.showerror('Sin contenido', 'El archivo no se puede guardar porque no hay contenido.')
            return
    
        # Abrir un cuadro de diálogo de guardado de archivo
        archivo = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Archivos de texto', '*.txt')])
    
        # Si el usuario cancela el cuadro de diálogo, salir de la función
        if archivo is None:
            return
    
        # Escribir el contenido en el archivo y cerrarlo
        archivo.write(contenido)
        archivo.close()
    
        # Mostrar un mensaje indicando que el archivo se ha guardado correctamente
        tk.messagebox.showinfo('Archivo guardado', f'El archivo {archivo.name} se ha guardado correctamente.')

    
ventana = Pantalla_Principal()

print()