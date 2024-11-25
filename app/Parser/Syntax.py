import sys
import os

# Obtener la ruta del directorio padre
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agregar el directorio padre al sys.path
sys.path.append(parent_dir)

import ply.yacc as yacc
import math
from Lexer.Lexer import tokens
from Lexer import Lexer
import sys

symbol_table = {}
Reduces = ""
Upd_ST = ""
Adv = ""

Output_Lex = ""
Output_SDT = "Parsing Success!\nSDT Verified!"
Output_Code = ""
Semantic_Errors = ""
conj_if = ""
desc = ""
if_List = []

def p_program(p):
    """program  : code
                | """
    saveMessages("Reduce", "P <- C")
    global if_List
    if if_List:
        prev = if_List.pop()
        if prev == "True":
            if_List.append("False")
        elif prev == "False":
            if_List.append("True")
        else:
            if_List.append("Ignore")


def p_code(p):
    """code : code statement 
            | statement"""
    if(len(p) >= 3):
        saveMessages("Reduce", "C <- C S")
    else:
        saveMessages("Reduce", "C <- S")

def p_statement(p):
    """statement    : declaration
                    | assignment
                    | prt
                    | directives
                    | ifst""" 
    saveMessages("Reduce", "S <- S(esp)")

def p_directives(p):
    """directives  : NS DIRECTIVES LIBRARIES"""
    saveMessages("Advertisements",f"Incluyendo {p[1]}{p[2]} {p[3]}")
    saveMessages("Reduce", f"Dir(S) <- {p[1]}{p[2]} {p[3]}")

def p_declaration(p):
    """declaration  : TYPE IDENTIFIER SEMIC
                    | TYPE IDENTIFIER EQUALS expression SEMIC"""
    var_type = p[1]
    var_name = p[2]
    valid = True
    #Si ya se declaro dicha variable
    if var_name in symbol_table:
        saveMessages("SemErr", f"Error: La variable '{var_name}' ya fue declarada. Linea {p.lineno(2)}. Posicion {p.lexpos(2)}")
        valid = False
        #raise SystemExit
    #Si además está haciendo una asignación
    if len(p) > 4 and p[3] == '=':
        message_red = f"D(S) <- {p[1]} {p[2]}{p[3]}{p[4]}{p[5]}"
        if p[4] == None:
            saveMessages("SemErr", f"Error: No se puede asignar un valor nulo a una variable. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
            valid = False
            #raise SystemExit
        elif (p[1] == 'int'):
            valueNum = abs(p[4])
            if (valueNum - int(valueNum) != 0):
                saveMessages("SemErr", f"Error: No se puede asignar un flotante en una variable entera. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
                valid = False
                #raise SystemExit
            else:
                value_st = int(p[4])
                message_adv = f"Declaración y asignación: {var_name} = {int(p[4])}"
        else:
            value_st = p[4]
            message_adv = f"Declaración y asignación: {var_name} = {p[4]}"
    else:
        value_st = None
        message_adv = f"Declaración: {var_name}"
        message_red = f"D(S) <- {p[1]} {p[2]}{p[3]}"
    
    saveMessages("Reduce", message_red)
    #Guardar variable, guardar mensajes y imprimir tabla de simbolos
    if (valid and ((if_List and if_List[-1] == "True") or not if_List )):
        symbol_table[var_name] = {'Identifier': var_name, 'Type': var_type, 'Value': value_st}
        saveMessages("Advertisements", message_adv)
        print_symbol_table()

def p_assignment(p):
    """assignment   : IDENTIFIER EQUALS expression SEMIC"""
    saveMessages("Reduce", f"A(S) <- {p[1]}{p[2]}{p[3]}{p[4]}")
    var_name = p[1]
    if var_name not in symbol_table:
        saveMessages("SemErr", f"Error: La variable '{var_name}' no está declarada. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
        #raise SystemExit
    else:
        valueNum = abs(p[3])
        if (symbol_table[var_name]['Type'] == 'int'):
            if (valueNum - int(valueNum) != 0):
                saveMessages("SemErr", f"Error: No se puede asignar un flotante en una variable entera. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
            elif ((if_List and if_List[-1] == "True") or not if_List):
                symbol_table[var_name]['Value'] = int(p[3])
                saveMessages("Advertisements", f"Asignación: {var_name} = {int(p[3])}")
                print_symbol_table()
        elif ((if_List and if_List[-1] == "True") or not if_List):
            symbol_table[var_name]['Value'] = p[3]
            saveMessages("Advertisements", f"Asignación: {var_name} = {p[3]}")
            print_symbol_table()
            

def p_print(p):
    """prt  : PRINT LPAREN expression RPAREN SEMIC
            | PRINT LPAREN STRING RPAREN SEMIC"""
    saveMessages("Reduce", f"P(S) <- Imprimiendo... Printf({p[3]})")
    if ((if_List and if_List[-1] == "True") or not if_List):
        show = str(p[3])
        if show[0] == '"':
            show = show.replace('"', '')
        elif show[0] == "'":
            show = show.replace("'", '')
        else:
            show = p[3]
            show = round(show, 3)
            show = str(p[3])
        
        saveMessages("Prints", show)
    #p[0] = p[1]

def p_if(p):
    """ifst : IF LPAREN valbool RPAREN OCURLB program CCURLB
            | IF LPAREN valbool RPAREN OCURLB program CCURLB ELSE OCURLB program CCURLB"""
    saveMessages("Advertisements", "Cierre de un if")
    saveMessages("Reduce", f"ifst(S) <- {p[1]}{p[2]}{p[3]}{p[4]}")
    if_List.pop()

#Syntax for summ
def p_expression_plus(p):
    """expression   : expression PLUS term"""
    if(p[1] == None):
        saveMessages("SemErr", f"Error: No se pueden sumar variables nulas. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
    elif(p[3] == None):
        saveMessages("SemErr", f"Error: No se pueden sumar variables nulas. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
        #raise SystemExit
    else:
        p[0] = p[1] + p[3]
        saveMessages("Reduce", f"E <- {p[1]}{p[2]}{p[3]}")

def p_expression_minus(p):
    """expression   : expression MINUS term"""
    if(p[1] == None):
        saveMessages("SemErr", f"Error: No se pueden restar variables nulas. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
    elif(p[3] == None):
        saveMessages("SemErr", f"Error: No se pueden restar variables nulas. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
        #raise SystemExit
    else:
        p[0] = p[1] - p[3]
        saveMessages("Reduce", f"E <- {p[1]}{p[2]}{p[3]}")
    

def p_term_times(p):
    """term : term TIMES factor"""
    if(p[1] == None):
        saveMessages("SemErr", f"Error: No se pueden multiplicar variables nulas. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
    elif(p[3] == None):
        saveMessages("SemErr", f"Error: No se pueden multiplicar variables nulas. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
        #raise SystemExit
    else:
        p[0] = p[1] * p[3]
        saveMessages("Reduce", f"T <- {p[1]} * {p[3]}")
    

def p_term_div(p):
    """term : term DIVIDE factor"""
    if(p[1] == None):
        saveMessages("SemErr", f"Error: No se pueden dividir variables nulas. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
    elif(p[3] == None):
        saveMessages("SemErr", f"Error: No se pueden dividir entre variables nulas. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
        #raise SystemExit
    else:
        p[0] = p[1] / p[3]
        saveMessages("Reduce", f"T <- {p[1]} / {p[3]}")
        #raise SystemExit
    
def p_factor_exp(p):
    """factor : EXP LPAREN factor value RPAREN"""
    if((p[3] != None) and ((p[4] != None))):
        saveMessages("Advertisements", f"Elevando {p[3]} a la {p[4]} = {p[3]**p[4]}")
        saveMessages("Reduce", f"F <- {p[1]}{p[2]}{p[3]} {p[4]}{p[5]}")
        p[0] = p[3]**p[4]
    else:
        saveMessages("SemErr", f"Error: No se puedee elevar a una potencia variables nulas. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
        #raise SystemExit
    
def p_factor_sqr(p):
    """factor : SQR LPAREN factor RPAREN"""
    if(p[3] != None):
        saveMessages("Advertisements", f"Raiz cuadrada de {p[3]} = {math.sqrt(p[3])}")
        saveMessages("Reduce", f"F <- {p[1]}{p[2]}{p[3]}{p[4]}")
        p[0] = math.sqrt(p[3])
    else:
        saveMessages("SemErr", f"Error: No se puede calcular la raiz cuadrada de variables nulas. Linea {p.lineno(3)}. Posicion {p.lexpos(3)}")
        #raise SystemExit
    

def p_values_num(p):
    """value   : NUMBER"""
    p[0] = p[1]
    saveMessages("Reduce", f"V <- N {p[1]}")

def p_value_bool(p):
    """ valbool     : VAL_BOOL
                    | expression OP_BOOL expression"""
    if (p[1] == 'True' or p[1] == 'False'):
        Val = p[1]
    elif p[2] == '<':
        Val = p[1] < p[3]
    elif p[2] == '>':
        Val = p[1] > p[3] 
    elif (p[2] == '<='):
        Val = p[1] <= p[3] 
    elif (p[2] == '>='):
        Val = p[1] >= p[3] 
    elif (p[2] == '=='):
        Val = p[1] == p[3] 
    else:
        Val = p[2]
    p[0] = Val
    saveMessages("Reduce", f"V <- B {Val}")
    #print("Valuación de un booleano")
    if ((if_List and if_List[-1] == "True") or not if_List):
        conj_if = str(Val)
        if_List.append(conj_if)
    else:
        if_List.append("Ignore")


def p_expression_term(p):
    """expression   : term""" 
    p[0] = p[1]
    saveMessages("Reduce", f"E <- T {p[1]}")

def p_term_factor(p):
    "term : factor"
    p[0] = p[1]
    saveMessages("Reduce", f"T <- F {p[1]}")

def p_factor_value(p):
    """factor   : value
                | IDENTIFIER
                | LPAREN expression RPAREN
                | MINUS factor"""
    if p[1] == '-':
        p[0] = (-1)*p[2]
        saveMessages("Reduce", f"F <- V {p[2]}")
    elif p[1] == '(':
        p[0] = p[2]
        saveMessages("Reduce", f"F <- V {p[2]}")
    elif not str(p[1])[0].isnumeric():
        var_name = p[1]
        if not var_name in symbol_table:
            saveMessages("SemErr", f"Error: La variable '{var_name}' no existe declarada. Linea {p.lineno(1)}. Posicion {p.lexpos(1)}")
            #raise SystemExit
        else:
            ref_val = symbol_table[var_name]['Value']
            p[0] = ref_val
            saveMessages("Reduce", f"F <- Var_val {ref_val}")
    else:
        p[0] = p[1]
        saveMessages("Reduce", f"F <- V {p[1]}")

#Error rule for syntax errors
def p_error(p):
    saveMessages("Advertisements", "Syntax error in input!")
    global Output_SDT
    print("Parsing error...")
    print("SDT error...\n")
    if p:
        tok = parser.token()
        #print(f"Error de sintaxis en '{p.value}'  '{p.type}'    '{parser.token()}'")
        Output_SDT = f"Parsing error...\nSDT error...\n\nError de sintaxis en '{p.value}' en la linea {p.lineno}, no se espera un token de tipo '{p.type}'"
        return
        #raise SystemExit
    else:
        #print("Error de sintaxis al final de la entrada")
        Output_SDT = f"Parsing error...\nSDT error...\n\nError de sintaxis al final de la entrada."
        return
        #raise SystemExit

def print_symbol_table():
    saveMessages("Symbol Table", "\n\nTabla de Símbolos:")
    saveMessages("Symbol Table", "{:<15} {:<10} {:<10}".format("Identificador", "Tipo", "Valor"))
    saveMessages("Symbol Table", "-" * 35)    
    for var_name, attributes in symbol_table.items():

        if isinstance(attributes, dict):
            var_type = attributes.get("Type", "N/A")
            var_value = attributes.get("Value", "N/A")
        else:
            
            var_type = "N/A"
            var_value = str(attributes)  
        
        if var_value is None:
            var_value = "N/A"

        saveMessages("Symbol Table", "{:<15} {:<10} {:<10}".format(var_name, var_type, var_value))
    saveMessages("Symbol Table", "-" * 35)

def saveMessages(Type, Message):
    global Upd_ST, Adv, Reduces, Semantic_Errors, Output_Code
    match Type: 
        case "Advertisements":
            Adv += Message + "\n"
        case "Reduce":
            Reduces += Message + "\n"
        case "Symbol Table":
            Upd_ST += Message + "\n"
        case "SemErr":
            Semantic_Errors += Message + "\n"
        case "Prints":
            Output_Code += Message + "\n"
    

def rebootVariables():
    global symbol_table, Reduces, Upd_ST, Adv, Output_SDT, Semantic_Errors, Output_Code
    symbol_table = {}
    Reduces = ""
    Upd_ST = ""
    Adv = ""
    Output_SDT = "Parsing Success!\nSDT Verified!"
    Semantic_Errors = ""
    Output_Code = ""
    Lexer.reboot_counts()

#Build the parser
parser = yacc.yacc()