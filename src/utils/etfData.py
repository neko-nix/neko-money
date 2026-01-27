import requests
import pandas as pd
import io
import os
from src.utils.paths import DATA_DIR


urlACWI = "https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf/1467271812596.ajax?fileType=csv&fileName=ACWI_holdings&dataType=fund"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
nombreArchivo = str(DATA_DIR)+"datosACWI.csv"
if not os.path.exists(nombreArchivo):
    print("Descargando datos ACWI...")
    r = requests.get(urlACWI, headers=headers)
    if r.status_code == 200:
        with open(nombreArchivo, "w", encoding="utf-8") as f:
            f.write(r.text)
    else:
        print(f"Error: {r.status_code}")
else:
    print(f'Utilizando el archivo local "{nombreArchivo}"')

try:
    df = pd.read_csv(nombreArchivo, skiprows=9, on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print(f"Error al leer el CSV: {e}")


