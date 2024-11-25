#import UI.UI
from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

colour1 = "#020f12"
colour2 = "#05d7ff"
colour3 = "#65e7ff"
colour4 = "BLACK"

colour5 = "#05242B"
colour6 = "#26364B"

app_dir = Path(__file__).parent
Outputs_dir = app_dir / "Outputs"
textRed =  Outputs_dir / "Reductions_List.txt"
    #archivo = Examples_dir / "ejemploE3.cpy"
    #if textRed == "":
    #    return
root = Tk()
root.title("Reductions")
root.resizable(True, True)
root.geometry('600x300')
#root.config(bg=colour1)

FrameR = Frame(root)#, background="#05242B")
FrameR.grid(row=0,column=0)
    
#RedLabel=Label(Frame1, text=textRed)
#RedLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
Red_text = ScrolledText(FrameR, width=70, height=30)
Red_text.config(background=colour6, foreground='WHITE')
Red_text.grid(row=2, column=0, padx=10, pady=10)
Red_text.insert("1.0", "Acá van las reducciones\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na")
Red_text.config(state="disabled")

root.mainloop()