import pandas as pd
import matplotlib.pyplot as plt

def analisis(file_path, nombre):
    data = pd.read_csv(file_path)
    # Ajustamos la columna 'intervalos' para que comience en 0 e incremente en 1 cada fila. 
    data['intervalos_ajustados'] = range(0, len(data))

    # Nos quedamos solo con 600 filas
    data = data[:600]

    # Graficamos nuevamente utilizando los intervalos ajustados
    plt.figure(figsize=(12, 6))
    plt.plot(data['intervalos_ajustados'], data['canal5'], label='ECG', color='blue')
    # Añadimos títulos y etiquetas
    plt.title('Series Temporales de ECG')
    plt.xlabel('Intervalos Ajustados')
    plt.ylabel('Valores de ECG')
    plt.legend()
    # Guardamos la gráfica
    plt.savefig(nombre)


if __name__=="__main__":
    file_path = "docs/ecg/csv/ecg_gonzalo.csv"
    nombre = "docs/ecg/graficas/ecg_gonzalo.png"
    analisis(file_path, nombre)
    file_path = "docs/ecg/csv/ecg_zazo.csv"
    nombre = "docs/ecg/graficas/ecg_zazo.png"
    analisis(file_path, nombre)
    file_path = "docs/ecg/csv/ecg_miguel.csv"
    nombre = "docs/ecg/graficas/ecg_miguel.png"
    analisis(file_path, nombre)
    file_path = "docs/ecg/csv/ecg_nacho.csv"
    nombre = "docs/ecg/graficas/ecg_nacho.png"
    analisis(file_path, nombre)