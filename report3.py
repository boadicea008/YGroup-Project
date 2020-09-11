# coding: utf-8

import os
from pathlib import Path
import pandas
import matplotlib.pyplot as plt

basepath = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main_report3():
    year = input("Por favor, escriba el año deseado (2014-2017): ")
    print("Generando informe del año ", year)
    topn = input("Por favor, escriba el numero N deseado para el listado del Top_N: ")
    print("Generando Top ", topn)
    filepath = basepath / 'YGroup-Project' / 'data' / f'OD_{year}.csv'
    print("Obteniendo dados de", filepath)
    
    fulldf = pandas.read_csv(filepath)
    
    pandas.options.mode.chained_assignment = None
    
    trips = fulldf[["start_station_code","end_station_code"]]
    trips['trip (start-end)'] = trips["start_station_code"].astype(str)+'-'+trips["end_station_code"].astype(str)
    trips.head(5)
    
    trips = trips.groupby('trip (start-end)').size().reset_index(name='count')
    trips = trips.sort_values('count',ascending=False)
    trips.reset_index(drop=True,inplace=True)
    trips.index += 1
    print(trips.head(int(topn)))   
    
    print("Informe generado con éxito!")

if __name__ == '__main__':
    main_report3()
    