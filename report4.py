# coding: utf-8

import os
from pathlib import Path
import pandas
import datetime
import matplotlib.pyplot as plt

basepath = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main_report4():
    year = input("Por favor, escriba el año deseado (2014-2017): ")
    print("Generando informe del año ", year)
    filepath = basepath / 'YGroup-Project' / 'data' / f'OD_{year}.csv'
    print("Obteniendo dados de", filepath)
    
    fulldf = pandas.read_csv(filepath)
    
    peak_time = pandas.DataFrame({"start_date":fulldf["start_date"]})
    peak_time["start_date"] = pandas.to_datetime(peak_time["start_date"])
    peak_time["hour"] = peak_time["start_date"].dt.hour
        
    peak_hour = peak_time["hour"]
        
    plt.hist(peak_hour, 24, histtype='bar', facecolor='b', edgecolor='k', alpha=0.5)
    plt.xlabel('Hora del viage')
    hh = list(range(0,24))
    plt.xticks(hh) 
    plt.ylabel('Numero de viajes') 
    plt.title('Horas punta de viajes en ' + year) 
    plt.show()
    
    print("Informe generado con éxito!")

if __name__ == '__main__':
    main_report4()