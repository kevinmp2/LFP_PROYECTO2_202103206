import os
from error import *
from tokens import *

class Analizador_sintactico:
    def __init__(self):
        self.i = 0
        self.lista_errores = []
        self.lista_tokens = []
        self.texto_salida = ''

    def analizar(self, lista_tokens):
        self.i = 0
        self.lista_tokens = lista_tokens
        self.inicio()
        return self.texto_salida 

    def inicio(self):
        self.instrucciones()

    def instrucciones(self):
        if self.lista_tokens[self.i].tipo == 'CrearBD':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'EliminarBD':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'CrearColeccion':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'EliminarColeccion':
            self.instruccion()
            self.instrucciones_2()
        
        elif self.lista_tokens[self.i].tipo == 'InsertarUnico':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'ActualizarUnico':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'EliminarUnico':
            self.instruccion()
            self.instrucciones_2()
        
        elif self.lista_tokens[self.i].tipo == 'BuscarTodo':
            self.instruccion()
            self.instrucciones_2()
        
        elif self.lista_tokens[self.i].tipo == 'BuscarUnico':
            self.instruccion()
            self.instrucciones_2()
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna)) # Dudaaaaa
            self.i += 1
            self.instruccion()
            self.instrucciones_2()
    
    def instrucciones_2(self):
        if self.lista_tokens[self.i].tipo == 'CrearBD':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'EliminarBD':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'CrearColeccion':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'EliminarColeccion':
            self.instruccion()
            self.instrucciones_2()
        
        elif self.lista_tokens[self.i].tipo == 'InsertarUnico':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'ActualizarUnico':
            self.instruccion()
            self.instrucciones_2()

        elif self.lista_tokens[self.i].tipo == 'EliminarUnico':
            self.instruccion()
            self.instrucciones_2()
        
        elif self.lista_tokens[self.i].tipo == 'BuscarTodo':
            self.instruccion()
            self.instrucciones_2()
        
        elif self.lista_tokens[self.i].tipo == 'BuscarUnico':
            self.instruccion()
            self.instrucciones_2()
        elif self.lista_tokens[self.i].tipo == 'EOF':
            print('Cadena aceptada')
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna)) # Dudaaaaa
            self.i += 1
            self.instruccion()
            self.instrucciones_2()


    def instruccion(self):
        #print(self.i)
        if self.lista_tokens[self.i].tipo == 'CrearBD':
            self.crearBD()

        elif self.lista_tokens[self.i].tipo == 'EliminarBD':
            self.eliminar_DB()

        elif self.lista_tokens[self.i].tipo == 'CrearColeccion':
            self.crear_coleccion()
    
        elif self.lista_tokens[self.i].tipo == 'EliminarColeccion': #duda
             self.eliminar_coleccion()
        
        elif self.lista_tokens[self.i].tipo == 'InsertarUnico':
            self.insertar_unico()

        elif self.lista_tokens[self.i].tipo == 'ActualizarUnico':
            self.actualizar_unico()
        
        elif self.lista_tokens[self.i].tipo == 'EliminarUnico':
            self.eliminar_unico()
        
        elif self.lista_tokens[self.i].tipo == 'BuscarTodo':
            self.buscar_todo()
        
        elif self.lista_tokens[self.i].tipo == 'BuscarUnico':
            self.buscar_unico()
            
    def crearBD(self):
        if self.lista_tokens[self.i].tipo == 'CrearBD':
            self.i += 1
            print('Entroooo a creardb' )
            if self.lista_tokens[self.i].tipo == 'ID':
                id = self.lista_tokens[self.i].puntero
                self.i += 1
                print('Entroooo a id' )
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    print('Entroooo a igual' )
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        print('Entroooo a nueva' )
                        if self.lista_tokens[self.i].tipo == 'CrearBD':
                            self.i += 1
                            print('Entroooo a creardb' )
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                print('Entroooo a PA' )
                                if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                    self.i += 1
                                    print('Entroooo a PC' )
                                    if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                        self.i += 1
                                        print('Entroooo a ;' )
                                        comando = f'use(\'{id}\');\n'
                                        self.texto_salida += comando
                                        #print(comando) 
                                    else:
                                        linea = self.lista_tokens[self.i].linea # Dudaaaaa
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else: 
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna)) 
                        print('EROOOOOORORROORORORO')
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(Error(self.lista_tokens[self.i].puntero, linea, columna))   
                     
                    
    def eliminar_DB(self):
        if self.lista_tokens[self.i].tipo == 'EliminarBD':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                #id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'EliminarBD':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                        self.i += 1
                                        comando = f'db.dropDatabase();\n'
                                        self.texto_salida += comando
                                    else:
                                        # Dudaaaaa
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                        print('EROOOOOORORROORORORO')
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
        
    def crear_coleccion(self):
        if self.lista_tokens[self.i].tipo == 'CrearColeccion':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'CrearColeccion':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                            self.i += 1
                                            comando = f'db.createCollection(\'{id}\');\n'
                                            self.texto_salida += comando
                                        else:
                                            # Dudaaaaa
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
        
    def eliminar_coleccion(self):
        if self.lista_tokens[self.i].tipo == 'EliminarColeccion':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'EliminarColeccion':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                            self.i += 1
                                            comando = f'db.{id}.drop();\n'
                                            self.texto_salida += comando
                                        else:
                                            # Dudaaaaa
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                        

    def insertar_unico(self):
        if self.lista_tokens[self.i].tipo == 'InsertarUnico':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                #id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'InsertarUnico':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    cadena = self.lista_tokens[self.i].puntero.replace("\"","")
                                    print('Entrrooooooooo', cadena)
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Coma':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Cadena':
                                            cadena_2 = self.lista_tokens[self.i].puntero.replace('"', '', 1)
                                            print('Entrrooooooooo', cadena_2)
                                            self.i += 1
                                            if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                                self.i += 1
                                                if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                                    self.i += 1
                                                    comando = f'db.{cadena}.insertOne(\n{cadena_2});\n'
                                                    self.texto_salida += comando
                                                else:
                                                    # Dudaaaaa
                                                    linea = self.lista_tokens[self.i].linea
                                                    columna = self.lista_tokens[self.i].columna
                                                    self.lista_errores.append(
                                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                                            else:
                                                linea = self.lista_tokens[self.i].linea
                                                columna = self.lista_tokens[self.i].columna
                                                self.lista_errores.append(
                                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                                        else:
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
    
    def actualizar_unico(self):    
        if self.lista_tokens[self.i].tipo == 'ActualizarUnico':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                #id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'ActualizarUnico':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    cadena = self.lista_tokens[self.i].puntero.replace("\"","")
                                    print('Entrrooooooooo', cadena)
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Coma':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Cadena':
                                            cadena_2 = self.lista_tokens[self.i].puntero.replace('"', '', 1)
                                            print('Entrrooooooooo', cadena_2)
                                            self.i += 1
                                            if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                                self.i += 1
                                                if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                                    self.i += 1
                                                    # salto_de_linea = '\n'
                                                    comando = f'db.{cadena}.insertOne(\n{cadena_2});\n'
                                                    self.texto_salida += comando
                                                else:
                                                    # Dudaaaaa
                                                    linea = self.lista_tokens[self.i].linea
                                                    columna = self.lista_tokens[self.i].columna
                                                    self.lista_errores.append(
                                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                                            else:
                                                linea = self.lista_tokens[self.i].linea
                                                columna = self.lista_tokens[self.i].columna
                                                self.lista_errores.append(
                                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                                        else:
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
    

    def eliminar_unico(self):    
        if self.lista_tokens[self.i].tipo == 'EliminarUnico':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                #id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'EliminarUnico':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    cadena = self.lista_tokens[self.i].puntero.replace("\"","")
                                    print('Entrrooooooooo', cadena)
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Coma':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Cadena':
                                            cadena_2 = self.lista_tokens[self.i].puntero.replace('"', '', 1)
                                            print('Entrrooooooooo', cadena_2)
                                            self.i += 1
                                            if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                                self.i += 1
                                                if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                                    self.i += 1
                                                    # salto_de_linea = '\n'
                                                    comando = f'db.{cadena}.insertOne(\n{cadena_2});\n'
                                                    self.texto_salida += comando
                                                else:
                                                    # Dudaaaaa
                                                    linea = self.lista_tokens[self.i].linea
                                                    columna = self.lista_tokens[self.i].columna
                                                    self.lista_errores.append(
                                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                                            else:
                                                linea = self.lista_tokens[self.i].linea
                                                columna = self.lista_tokens[self.i].columna
                                                self.lista_errores.append(
                                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                                        else:
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
    

    def buscar_todo(self):    
        if self.lista_tokens[self.i].tipo == 'BuscarTodo':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'BuscarTodo':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                            self.i += 1
                                            comando = f'db.{id}.find();\n'
                                            self.texto_salida += comando
                                        else:
                                            # Dudaaaaa
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))
        
        
    def buscar_unico(self):
        if self.lista_tokens[self.i].tipo == 'BuscarUnico':
            self.i += 1
            if self.lista_tokens[self.i].tipo == 'ID':
                id = self.lista_tokens[self.i].puntero
                self.i += 1
                if self.lista_tokens[self.i].tipo == 'Igual':
                    self.i += 1
                    if self.lista_tokens[self.i].tipo == 'nueva':
                        self.i += 1
                        if self.lista_tokens[self.i].tipo == 'BuscarUnico':
                            self.i += 1
                            if self.lista_tokens[self.i].tipo == 'Parentesis abierto':
                                self.i += 1
                                if self.lista_tokens[self.i].tipo == 'Cadena':
                                    self.i += 1
                                    if self.lista_tokens[self.i].tipo == 'Parentesis cerrado':
                                        self.i += 1
                                        if self.lista_tokens[self.i].tipo == 'Punto y coma':
                                            self.i += 1
                                            comando = f'db.{id}.findOne();\n'
                                            self.texto_salida += comando
                                        else:
                                            # Dudaaaaa
                                            linea = self.lista_tokens[self.i].linea
                                            columna = self.lista_tokens[self.i].columna
                                            self.lista_errores.append(
                                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                                    else:
                                        linea = self.lista_tokens[self.i].linea
                                        columna = self.lista_tokens[self.i].columna
                                        self.lista_errores.append(
                                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                                else:
                                    linea = self.lista_tokens[self.i].linea
                                    columna = self.lista_tokens[self.i].columna
                                    self.lista_errores.append(
                                        Error(self.lista_tokens[self.i].puntero, linea, columna))
                            else:
                                linea = self.lista_tokens[self.i].linea
                                columna = self.lista_tokens[self.i].columna
                                self.lista_errores.append(
                                    Error(self.lista_tokens[self.i].puntero, linea, columna))
                        else:
                            linea = self.lista_tokens[self.i].linea
                            columna = self.lista_tokens[self.i].columna
                            self.lista_errores.append(
                                Error(self.lista_tokens[self.i].puntero, linea, columna))
                    else:
                        linea = self.lista_tokens[self.i].linea
                        columna = self.lista_tokens[self.i].columna
                        self.lista_errores.append(
                            Error(self.lista_tokens[self.i].puntero, linea, columna))
                else:
                    linea = self.lista_tokens[self.i].linea
                    columna = self.lista_tokens[self.i].columna
                    self.lista_errores.append(
                        Error(self.lista_tokens[self.i].puntero, linea, columna))
            else:
                linea = self.lista_tokens[self.i].linea
                columna = self.lista_tokens[self.i].columna
                self.lista_errores.append(
                    Error(self.lista_tokens[self.i].puntero, linea, columna))
        else:
            linea = self.lista_tokens[self.i].linea
            columna = self.lista_tokens[self.i].columna
            self.lista_errores.append(
                Error(self.lista_tokens[self.i].puntero, linea, columna))

                                    
    def ver_errores_sintacticos(self):
        archivo3 = open('sintacticos.dot', 'w')
        archivo3.write('digraph G {')
        archivo3.write('Start[label="", shape=none]\n')
        archivo3.write('a0[shape=none label=<<TABLE align="center" border="3" cellspacing="3" cellpadding="20">')
        archivo3.write('<TR><TD><FONT FACE="bold">No.</FONT></TD><TD><FONT FACE="bold">Descripcion</FONT></TD><TD><FONT FACE="bold">Linea</FONT></TD><TD><FONT FACE="bold">Columna</FONT></TD></TR>')
        print('Caracteres')
        contador_sintac = 0
        for errores in self.lista_errores:
            contador_sintac += 1
            print(f'No.{contador_sintac}, Errores: {errores.caracter}, Linea: {errores.linea}, Columna: {errores.columna}')
            archivo3.write('<TR><TD>' + str(contador_sintac) + '</TD><TD>' + str(errores.caracter) + '</TD><TD>' + str(errores.linea) + '</TD><TD>' + str(errores.columna) + '</TD></TR>')
        archivo3.write('</TABLE>>];}')
        archivo3.close()
        os.system('dot.exe -Tpng sintacticos.dot -o sintacticos.png')
        print(os.getcwd()) 
        os.startfile('sintacticos.png')


                        






