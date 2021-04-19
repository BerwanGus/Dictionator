# (Venv_main) PS C:\Users\Pichau\Desktop\Área de Trabalho Discreta\programação\ProjetoPythonDicionario>
#
# Programa feito por Gustavo, finalizado em 28/02/2021.

from tkinter import *
import tkinter.font as TkFont
from platform import python_version
from functools import partial
from PyDictionary import PyDictionary as Pd

mainWin = Tk()

class MainWinLayout:

    def __init__(self, master):

        self.master = master
        self.master.geometry("720x720")
        self.master.minsize(500,400)
        self.master.title('Dictionator')
        self.master.iconbitmap('iconbit.ico')

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.bg_img = PhotoImage(file=('app_bg.png'))

        self.frame1 = Label(self.master, image=self.bg_img)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(2, weight=1)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(5, weight=1)
        
        self.Title = Label(self.frame1, text="Dictionator", font=("Castellar", 48), pady=15, padx=15)
        self.Title.grid(row=1, column=1, sticky=(N, W, E, S))

        self.main_InputField = Entry(self.frame1, width=35, bd=2, font=('Time New Roman', 12))
        self.main_InputField.insert(0, "Type here.")
        self.main_InputField.grid(row=2, column=1, pady=(10, 0), sticky=E)
        
        self.Submit = Button(self.frame1, font=('Time New Roman', 12), text='Search', activebackground='lightgray', border=2, command=self.GetEntryValues)
        self.Submit.grid(row=3, column=1, sticky='E', pady=5)
        self.master.bind('<Return>', lambda event: self.GetEntryValues())

        self.ResultBox = Label(self.frame1, bd=1, padx=10, pady=10, \
        relief=SOLID, text="Welcome to the Dictionator.", wraplength=480, justify=LEFT, font=('Time New Roman Bold', 12))
        self.ResultBox.grid(row=4, column=1, pady=(5, 10))

        self.frame1.grid(row=0, column=0, sticky=(N, W, E, S))


        self.master.mainloop()

    def GetEntryValues(self):
        self.invalid_list = [".", ",", "{", "}", "(", ")", "!", "?", "*", "@", ":", ";", "]", "[", "-", "_", "#"]
        self.e_text = self.main_InputField.get()
        
        for self.char in self.e_text: #formatar texto.
            if self.char in self.invalid_list:
                self.e_text = self.e_text.replace(self.char, "")

        if " " not in self.e_text and self.e_text is not "":
            self.Search(self.e_text)      
        else:
            self.ResultBox.config(text=("Results not found. Please, try again."))
            print("Results not found.")

    def Search(self, search_input):
        self.search_input = search_input
        self.pd_mean = Pd.meaning(self.search_input)
        if self.pd_mean is not None:
            self.pd_mean = str(self.pd_mean)
            self.ResultBox.config(text=(self.FormatText(self.pd_mean)))
            print("Successful")
        else:
            self.ResultBox.config(text=("Results not found. Please, try again."))
            print("Results not found.")
        
    def FormatText(self, intput_str):
        self.str = intput_str
        self.remove_list = ["{", "}"]
        for self.char in self.remove_list:
            self.str = self.str.replace(self.char, "    ")
        return self.str
    
    

        


if __name__ == "__main__":
    layout = MainWinLayout(mainWin)
    


   
    