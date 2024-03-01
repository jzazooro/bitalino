from pybitalino import BITalino

# Cambia 'XX:XX:XX:XX:XX:XX' por la dirección MAC de tu dispositivo BITalino
macAddress = "84:BA:20:5E:FB:98"

# Iniciando conexión
device = BITalino(macAddress)

# Configuración: define qué canales quieres usar [0, 1, 2, 3, 4, 5] y la frecuencia de muestreo
device.start([0, 1, 2, 3, 4, 5], 1000)

# Leer 10 muestras
data = device.read(10)

# Detener la adquisición y cerrar la conexión
device.stop()
device.close()

print(data)
