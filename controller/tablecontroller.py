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
        
        self.table.search_entry_var = self.table.search_entry.get().upper() # wpisane słowo w polu szukaj

        
        if self.table.search_entry_var !='':
                
            self.dataframe = self.data[self.select_sheet] # dane aktywnej zakładki
            search_data = self.dataframe[self.dataframe.apply(lambda row: row.astype(str).str.contains(self.table.search_entry_var).any(), axis=1)] # wyszukuje wpisanego słowa w danych               
            self.table.create_view(search_data) # tworzy tabele z wyszukanymi słowami
            
        else:
        
            self.table.create_view(self.data[self.select_sheet])
           
    def update(self):
    
        self.mainwindow_controller.bind() #wykrycie która zakładka jest aktywna
        self.select_sheet = self.mainwindow_controller.select_tab # nazwa aktywnej zakładki
        self.get_dataframe(self.select_sheet) # pobieranie danych z modelu
        self.table.create_view(self.dataframe) # tworzenie tabeli z danymi
        self.table.search_entry.delete(0,'end') # czyszczenie widgetu szukaj
        
    def get_dataframe(self, sheet):
        self.dataframe = self.model.createDataframe(sheet) #pobieranie danych z modelu
        self.data[sheet] = self.dataframe

        
    def set_controller(self, mainwindow_controller):
        self.mainwindow_controller = mainwindow_controller # ustawienie kontrolera 