import ply.lex as lex

Il_char = ""

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

keywords = {
    'else', 'float', 'if', 'int', 'void', 'printf','exp', 'sqr'
}

types = {
    'int', 'float'
}

libraries = {
    'stdio.h', 'math.h'
}

directives = {
    'include'
}

val_bool = {
    'True', 'False'
}


# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'OCURLB',
    'CCURLB',
    'SEMIC', 
    'TYPE',
    'EQUALS',
    'IDENTIFIER',
    'PRINT',
    'EXP',
    'SQR',
    'NS',
    'LIBRARIES',
    'DIRECTIVES',
    'IF',
    'ELSE',
    'VAL_BOOL',
    'OP_BOOL',
    'STRING'
)

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_OCURLB    = r'\{'
t_CCURLB    = r'\}'
t_SEMIC     = r';'
t_EQUALS    = r'='
t_NS        = r'\#'
t_PRINT     = r'printf'
t_EXP       = r'exp'
t_SQR       = r'sqr'
t_IF        = r'if'
t_ELSE      = r'else'

t_TYPE      = r'\b(?:' + '|'.join(types) + r')\b'

#Aquí agregar todas las listas de palabras reservadas posibles
resserverWords = keywords | libraries | directives | types | val_bool

t_IDENTIFIER = r'(?!\b(?:' + '|'.join(resserverWords) + r')\b)[a-zA-Z_][a-zA-Z0-9_]*'
t_LIBRARIES = r'\b(?:' + '|'.join(libraries) + r')\b'
t_DIRECTIVES = r'\b(?:' + '|'.join(directives) + r')\b'
t_VAL_BOOL = r'\b(?:' + '|'.join(val_bool) + r')\b'
t_OP_BOOL = r'(<=|>=|==|<|>)'

t_STRING = r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)  # Convierte la cadena a un número de punto flotante
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    global Il_char
    Il_char += f"'{t.value[0]}' "
    t.lexer.skip(1)

def t_eof(t):
    lexer.lineno = 1

def reboot_counts():
    global Il_char
    Il_char = ""

def counting_tokens(txt):
    lexer.input(txt)
    global tk_count
    tk_count = ""
    desc = ""

    Il_Char_taken = Il_char
    Error_Count = len(Il_Char_taken.split())

    cont = 0
    keywords_set = set()
    identifiers = set()
    punctuation = set()
    operators = set()
    constants = set()
    directives = set()
    strings = set()

    while True:
        tok = lexer.token()
        if not tok:
            break
        #Keywords
        if tok.type in {'PRINT', 'EXP', 'SQR', 'IF', 'ELSE', 'TYPE'}:
            keywords_set.add(tok.value)
        elif tok.type == 'IDENTIFIER' and tok.value not in keywords_set:
            identifiers.add(tok.value)
        #Punctuation
        elif tok.type in {'LPAREN', 'RPAREN', 'OCURLB', 'CCURLB', 'SEMIC', 'NS'}:
            punctuation.add(tok.value)
        #Operators
        elif tok.type in {'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'OP_BOOL'}:
            operators.add(tok.value)
        elif tok.type in {'NUMBER', 'VAL_BOOL'}:
            constants.add(tok.value)
        elif tok.type in {'DIRECTIVES', 'LIBRARIES'}:
            directives.add(tok.value)
        elif tok.type == 'STRING':
            strings.add(tok.value)
        cont += 1
        desc += f"Token N {cont} --> '{tok.value}' \t\tType: {tok.type} \n"
    
    #Guardar resultados
    tk_count += f"------ Conteo de Tokens ------\n\n"
    tk_count += f"Keyword: {' '.join(sorted(keywords_set))}" + "\n"
    tk_count += f"Identifier: {' '.join(sorted(identifiers))}" + "\n"
    tk_count += f"Punctuation: {' '.join(sorted(punctuation))}" + "\n"
    tk_count += f"Operator: {' '.join(sorted(operators))}" + "\n"
    tk_count += f"Constant: {' '.join(sorted(map(str, constants)))}" + "\n"
    tk_count += f"Directive: {' '.join(sorted(directives))}" + "\n"
    tk_count += f"Strings: {' '.join(sorted(strings))}" + "\n"
    tk_count += f"Conteo de tokens clasificados: {cont}"
    tk_count += f"\n-Caracteres Ilegales: {Il_Char_taken}"
    tk_count += f"\n-Conteo de tokens no clasificados: {Error_Count}" + "\n"
    tk_count += "\nDescripcion de conteo de tokens clasificados correctamente:\n" + desc

    return tk_count


# Build the lexer
lexer = lex.lex()