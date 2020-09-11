from report1 import main_report1
from report2 import main_report2
from report3 import main_report3
from report4 import main_report4


def banner(message, border='*'):
    line = border * 73
    print("\n")
    print(line)
    print(message)
    print(line)

def report1():
    print("Iniciando informe 1...")
    main_report1()
def report2():
    print("Iniciando informe 2...")
    main_report2()
def report3():
    print("Iniciando informe 3...")
    main_report3()
def report4():
    print("Iniciando informe 4...")
    main_report4()

def callreport(selectedrep):
    if selectedrep == 1:
        report1()
    elif selectedrep == 2:
        report2()
    elif selectedrep == 3:
        report3()
    elif selectedrep == 4:
        report4()
    else:
        print("\n\nOpción no valida!")
        main()

def main():
    message = '\nBIENVENIDO A YGROUP -- INFORMES DE BIXI\n\nPorfavor, escriba el numero del informe desado.\n\n1. Histograma de tiempos de viaje para un año dado\n2. Listado del Top N de estaciones más utilizadas para un año dado\n3. Listado del Top N de viajes más comunes para un año dado\n4. Identificación de horas punta para un año\n\nPresione Ctrl+Z y ENTER para salir.\n'
    banner(message)
    selectedrep = input("Escriba el numero (1-4): ")
    print("Informe ", selectedrep, " seleccionado")
    callreport(int(selectedrep))
    main()


if __name__ == '__main__':
    main()

