import pandas as pd
import matplotlib.pyplot as plt

def analisis_eda(file_path, nombre):
    data = pd.read_csv(file_path)
    # Ajustamos la columna 'intervalos' para que comience en 0 e incremente en 1 cada fila
    data['intervalos_ajustados'] = range(0, len(data))

    # Graficamos nuevamente utilizando los intervalos ajustados
    plt.figure(figsize=(12, 6))
    plt.plot(data['intervalos_ajustados'], data['canal5'], label='EDA', color='blue')
    # Añadimos títulos y etiquetas
    plt.title('Serie Temporal de Actividad Electrodermal (EDA) con Intervalos Ajustados')
    plt.xlabel('Intervalos Ajustados')
    plt.ylabel('Valores de EDA')
    plt.legend()
    # Guardamos la gráfica
    plt.savefig(nombre)


if __name__=="__main__":
    file_path = "docs/eda/csv/eda_gonzalo.csv"
    nombre = "docs/eda/graficas/eda_gonzalo.png"
    analisis_eda(file_path, nombre)
    file_path = "docs/eda/csv/eda_zazo.csv"
    nombre = "docs/eda/graficas/eda_zazo.png"
    analisis_eda(file_path, nombre)
    file_path = "docs/eda/csv/eda_miguel.csv"
    nombre = "docs/eda/graficas/eda_miguel.png"
    analisis_eda(file_path, nombre)
    file_path = "docs/eda/csv/eda_nacho.csv"
    nombre = "docs/eda/graficas/eda_nacho.png"
    analisis_eda(file_path, nombre)