from view.views import View
import tkinter as tk
from tkinter import ttk


class Mainwindow(View):
    def __init__(self, parent):
    
        super().__init__(parent)
        self.master = parent
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def create_view(self):
    
        # tworzenie okna głównego
        self.window = self.master
        self.window.title( "Planista" )
        #self.window.geometry("1024x800")    
    
        # tworzenia ramki głównej w oknie
        self.main_frame = ttk.Frame(self.window, width=1400, height=850, borderwidth=5, relief='flat')
        self.main_frame.columnconfigure(0, weight=0)
        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.grid(row=0, column=0)  
        self.notebook = ttk.Notebook(self.main_frame, width=1400, height=850) # zakładki
        self.notebook.grid(row=0, column=0) 
     
        
            
    
        
