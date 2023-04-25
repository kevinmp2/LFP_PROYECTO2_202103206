from analizador import Analizador_l
from analizador_sintactico import Analizador_sintactico


lexico = Analizador_l()
lista = lexico.analizar(open('prueba2.txt').read())
print(len(lista))
# # lexico.visualizar_errores()
# lexico.visualizar_token()

sintactico = Analizador_sintactico()
text_salida = sintactico.analizar(lista)
print(text_salida)