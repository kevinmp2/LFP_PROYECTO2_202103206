import os
from error import *
from tokens import *

#from prettytable import PrettyTable

class Analizador_l:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.linea = 1
        self.columna = 1
        self.estado_actual = 0
        self.puntero = ''



    def guardar_errores(self, caracter):
        self.errores.append(Error(f'Caracter invalido: {caracter}', self.linea, self.columna))
    
    def guardar_token(self, tipo, token):
        self.tokens.append(Token(tipo, token, self.linea, self.columna))
        self.indice -= 1

    def visualizar_errores(self):
        archivo = open('errores.dot', 'w')
        archivo.write('digraph G {a0[shape=none label=<<TABLE align="center" border="3" cellspacing="3" cellpadding="20">')
        archivo.write('<TR><TD><FONT FACE="bold">No.</FONT></TD><TD><FONT FACE="bold">Descripcion</FONT></TD><TD><FONT FACE="bold">Linea</FONT></TD><TD><FONT FACE="bold">Columna</FONT></TD></TR>')
        print('Errores')
        contador = 0
        for error in self.errores:
            print(f'Tipo de error: {error.caracter}, Fila: {error.linea}, Columna: {error.columna}')
            contador += 1
            archivo.write('<TR><TD>' + str(contador) + '</TD><TD>' + str(error.caracter) + '</TD><TD>' + str(error.linea) + '</TD><TD>' + str(error.columna) + '</TD></TR>')

        archivo.write('</TABLE>>];}')
        archivo.close()
        os.system('dot.exe -Tpng errores.dot -o errores.png')
        os.startfile('errores.png')

    def visualizar_token(self):
        archivo2 = open('tokens.dot', 'w')
        archivo2.write('digraph G {')
        archivo2.write('Start[label="", shape=none]\n')
        #archivo2.write('Start -> a0 [label="Tabla de Tokens"]\n')
        archivo2.write('a0[shape=none label=<<TABLE align="center" border="3" cellspacing="3" cellpadding="20">')
        archivo2.write('<TR><TD><FONT FACE="bold">No.</FONT></TD><TD><FONT FACE="bold">Lexema</FONT></TD><TD><FONT FACE="bold">Token</FONT></TD><TD><FONT FACE="bold">Linea</FONT></TD><TD><FONT FACE="bold">Columna</FONT></TD></TR>')
        print('Tokens')
        contador_token = 0
        for token in self.tokens:
            print(f'Token: {token.puntero}, Tipo: {token.tipo}, Fila: {token.linea}, Columna: {token.columna}')
            contador_token += 1
            archivo2.write('<TR><TD>' + str(contador_token) + '</TD><TD>' + str(token.puntero) + '</TD><TD>' + str(token.tipo) + '</TD><TD>' + str(token.linea) +  '</TD><TD>' + str(token.columna) + '</TD></TR>')

        archivo2.write('</TABLE>>];}')
        archivo2.close()
        os.system('dot.exe -Tpng tokens.dot -o tokens.png')
        print(os.getcwd()) 
        os.startfile('tokens.png')
    
    def estado_0(self, caracter):
        if caracter == '-':
            self.estado_actual = 1
            self.columna += 1
            self.puntero += caracter
        elif caracter == '/':
            self.estado_actual = 6
            self.columna += 1
            self.puntero += caracter
        elif caracter.isalpha():
            self.estado_actual = 11
            self.columna += 1
            self.puntero += caracter
        elif caracter == '=':
            self.estado_actual = 12
            self.columna += 1
            self.puntero += caracter
        elif caracter == '(':
            self.estado_actual = 13
            self.columna += 1
            self.puntero += caracter
        elif caracter == ')':
            self.estado_actual = 14
            self.columna += 1
            self.puntero += caracter
        elif caracter == ';':
            self.estado_actual = 15
            self.columna += 1
            self.puntero += caracter
        elif caracter == ',':
            self.estado_actual = 16
            self.columna += 1
            self.puntero += caracter
        elif caracter == '"':
            self.estado_actual = 17
            self.columna += 1
            self.puntero += caracter 
        elif caracter in [' ']:
            self.columna += 1
        elif caracter == '\n':
            self.columna = 1
            self.linea += 1
        elif caracter == '#':
            pass
        else:
            self.guardar_errores(caracter)
            self.estado_actual = 0
            self.columna += 1
            self.puntero = ''
        
    def estado_1(self, caracter):
        if caracter == '-':
            self.estado_actual = 2
            self.columna += 1
            self.puntero += caracter
        else:
            self.guardar_errores(self.puntero)
            self.estado_actual = 0
            self.columna += 1
            self.puntero = ''  

    def estado_2(self, caracter):
        if caracter == '-':
            self.estado_actual = 3
            self.columna += 1
            self.puntero += caracter
        else:
            self.guardar_errores(self.puntero)
            self.estado_actual = 0
            self.columna += 1
            self.puntero = ''

    def estado_3(self, caracter):
        if caracter != '\n':
            self.estado_actual = 4
            self.columna += 1
            self.puntero += caracter
        else:
            #print(f'{self.puntero}')
            self.estado_actual = 5
            self.columna += 1
            self.linea += 1
            #self.puntero = ''     
    
    def estado_4(self, caracter):
        if caracter != '\n':
            self.estado_actual = 4
            self.columna += 1
            self.puntero += caracter
        else:
            #print(f'{self.puntero}')
            self.estado_actual = 5
            self.columna = 1
            self.linea += 1
            #self.puntero = ''

    def estado_5(self):
        print('Comnetario de una sola linea')
        self.estado_actual = 0
        self.indice -= 1
        self.puntero = ''
        #self.estado_actual = 0
    
    def estado_6(self, caracter):
        if caracter == '*':
            self.estado_actual = 7
            self.columna += 1
            self.puntero += caracter
        else:
            self.guardar_errores(self.puntero)
            self.estado_actual = 0
            self.columna += 1
            self.puntero = ''

    def estado_7(self, caracter):
        if caracter != '*':
            self.estado_actual = 8
            self.columna += 1
            self.puntero += caracter
        else:
            self.estado_actual = 9
            self.columna += 1
            self.puntero = ''
    
    def estado_8(self, caracter):
        if caracter != '*':
            self.estado_actual = 8
            self.columna += 1
            self.puntero += caracter
        else:
            self.estado_actual = 9
            self.columna += 1
            self.puntero = ''

    def estado_9(self, caracter):
        if caracter != '/':
            self.estado_actual = 8
            self.columna += 1
            self.puntero += caracter
        else:
            self.estado_actual = 10
            self.columna += 1
            self.puntero = ''
    
    def estado_10(self):
        print('Comentario de varias lineas')
        self.estado_actual = 0
        self.columna += 1
        self.puntero = ''
    
    def estado_11(self, caracter):
        if caracter.isalpha():
            self.estado_actual == 11
            self.columna += 1
            self.puntero += caracter
        else:
            if self.puntero in ['CrearBD', 'EliminarBD', 'CrearColeccion', 'EliminarColeccion', 'InsertarUnico', 'ActualizarUnico', 'EliminarUnico', 'BuscarTodo', 'BuscarUnico', 'nueva']:
                if self.puntero == 'CrearBD':
                    self.guardar_token(f'CrearBD', self.puntero)
                elif self.puntero == 'EliminarBD':
                    self.guardar_token(f'EliminarBD', self.puntero)
                elif self.puntero == 'CrearColeccion':
                    self.guardar_token(f'CrearColeccion', self.puntero)
                elif self.puntero == 'EliminarColeccion':
                    self.guardar_token(f'EliminarColeccion', self.puntero)
                elif self.puntero == 'InsertarUnico':
                    self.guardar_token(f'InsertarUnico', self.puntero)
                elif self.puntero == 'ActualizarUnico':
                    self.guardar_token(f'ActualizarUnico', self.puntero)
                elif self.puntero == 'EliminarUnico':
                    self.guardar_token(f'EliminarUnico', self.puntero)
                elif self.puntero == 'BuscarTodo':
                    self.guardar_token(f'BuscarTodo', self.puntero)
                elif self.puntero == 'BuscarUnico':
                    self.guardar_token(f'BuscarUnico', self.puntero)
                elif self.puntero == 'nueva':
                    self.guardar_token(f'nueva', self.puntero)
                # self.guardar_token(f'Reservada', self.puntero) # Cambios
                self.puntero = ''
                self.estado_actual = 0
            else:
                self.guardar_token('ID', self.puntero)
                self.puntero = ''
                self.estado_actual = 0
    
    def estado_12(self):
        self.guardar_token('Igual', self.puntero)
        self.puntero = ''
        self.estado_actual = 0

    def estado_13(self):
        self.guardar_token('Parentesis abierto', self.puntero)
        self.puntero = ''
        self.estado_actual = 0

    def estado_14(self):
        self.guardar_token('Parentesis cerrado', self.puntero)
        self.puntero = ''
        self.estado_actual = 0

    def estado_15(self):
        self.guardar_token('Punto y coma', self.puntero)
        self.puntero = ''
        self.estado_actual = 0
    
    def estado_16(self):
        self.guardar_token('Coma', self.puntero)
        self.puntero = ''
        self.estado_actual = 0
    
    def estado_17(self, caracter):
        if caracter != '"':
            if caracter == '\n':
                self.estado_actual = 17
                self.linea += 1
                self.columna = 1
            elif caracter == '{':
                self.estado_actual = 20
                self.puntero += caracter # ------------Coreccion
            else:
                self.estado_actual = 18
                self.puntero += caracter
            self.columna += 1
        else:
            self.estado_actual = 19
            self.columna += 1
            self.puntero += caracter
        
    def estado_18(self, caracter):
        if caracter != '"':
            self.estado_actual = 18
            self.columna += 1
            self.puntero += caracter
        else:
            self.estado_actual = 19
            self.columna += 1
            self.puntero += caracter

    def estado_19(self):
        self.guardar_token('Cadena', self.puntero)
        self.puntero = ''
        self.estado_actual = 0

    def estado_20(self, caracter):
        if caracter != '}':
            self.estado_actual = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.puntero += caracter
        else:
            self.estado_actual = 22
            self.columna += 1
            self.puntero += caracter
    
    def estado_21(self, caracter):
        if caracter != ')':
            self.estado_actual = 21
            if caracter == '\n':
                self.columna = 1
                self.linea += 1
            else:
                self.columna += 1
                self.puntero += caracter
        else:
            self.estado_actual = 22
            self.columna += 1

    def estado_22(self):
        try:
            self.puntero = self.puntero[:-1]
        except: pass
        self.guardar_token('Cadena',self.puntero)
        self.puntero = ''
        self.estado_actual = 0
        self.indice -= 1
    

    def analizar(self, cadena):
        print('Analizandooooooo')
        cadena += '#'
        self.indice = 0
        while(self.indice < len(cadena)):
            if self.estado_actual == 0:
                self.estado_0(cadena[self.indice])
            elif self.estado_actual == 1:
                self.estado_1(cadena[self.indice])
            elif self.estado_actual == 2:
                self.estado_2(cadena[self.indice])
            elif self.estado_actual == 3:
                self.estado_3(cadena[self.indice])
            elif self.estado_actual == 4:
                self.estado_4(cadena[self.indice])
            elif self.estado_actual == 5:
                self.estado_5()
            elif self.estado_actual == 6:
                self.estado_6(cadena[self.indice])
            elif self.estado_actual == 7:
                self.estado_7(cadena[self.indice])
            elif self.estado_actual == 8:
                self.estado_8(cadena[self.indice])
            elif self.estado_actual == 9:
                self.estado_9(cadena[self.indice])
            elif self.estado_actual == 10:
                self.estado_10()
            elif self.estado_actual == 11:
                self.estado_11(cadena[self.indice])
            elif self.estado_actual == 12:
                self.estado_12()
            elif self.estado_actual == 13:
                self.estado_13()
            elif self.estado_actual == 14:
                self.estado_14()
            elif self.estado_actual == 15:
                self.estado_15()
            elif self.estado_actual == 16:
                self.estado_16()
            elif self.estado_actual == 17:
                self.estado_17(cadena[self.indice])
            elif self.estado_actual == 18:
                self.estado_18(cadena[self.indice])
            elif self.estado_actual == 19:
                self.estado_19()
            elif self.estado_actual == 20:
                self.estado_20(cadena[self.indice])
            elif self.estado_actual == 21:
                self.estado_21(cadena[self.indice])
            elif self.estado_actual == 22:
                self.estado_22()
            self.indice += 1
        self.tokens.append(Token('EOF', 'EOF', 0, 0))
        return self.tokens
            











