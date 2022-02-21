from view.views import View
import tkinter as tk
from tkinter import ttk
from pandas import DataFrame
from pandastable import Table, TableModel

class Table1(View):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.search_entry_var = tk.StringVar()
        
        #self.rowconfigure(0, weight=1)
        #self.columnconfigure(0, weight=1)
        #self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        
        self.notebookframe = ttk.Frame(self, width=1400, height=850, borderwidth=5, relief='flat')
        self.notebookframe.grid(row=0,column=0)
        
        
        # tworzenia ramki górnej w ramce głównej
        self.topframe = ttk.Frame(self.notebookframe, width=1400, height=100, borderwidth=5, relief='flat')
        self.topframe.grid(row=0,column=0)
        label1 = ttk.Label(self.topframe, text ="Szukaj")
        label1.grid(row=0,column=0)
        self.search_entry = ttk.Entry(self.topframe, textvariable = self.search_entry_var)
        self.search_entry.grid(row=0,column=1)
        self.search_entry_var = self.search_entry.get()
        
        # tworzenia ramki środkowej w ramce głównej        
        self.middleframe = ttk.Frame(self.notebookframe, width=1400, height=650, borderwidth=5, relief='flat')
        self.middleframe.grid(row=1,column=0)        

        
        # tworzenia dolnej górnej w ramce głównej        
        self.bottomframe = ttk.Frame(self.notebookframe, width=1400, height=100, borderwidth=5, relief='flat')
        self.bottomframe.grid(row=2,column=0)   

        self.create_button() 
        
        
    def create_view(self, data: DataFrame):

        table = pt = Table(self.middleframe, dataframe=data, showtoolbar=False, showstatusbar=False, editable=False, enable_menus=False, width=1300, height=700)
        pt.show()
        table.columncolors['ARTYKUŁ'] = '#dcf1fc' #color a specific column
        table.columncolors['NOWY TERMIN'] = '#ffe4e1'
        table.columncolors['TERMIN WYPRODUKOWANIA'] = '#ffffe0'
        table.redraw()

        """
        print(self.search_entry_var)
        canvas=tk.Canvas(self.middleframe,bg='#FFFFFF', width=1000, height=750)
        canvas.configure(scrollregion=canvas.bbox("all"))
        ybar=tk.Scrollbar(self.middleframe,orient='vertical')
        ybar.grid(row=0,column=1,sticky='ns')
        ybar.config(command=canvas.yview)
        xbar=tk.Scrollbar(self.middleframe,orient='horizontal')
        xbar.grid(row=1,column=0,sticky='we')
        xbar.config(command=canvas.xview)
        #canvas.config(width=1050, height=450)
        canvas.config(yscrollcommand=ybar.set)
        canvas.config(xscrollcommand=ybar.set)        
        canvas.grid(row=0,column=0,sticky='news')
        frame = tk.Frame(canvas)
        frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)        
        canvas.create_window(0,0,anchor='nw',window=frame)
        
        #frame = tk.Frame(self.text, height=20, width=95)
        
        
        
        #frame.rowconfigure(0, weight=1)
        #frame.columnconfigure(0, weight=1)

                
        total_rows = len(data.index)
        total_columns = len(data.columns)

        
        for idx, col in enumerate(list(data.columns)):
            label = ttk.Label(frame,width=20, text = str(col))
            label.grid(row=0, column=idx, sticky=tk.N + tk.S + tk.E + tk.W)
        
        for row in range(total_rows):
            for col in range(total_columns):
                entry = tk.Entry(frame, width=20)

                entry.grid(row=row+1, column=col, sticky=tk.N + tk.S + tk.E + tk.W)
                entry.rowconfigure(0, weight=1)
                entry.columnconfigure(0, weight=1)
                entry.insert(tk.END, data.iloc[row,col])
        """

    def create_button(self):
        frame1 = tk.Frame(self.bottomframe)
        frame1.rowconfigure(0, weight=1)
        frame1.columnconfigure(0, weight=1)
        self.button = tk.Button(frame1)
        self.button["text"] = "Odśwież"
        self.button.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        frame1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)        