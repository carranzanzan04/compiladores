#-----------------------------------------------------
# calculexer.py
#
# tokenizador para una expreción para
# nimeros y +,-,*,/
#--------------------------------------------------------
from ast import type_ignore
from ply.lex import lex
# lista del nombre de los token. esto es requerido siempre
tokens=("numero","mas","menos","por","entre","aparentesis","cparentesis")
# expreciones regulares para simplificar los tokens 
t_mas=r"\+"
t_menos=r"-"
t_por=r"\*"
t_entre=r"\/"
t_aparentesis=r"\("
t_cparentesis=r"\)"
#una regla de exprecion  regular con algun codigo de accion  
def t_numero(t):
    r"\d+"
    t.value=int(t.value)
    return t
# define una regla para poder rastrear los numeros de la linea
def T_nuevalinea(t):
    r"\n+"
    t.lexer.lineno +=len(t.value)
#una cadena que contiene caracteres ignorados (espacios y tabuladores)
t_ignore ="\t"
# regla de maneo de errores
def t_error(t):
    print("caracter ilegal '%s'"%t.value[0])
    t.lexer.skip(1)
# construlle el lexer
lexer = lex()
data="...3 + 4 * 10 + - 20 *2..."
# Dale al lexer algo de entrada
lexer.input(data)
#tokenizar
while True:
    tok=lexer.token()
    if not tok:
        break
    print(tok)

