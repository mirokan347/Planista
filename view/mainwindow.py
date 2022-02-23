from view.views import View
from tkinter import ttk
import tkinter as tk

class Mainwindow(View):
    def __init__(self, parent):
    
        super().__init__(parent)
        self.master = parent
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1) 
        
    def create_view(self):
    
        # tworzenie okna głównego
        self.window = self.master
        self.window.title( "Planista" )
        self.window.geometry("1420x850")    
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1) 
        
        # tworzenia ramki głównej w oknie
        self.main_frame = ttk.Frame(self.window, borderwidth=5, width=1420, height=850, relief='flat')
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.grid(row=0, column=0, padx=2, pady=2, sticky=tk.N + tk.S + tk.E + tk.W) 
        self.notebook = ttk.Notebook(self.main_frame) # zakładki
        self.notebook.grid(row=0, column=0, padx=2, pady=2, sticky=tk.N + tk.S + tk.E + tk.W) 
        self.notebook.columnconfigure(0, weight=1)
        self.notebook.rowconfigure(0, weight=1)
        
            
    
        
