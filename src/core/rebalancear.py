# Este script verifica la estrategia de inversión, y la compara con los valores actuales
# para determinar si es necesario hacer un rebalanceo.

import sqlite3
import yfinance as yf
from src.utils import conversiones
from src.utils.paths import DB_PATH, DATA_DIR
import pandas as pd


holdingsACWI = DATA_DIR+"datosACWI.csv"
print(holdingsACWI)

df = pd.read_csv(holdingsACWI, skiprows=9)


proporcionUSA = (df[df['Location'] == 'United States']['Weight (%)'].sum()/100)
proporcionINT = 1-proporcionUSA

tickersUSA = [["ITOT", 1/3],["IUSV",1/3],["IJR",1/3]]
tickersINT = [["IXUS", 4/5], ["SCZ",1/5]]

print("Las proporciones objetivo son las siguientes:")
for i, (ticker, prop) in enumerate(tickersUSA):
    tickersUSA[i][1] = prop*proporcionUSA
    print(f"{ticker} {tickersUSA[i][1]*100:.2f}%")

for i, (ticker, prop) in enumerate(tickersINT):
    tickersINT[i][1] = prop*proporcionINT
    print(f"{ticker} {tickersINT[i][1]*100:.2f}%")

    
def calcular_proporciones():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT ticker, 
               SUM(cantidad) as total_titulos, 
               SUM(total_clp) as inversion_total_clp
        FROM transacciones 
        GROUP BY ticker
    """)
    mis_activos = cursor.fetchall()
    totales = []

    
    total_cartera_clp = 0

    #print(f"{'TICKER':<10} | {'CANT':<7} | {'PPA ':<15} | {'VALOR ACTUAL':<15} | {'DIFERENCIA %':<10}")
    #print("-" * 65)

    for i, (ticker, cant, inv_clp) in enumerate(mis_activos):

        data = yf.Ticker(ticker)
        precio_actual_usd = data.fast_info['last_price']       
        dolar = conversiones.get_usd()

        ppa_clp = inv_clp / cant
        valor_actual_posicion_usd = cant * precio_actual_usd
        valor_actual_clp = valor_actual_posicion_usd * dolar

        totales.append([ticker,cant,inv_clp,valor_actual_clp])

    conn.close()

    sumaFinal = 0
    sumaInicial = 0
    gananciaTotal = 0
    for activos in totales:
        sumaFinal = activos[3] + sumaFinal
        sumaInicial = activos[2] + sumaInicial
    
    gananciaTotal = (sumaFinal - sumaInicial) / sumaInicial

    print("")
    print(f"El valor invertido inicial es CLP {sumaInicial:.0f}")
    print(f"El valor actual de la cartera es CLP {sumaFinal:.0f}")
    print(f"La cartera ha variado en CLP {sumaFinal-sumaInicial:.0f} ({gananciaTotal*100:.2f}%)")

    print("")
    print("Las proporciones actuales son:")
    for activos in totales:
        propoActual = activos[3]/sumaFinal
        print(f"{activos[0]} es {propoActual*100:.2f}%")


calcular_proporciones()

