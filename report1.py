# coding: utf-8

import os
from pathlib import Path
import pandas
import matplotlib.pyplot as plt

basepath = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main_report1():
    year = input("Por favor, escriba el año deseado (2014-2017): ")
    print("Generando informe del año ", year)
    filepath = basepath / 'YGroup-Project' / 'data' / f'OD_{year}.csv'
    print("Obteniendo dados de", filepath)
    
    fulldf = pandas.read_csv(filepath)
    dur_sec = fulldf["duration_sec"]
    
    plt.hist(dur_sec, 20, histtype='bar', facecolor='b', edgecolor='k', alpha=0.5)
    plt.xlabel('Tiempo de los viages(segundos)')
    plt.ylabel('Numero de viajes')
    plt.title('Tiempos de viaje ' + year)
    plt.show()
    
    print("Informe generado con éxito!")
    
if __name__ == '__main__':
    main_report1()