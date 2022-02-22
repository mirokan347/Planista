import pandas as pd
import datetime as dt

class Model():
    def __init__(self, LINK: str, DROP_COLUMNS: str):
    
        self.link = LINK
        self.drop_columns = DROP_COLUMNS
                       
    def createDataframe(self, sheet: str):
    
        try:
            df = pd.read_excel(self.link, sheet_name=sheet, header=1) # wczytanie pliku 
        
            df = df[df['TYP'].notna()]  # usunięcie wierszy z wartościami null dla kolumny TYP
            df = df.iloc[:,:18] # ograniczenie ilości kolumn wg. przedziału
            
            # usunięcie kolumn z listy zemiennej z env
            for col in self.drop_columns:
                df = df.drop([col.replace('\\n','\n')], axis=1)

            # zmiana nazwy niektórych kolumn
            df = df.rename(columns={'TERMIN WYPRODUKOWANIA PARTII PROD': 'TERMIN WYPRODUKOWANIA', 'NOWY TERMIN, JEŚLI OPÓŹNIONE': 'NOWY TERMIN',
                                    'BRAK Z DNIA/\nPOŻADANY TERMIN': 'BRAK Z DNIA'})
            # zamienienie wartości nan na puste stringi
            df.fillna('', inplace=True)
            
            # zmiana formatu wyświetlania daty
            df['BRAK Z DNIA'] = df['BRAK Z DNIA'].dt.strftime('%Y-%m-%d')
            df['DATA DO WYSYŁKI'] = df['DATA DO WYSYŁKI'].dt.strftime('%Y-%m-%d')
            df['NOWY TERMIN'] = df['NOWY TERMIN'].dt.strftime('%Y-%m-%d')
            df['TERMIN WYPRODUKOWANIA'] = df['TERMIN WYPRODUKOWANIA'].apply(lambda x: str(x).split(' ')[0]) 
            df['UWAGI'] = df['UWAGI'].apply(lambda x: str(x).replace('\n',' '))  
            
        except:        
            # jeżli nie można było wczytać pliku, wyświetla komunikat w tabeli
            d = {'col1': ["błąd odczytu pliku excel"], 'col2': ["Sprawdź scieżkę do pliku"], 'col3': ["lub plik nie istnieje"]}
            df = pd.DataFrame(data=d)
 
        
        return df
