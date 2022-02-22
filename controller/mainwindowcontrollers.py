from controller.controllers import Controller

class MainwindowController(Controller):
    def __init__(self, mainwindow) -> None:
        super().__init__()
        self.view = None
        self.mainwindow = mainwindow
        self.select_tab = None
        
    def bind(self):
        self.select_tab = self.mainwindow.notebook.tab(self.mainwindow.notebook.select(), 'text') # przypisanie do zmiennej aktywnej zakładki
        