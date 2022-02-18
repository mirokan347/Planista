import pandas as pd

class Model():
    def __init__(self, link: str):
    
        self.link = link
        #self.dataframe = self.createDataframe()

                       
    def createDataframe(self, sheet: str):
        
        df = pd.read_excel(self.link, sheet_name=sheet, header=1)
        df = df[df['TYP'].notna()]       
        df = df.iloc[:,:18]
        return df

"""
link = "Q:\Planowanie Produkcji\!POTWIERDZANIE TERMINOW\Potwierdzanie terminow.xlsx"
df = pd.read_excel(link, sheet_name="EXTA", header=1)
df = df[df['TYP'].notna()]
#exta = df.iloc[:,0:15]
#result = exta.loc[df['TYP'] == 'ZCM-12']
#print(result)
"""