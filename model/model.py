import pandas as pd
import datetime as dt

class Model():
    def __init__(self, link: str):
    
        self.link = link
        #self.dataframe = self.createDataframe()

                       
    def createDataframe(self, sheet: str):
    
        try:
            df = pd.read_excel(self.link, sheet_name=sheet, header=1)
        
            df = df[df['TYP'].notna()]       
            df = df.iloc[:,:18]
            df = df.drop(['GRUPA','EXPORT', 'AMAZON / \n MARKETY', 'ILE ZAMÓWIEŃ', 'MAX ILOŚĆ POZYCJI NA  1 ZAMÓWIENIU',
                         'SUMA ZAMÓWIEŃ PO TERMINIE', 'BRAKUJE DO ZAMÓWIEŃ PO TERMINIE'], axis=1)

            df = df.rename(columns={'TERMIN WYPRODUKOWANIA PARTII PROD': 'TERMIN WYPRODUKOWANIA', 'NOWY TERMIN, JEŚLI OPÓŹNIONE': 'NOWY TERMIN',
                                    'BRAK Z DNIA/\nPOŻADANY TERMIN': 'BRAK Z DNIA'})
            df.fillna('', inplace=True)

            df['BRAK Z DNIA'] = df['BRAK Z DNIA'].dt.strftime('%Y-%m-%d')
            df['DATA DO WYSYŁKI'] = df['DATA DO WYSYŁKI'].dt.strftime('%Y-%m-%d')
            df['NOWY TERMIN'] = df['NOWY TERMIN'].dt.strftime('%Y-%m-%d')
            df['TERMIN WYPRODUKOWANIA'] = df['TERMIN WYPRODUKOWANIA'].apply(lambda x: str(x).split(' ')[0]) 
                    
        except:
        
            d = {'col1': ["błąd odczytu pliku excel"], 'col2': ["Sprawdź scieżkę do pliku"], 'col3': ["lub plik nie istnieje"]}
            df = pd.DataFrame(data=d)

        
        return df

"""
link = "Q:\Planowanie Produkcji\!POTWIERDZANIE TERMINOW\Potwierdzanie terminow.xlsx"
df = pd.read_excel(link, sheet_name="EXTA", header=1)
df = df[df['TYP'].notna()]
#exta = df.iloc[:,0:15]
#result = exta.loc[df['TYP'] == 'ZCM-12']
#print(result)
"""