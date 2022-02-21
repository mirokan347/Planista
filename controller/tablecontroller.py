from controller.controllers import Controller
from view.table import Table1
from model.model import Model

class TableController(Controller):
    def __init__(self, table, model) -> None:
        super().__init__()
        self.table = table
        self.model = model
        self.mainwindow_controller = None
        self.data = {}
        self.dataframe = None
        self.select_sheet = None

    def bind(self, sheet: str):
        self.get_dataframe(sheet)
        self.table.create_view(self.dataframe)
        self.table.button.configure(command=self.update)
        self.table.search_entry.bind('<Key-Return>', self.search)
   
    def search(self, event):
        self.mainwindow_controller.bind() #wykrycie która zakładka jest aktywna
        self.select_sheet = self.mainwindow_controller.select_tab # nazwa aktywnej zakładki
        print("select sheet",self.select_sheet) 
        
        self.table.search_entry_var = self.table.search_entry.get().upper() # wypsane słowo w polu szukaj
        print(self.table.search_entry_var)
        
        print("data -",self.data)

        if self.table.search_entry_var !='':
                
            self.dataframe = self.data[self.select_sheet]
            
            #search_data = self.dataframe[self.dataframe['TYP']==self.table.search_entry_var]
            #search_data = self.dataframe[self.dataframe.isin([self.table.search_entry_var]).any(axis=1)]
            
            df = self.dataframe
            #mask = np.column_stack([df[col].str.contains(self.table.search_entry_var, na=False) for col in df])
            search_data = df[df.apply(lambda row: row.astype(str).str.contains(self.table.search_entry_var).any(), axis=1)]
                        
            print(search_data)
            self.table.create_view(search_data)
            
        else:
        
            self.table.create_view(self.data[self.select_sheet])
        
   
    def update(self):
        self.get_dataframe(self.select_sheet)
        self.table.create_view(self.dataframe)
        self.table.search_entry.delete(0,'end')

    def get_dataframe(self, sheet):
        self.dataframe = self.model.createDataframe(sheet)
        self.data[sheet] = self.dataframe
        print(self.data.keys())
        
    def set_controller(self, mainwindow_controller):
        self.mainwindow_controller = mainwindow_controller