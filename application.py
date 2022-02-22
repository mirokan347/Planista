import tkinter as tk
from view.mainwindow import Mainwindow
from view.table import Table1
from model.model import Model
from controller.tablecontroller import TableController
from controller.mainwindowcontrollers import MainwindowController

import os
from dotenv import load_dotenv, find_dotenv

# wczytanie zmiennych env
load_dotenv(find_dotenv())
SHEETS: list
DROP_COLUMNS: list
LINK = os.environ.get("LINK")
SHEETS = os.environ.get("SHEETS").split(",")
DROP_COLUMNS = os.environ.get("DROP_COLUMNS").split(",")

print(LINK, SHEETS)
print(DROP_COLUMNS)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # utworzenie modelu
        self.model = Model(LINK, DROP_COLUMNS) 
        
        # utowrzenie widoku okna głównego
        self.mainwindow = Mainwindow(self) 
        self.mainwindow.create_view()       

        # utworzenie kontrolera okna głónego
        self.mainwindow_controller = MainwindowController(self.mainwindow)            

        # utorzenie zakładek
        for sheet in SHEETS:
            self.new_tab(sheet)
                          
    def new_tab(self, sheet):

        # utworzenie tabelu
        table = Table1(self.master)
        
        # utworzenie kontrolera
        table_controller = TableController(table, self.model)
        table_controller.bind(sheet)
        table_controller.set_controller(self.mainwindow_controller)
        
        # dołożenie zakladek do okna głównego
        self.mainwindow.notebook.add(table, text=sheet)     
        

if __name__ == "__main__":

    app = Application()
       
    app.mainloop()