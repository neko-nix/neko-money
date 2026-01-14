# Este script verifica la estrategia de inversión, y la compara con los valores actuales
# para determinar si es necesario hacer un rebalanceo.

import sqlite3
import yfinance as yf
import conversiones


# Estrategia
# Idealmente después esto será automático.

proporcionUSA = 0.64
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
    conn = sqlite3.connect('nekoMoney.db')
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

    suma = 0
    for activos in totales:
        suma = activos[3] + suma
    
    print(f"El total invertido es CLP {suma:.0f}")

    print("Las proporciones actuales son:")
    for activos in totales:
        propoActual = activos[3]/suma
        print(f"{activos[0]} es {propoActual*100:.2f}%")


calcular_proporciones()

