import tkinter as tk
import tkinter.messagebox as tkmsg
from abc import ABC, abstractmethod
from tkinter import ttk
import pandas as pd
from typing import List

from view.mainwindow import Mainwindow
from view.views import View
from view.table import Table1
from model.model import Model
from controller.controllers import Controller
from controller.tablecontroller import TableController
from controller.mainwindowcontrollers import MainwindowController

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
link: list
link = os.environ.get("link")
sheets = os.environ.get("sheets").split(",")
print(link, sheets)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.model = Model(link)
        #self.title('App')
        self.mainwindow = Mainwindow(self)
 
        #mainwindow.grid(row=0, column=0, padx=10, pady=10)
        self.mainwindow.create_view()       
        
        
        #app.new_tab(view=Form, controller=predict_controller, name="Prediction")
        self.mainwindow_controller = MainwindowController(self.mainwindow)            

        
        for sheet in sheets:
            self.new_tab(sheet)
            
        

        
    def new_tab(self, sheet):

        table = Table1(self.master)
        table_controller = TableController(table, self.model)
        table_controller.bind(sheet)
        table_controller.set_controller(self.mainwindow_controller)
        self.mainwindow.notebook.add(table, text=sheet)     
        


        

if __name__ == "__main__":

    app = Application()
       
    app.mainloop()