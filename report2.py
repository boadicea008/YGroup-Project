# coding: utf-8

import os
from pathlib import Path
import pandas
import matplotlib.pyplot as plt

basepath = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main_report2():
    year = input("Por favor, escriba el año deseado (2014-2017): ")
    print("Generando informe del año ", year)
    topn = input("Por favor, escriba el numero N deseado para el listado del Top_N: ")
    print("Generando Top ", topn)
    filepath = basepath / 'YGroup-Project' / 'data' / f'OD_{year}.csv'
    print("Obteniendo dados de", filepath)
    
    fulldf = pandas.read_csv(filepath)
    
    start_st = pandas.DataFrame({'station_code':fulldf['start_station_code']})
    start_st.dropna()
    
    end_st = pandas.DataFrame({'station_code':fulldf['end_station_code']})
    end_st.dropna()
    
    gen_st = start_st.append(end_st)
    gen_st.dropna()
    
    start_st = start_st.groupby('station_code').size().reset_index(name='count')
    start_st = start_st.sort_values('count',ascending=False)
    start_st.reset_index(drop=True,inplace=True)
    start_st.index += 1
    start_st.head(int(topn))
    
    end_st = end_st.groupby('station_code').size().reset_index(name='count')
    end_st = end_st.sort_values('count',ascending=False)
    end_st.reset_index(drop=True,inplace=True)
    end_st.index += 1
    end_st.head(int(topn))
    
    gen_st = gen_st.groupby('station_code').size().reset_index(name='count')
    gen_st = gen_st.sort_values('count',ascending=False)
    gen_st.reset_index(drop=True,inplace=True)
    gen_st.index += 1
    gen_st.head(int(topn))
    
    top_st = pandas.merge(start_st, end_st, left_index=True, right_index=True)
    top_st = pandas.merge(top_st, gen_st, left_index=True, right_index=True)
    top_st.columns = ["start_station_code", "start_count","end_station_code", "end_count","gen_station_code", "gen_count"]
    print(top_st.head(int(topn)))
    
    print("Informe generado con éxito!")

if __name__ == '__main__':
    main_report2()
    