import tkinter as tk
from abc import ABC, abstractmethod

class View(tk.Frame):
    @abstractmethod
    def create_view():
        raise NotImplementedError
        
