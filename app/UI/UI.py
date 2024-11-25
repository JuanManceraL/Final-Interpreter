import sys
import os

# Obtener la ruta del directorio padre
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Agregar el directorio padre al sys.path
sys.path.append(parent_dir)

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time
from pathlib import Path
import Analyzer

UI_dir = Path(__file__).parent
app_dir = UI_dir.parent.parent
Examples_dir = app_dir / "Examples"
Outputs_dir = app_dir / "Outputs"

prevName = "a"
pad_x_buttons = 7
pad_y_buttons = 24

colour1 = "#020f12"
colour2 = "#05d7ff"
colour3 = "#65e7ff"
colour4 = "BLACK"

colour5 = "#05242B"
colour6 = "#26364B"


def NewArchive():
    prevName = "a"
    Box_code.delete("1.0", "end")

def AnalyzeCode():
    Script_txt = Box_code.get(1.0, END)
    Analyzer.AnalyzeCode(Script_txt)
    UpdateOutput()

def AnalyzeScript(ExampleNum = None):
    global prevName
    if ExampleNum == None:
        archivo = filedialog.askopenfilename()
        prevName = archivo
    else:
        if ExampleNum == 0:
            archivo = Examples_dir / "ejemplo0.cpy"
        elif ExampleNum == 1:
            archivo = Examples_dir / "ejemplo1.cpy"
        elif ExampleNum == 2:
            archivo = Examples_dir / "ejemplo2.cpy"
        elif ExampleNum == 3:
            archivo = Examples_dir / "ejemplo3.cpy"
        elif ExampleNum == 4:
            archivo = Examples_dir / "ejemploprt.cpy"
        elif ExampleNum == 5:
            archivo = Examples_dir / "ejemplo5.cpy"
        elif ExampleNum == 6:
            archivo = Examples_dir / "ejemploE0.cpy"
        elif ExampleNum == 7:
            archivo = Examples_dir / "ejemploE1.cpy"
        elif ExampleNum == 8:
            archivo = Examples_dir / "ejemploE2.cpy"
        elif ExampleNum == 9:
            archivo = Examples_dir / "ejemploE3.cpy"
        prevName = "a"
    if not archivo:
        prevName = "a"
        return
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())
    AnalyzeCode()

def LoadCode():
    global prevName
    archivo = filedialog.askopenfilename()
    if not archivo:
        return
    prevName = archivo
    Box_code.delete("1.0", "end")
    with open(archivo, 'r') as file:
        Box_code.insert("1.0", file.read())

def SaveCodeAs():
    global prevName
    archivo = filedialog.asksaveasfile(defaultextension='.cpy', filetypes=[('Archivo CPY','.cpy'), ('Archivo de texto','.txt'), ('Archivo C','.c'), ('Todos los archivos','.*') ])
    if archivo is None:
        return
    prevName = archivo.name
    archivoTexto = Box_code.get(1.0, END)
    archivo.write(archivoTexto)
    archivo.close()

def SaveCode():
    if len(prevName) <= 1:
       SaveCodeAs()
       return
    with open(prevName, "w") as file:
        archivoTexto = Box_code.get(1.0, END)
        file.write(archivoTexto)

def Copy():
    Box_code.event_generate("<<Copy>>")

def Cut():
    Box_code.event_generate("<<Cut>>")  

def Paste():
    Box_code.event_generate("<<Paste>>")  

def ExitApp():
    value = messagebox.askokcancel("Salir", "Estás seguro que deseas salir?")
    if value:
        raiz.destroy()

def UpdateOutput():
    time.sleep(0.2)
    textOutput = Analyzer.analysis_output
    LabSA.config(text=textOutput)
    
    textOutput = Analyzer.code_output
    LabOut.config(text=textOutput)
    #Asignar a la salida output el 
    #Analyzer.code_output

def ShowCommands():
    messagebox.showinfo("Funciones disponibles", """- printf: \nImprime numeros o cadenas de texto \nUso:\nprintf('Cadena de texto') || printf(3+5) || printf(variable)\n\n
- if: \nPermite solo ejecutar ciertos segmentos de código a partir de una condición \nUso:\nif(condicion)\n{codigo_a_realizar} || \n\nif(condicion)\n{codigo_a_realizar}\nelse\n{codigo_a_realizar_en_caso_contrario}""")

def ShowRequeriments():
    messagebox.showinfo("Información del entorno", "Información del entorno de ejecución en el que fue creado este proyecto: \n\nPython 3.10.4\n\ntkinter == 8.6\nply == 3.11")

def ShowInfoTeam():
    messagebox.showinfo("Team Info", "Code editor for language CPY\nInterpreter - Team 05 \nLexel / Syntatic / Semantic - Analyzer") #\nJuan M\nDaniela M\nAngel R\n


def showOutputs(textDir = None, title= None):
    #textDir = "Reductions_List.txt"
    if (textDir == None) or (title == None):
        return
    textRed =  Outputs_dir / textDir
    if not Path(textRed).is_file():
        messagebox.showwarning("Error", "No se ha encontrado el archivo de salida seleccionado. \nFavor de ejecutar al menos un código")
        return
    #print(textRed)
    root = Tk()
    root.title(title)#"Reductions"
    root.resizable(True, True)
    root.geometry('600x250')
    root.config(bg=colour1)

    FrameR = Frame(root, background="#05242B")
    FrameR.grid(row=0,column=0)
    
    Output_text = ScrolledText(FrameR, width=70, height=14)
    Output_text.config(background=colour6, foreground='WHITE')
    Output_text.grid(row=2, column=0, padx=10, pady=10)
    Output_text.insert("1.0", "No se ha analizado ningún código")
    Output_text.delete("1.0", "end")
    with open(textRed, 'r') as file:
        Output_text.insert("1.0", file.read())
    if Output_text.get(1.0, END) == "\n":
        Output_text.insert("1.0", "No se ha hecho ninguna reducción")
    Output_text.config(state="disabled")

#raiz
raiz = Tk()
raiz.title("Code Editor - Interpreter - CPY - Team 05")
raiz.resizable(True, True)
raiz.iconbitmap(UI_dir / "Image_icon.ico")
#raiz.geometry('800x400')
raiz.geometry("850x750")
raiz.config(bg=colour1)

Frame1 = Frame(raiz, background="#05242B")
Frame1.grid(row=0,column=0)
Frame1.config(bg="#05242B", height=750, pady=30 )

Frame2 = Frame(raiz)
Frame2.grid(row=0,column=1)
Frame2.config(bg=colour1, width=20, height=20, pady=40, padx=25)

CodeLabel=Label(Frame1, text="Codigo: ", background="#05242B", foreground='WHITE', font=('Arial', 10, 'bold'))
CodeLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")

Box_code = ScrolledText(Frame1, width=70, height=27)
Box_code.config(background=colour6, foreground='WHITE')
Box_code.grid(row=2, column=0, padx=10, pady=10)
Box_code.insert("1.0", "Escribe tu codigo aqui")
#Box_code.config(state="disabled")

CodeLabel=Label(Frame1, text="Salida analisis: ", background="#05242B", foreground='WHITE', font=('Arial', 10, 'bold'))
CodeLabel.grid(row=3, column=0, padx=10, pady=5, sticky="w")

LabSA=Label(Frame1)
LabSA.config(background="#05242B", text="", wraplength=580, foreground='WHITE', font=('Arial', 10, 'bold'))
LabSA.grid(row=4, column=0, padx=10, pady=2)

LabInf=Label(Frame1, text="", background="#05242B")
LabInf.grid(row=5, column=0, padx=10, pady=45, sticky="w")

width_buttons = 18

botonAnalyze = Button(Frame2, text="Ejecutar codigo", width=width_buttons, command=AnalyzeCode, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
botonAnalyze.grid(row=0, column=0, padx=pad_y_buttons)

LabB1=Label(Frame2)
LabB1.config(background=colour1)
LabB1.grid(row=1, column=0, padx=2, pady=2)

botonAnalyzeCode = Button(Frame2, text="Ejecutar archivo", width=width_buttons, command=AnalyzeScript, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
botonAnalyzeCode.grid(row=2, column=0, padx=pad_y_buttons)

LabB2=Label(Frame2)
LabB2.config(background=colour1)
LabB2.grid(row=3, column=0, padx=2, pady=2)

PasteButton=Button(Frame2, text="Pegar texto copiado", width=width_buttons, command=Paste, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
PasteButton.grid(row=4, column=0, padx=pad_y_buttons)

LabB3=Label(Frame2)
LabB3.config(background=colour1)
LabB3.grid(row=5, column=0, padx=2, pady=2)

LoadButton=Button(Frame2, text="Cargar Archivo", width=width_buttons, command=LoadCode, font=('Arial', 10, 'bold'), height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
LoadButton.grid(row=6, column=0, padx=pad_y_buttons)

LabB4=Label(Frame2)
LabB4.config(background=colour1)
LabB4.grid(row=7, column=0, padx=2, pady=2)

SaveButton=Button(Frame2, command=SaveCode, text="Guardar", font=('Arial', 10, 'bold'), width=width_buttons, height=1,
                            background=colour1, foreground=colour2, activebackground=colour3, activeforeground=colour1,
                            highlightthickness=1, highlightbackground=colour1, highlightcolor='salmon', border=5)
SaveButton.grid(row=8, column=0, padx=pad_y_buttons)

LabB5=Label(Frame2)
LabB5.config(background=colour1)
LabB5.grid(row=9, column=0, padx=10, pady=2)

LabB6=Label(Frame2)
LabB6.config(background=colour1, text="Salida:", foreground=colour2, font=('Arial', 10, 'bold'))
LabB6.grid(row=10, column=0, padx=10, pady=2)

#txt_Output=''
LabOut=Label(Frame2)
LabOut.config(background=colour1, text="", width=width_buttons+5, wraplength=180, foreground=colour2, font=('Arial', 10, 'bold'))
LabOut.grid(row=11, column=0, padx=10, pady=2)

    #Menu
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo", command=NewArchive)
archivoMenu.add_command(label="Guardar", command=SaveCode)
archivoMenu.add_command(label="Guardar como", command=SaveCodeAs)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ExitApp)

ejemplosMenu = Menu(barraMenu, tearoff=0)
ejemplosMenu.add_command(label="Ejemplo 0", command=lambda: AnalyzeScript(0))
ejemplosMenu.add_command(label="Ejemplo 1", command=lambda: AnalyzeScript(1))
ejemplosMenu.add_command(label="Ejemplo 2", command=lambda: AnalyzeScript(2))
ejemplosMenu.add_command(label="Ejemplo 3", command=lambda: AnalyzeScript(3))
ejemplosMenu.add_command(label="Ejemplo 4", command=lambda: AnalyzeScript(4))
ejemplosMenu.add_command(label="Ejemplo 5", command=lambda: AnalyzeScript(5))
ejemplosMenu.add_separator()
ejemplosMenu.add_command(label="Ejemplo error 0", command=lambda: AnalyzeScript(6))
ejemplosMenu.add_command(label="Ejemplo error 1", command=lambda: AnalyzeScript(7))
ejemplosMenu.add_command(label="Ejemplo error 2", command=lambda: AnalyzeScript(8))
ejemplosMenu.add_command(label="Ejemplo error 3", command=lambda: AnalyzeScript(9))

herramientasMenu = Menu(barraMenu, tearoff=0)
herramientasMenu.add_command(label="Cortar", command=Cut)
herramientasMenu.add_command(label="Copiar", command=Copy)
herramientasMenu.add_command(label="Pegar", command=Paste)

outputsMenu = Menu(barraMenu, tearoff=0)
outputsMenu.add_command(label="Conteo de tokens", command=lambda: showOutputs("Token_Count.txt", "Conteo de Tokens"))
outputsMenu.add_command(label="Muestra de reducciones", command=lambda: showOutputs("Reductions_List.txt", "Reducciones"))
outputsMenu.add_command(label="Actualizacion de tabla de simbolos", command=lambda: showOutputs("SymbolTable_Updates.txt", "Actualizaciones de Tabla de Símbolos"))
outputsMenu.add_command(label="Registro de eventos", command=lambda: showOutputs("Advertisements.txt", "Registro de eventos"))

ayudaMenu = Menu(barraMenu,  tearoff=0)
ayudaMenu.add_command(label="Funciones disponibles", command=ShowCommands)
ayudaMenu.add_command(label="Información del entorno", command=ShowRequeriments)
ayudaMenu.add_command(label="Información fabricante", command=ShowInfoTeam)

barraMenu.add_cascade(label="Archivo", menu = archivoMenu)
barraMenu.add_cascade(label="Ejemplos", menu = ejemplosMenu)
barraMenu.add_cascade(label="Herramientas", menu = herramientasMenu)
barraMenu.add_cascade(label="Últimas salidas", menu = outputsMenu)
barraMenu.add_cascade(label="Ayuda", menu = ayudaMenu)

raiz.mainloop()
