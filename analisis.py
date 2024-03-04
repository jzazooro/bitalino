import pandas as pd
import matplotlib.pyplot as plt

def analisis(file_path, nombre):
    data = pd.read_csv(file_path)
    # Ajustamos la columna 'intervalos' para que comience en 0 e incremente en 1 cada fila. 
    data['intervalos_ajustados'] = range(0, len(data))

    # Nos quedamos solo con 600 filas
    

    # Graficamos nuevamente utilizando los intervalos ajustados
    plt.figure(figsize=(12, 6))
    plt.plot(data['intervalos_ajustados'], data['canal5'], label='emg', color='blue')
    # Añadimos títulos y etiquetas
    plt.title('Series Temporales de EMG')
    plt.xlabel('Intervalos Ajustados')
    plt.ylabel('Valores de EMG')
    plt.legend()
    # Guardamos la gráfica
    plt.savefig(nombre)


if __name__=="__main__":
    file_path = "docs/emg/csv/emg_gonzalo.csv"
    nombre = "docs/emg/graficas/emg_gonzalo.png"
    analisis(file_path, nombre)
    file_path = "docs/emg/csv/emg_zazo.csv"
    nombre = "docs/emg/graficas/emg_zazo.png"
    analisis(file_path, nombre)
    file_path = "docs/emg/csv/emg_miguel.csv"
    nombre = "docs/emg/graficas/emg_miguel.png"
    analisis(file_path, nombre)
    file_path = "docs/emg/csv/emg_nacho.csv"
    nombre = "docs/emg/graficas/emg_nacho.png"
    analisis(file_path, nombre)