from pathlib import Path
from Parser.Syntax import parser
import Parser.Syntax as Syntax
import Lexer.Lexer

lex_output = ""
analysis_output = ""
code_output = ""

path_Reduction = ""

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()
    
def guardar_resultados(nombre_archivo, data):
    AppDir = script_dir.parent
    output_dir = AppDir / "Outputs"
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / nombre_archivo
    global path_Reduction
    path_Reduction = output_dir / "Reductions_List.txt"
    with open(file_path, "w") as file:
        file.write(data)

script_dir = Path(__file__).parent

# Ejecutar el analizador
def AnalyzeArchive(input_file_dir):
    Syntax.rebootVariables()
    codigo = leer_archivo(input_file_dir)
    AnalyzeCode(codigo)


#    parser.parse(codigo)
    #Syntax.parsear(codigo)

#    guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
#    guardar_resultados("Reductions_List.txt", Syntax.Reduces)
#    guardar_resultados("Advertisements.txt", Syntax.Adv)
#    global code_output
#    global analysis_output
#    global lex_output
#    analysis_output = Syntax.Output_SDT
#    SDTOutput = Syntax.Semantic_Errors
#    lex_output = Lexer.Lexer.Il_char
#    if lex_output != "":
#        analysis_output = "Lexer error\n" + lex_output
#        code_output = ""
#    elif analysis_output == "Parsing Success!\nSDT Verified!":
#        if SDTOutput != "":        
#            analysis_output = "Parsing Success!\nSDT error...\n\n" + SDTOutput
#            code_output = ""
#        else:
#            code_output = Syntax.Output_Code
#    else:
#        code_output = ""


# Ejecutar el analizador
def AnalyzeCode(txt):
    Syntax.rebootVariables()

    parser.parse(txt)
    #Syntax.parsear(txt)

    guardar_resultados("SymbolTable_Updates.txt", Syntax.Upd_ST)
    guardar_resultados("Reductions_List.txt", Syntax.Reduces)
    guardar_resultados("Advertisements.txt", Syntax.Adv)
    guardar_resultados("Token_Count.txt", Lexer.Lexer.counting_tokens(txt))
    #print(Lexer.Lexer.counting_tokens(txt))
    global code_output
    global analysis_output
    global lex_output
    analysis_output = Syntax.Output_SDT
    SDTOutput = Syntax.Semantic_Errors
    lex_output = Lexer.Lexer.Il_char
    if lex_output != "":
        analysis_output = "Lexer error\n" + lex_output
        code_output = ""
    elif analysis_output == "Parsing Success!\nSDT Verified!":
        if SDTOutput != "":        
            analysis_output = "Parsing Success!\nSDT error...\n\n" + SDTOutput
            code_output = ""
        else:
            code_output = Syntax.Output_Code
    else:
        code_output = ""