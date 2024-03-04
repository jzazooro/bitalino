import pandas as pd

RUTA_TXT = "docs/data/flexiones_miguel.txt"
RUTA_CSV = "docs/data/csv/flexiones_miguel.csv"

with open(RUTA_TXT) as f:
    lines = f.readlines()
    canal1 = []
    canal2 = []
    canal3 = []
    canal4 = []
    canal5 = []
    intervals = []
for i in range(3,len(lines)):
    intervals.append(lines[i].split("\t")[0])
    canal1.append(lines[i].split("\t")[1])
    canal2.append(lines[i].split("\t")[2])
    canal3.append(lines[i].split("\t")[3])
    canal4.append(lines[i].split("\t")[4])
    canal5.append(lines[i].split("\t")[5])


columns = ["intervalos", "canal1", "canal2", "canal3", "canal4", "canal5"]
data = [intervals, canal1, canal2, canal3, canal4, canal5]

df = pd.DataFrame(data, columns).T
df.to_csv(RUTA_CSV, index=False)