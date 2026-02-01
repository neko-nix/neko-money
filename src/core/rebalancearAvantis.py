# Este script verifica la estrategia de inversión, y la compara con los valores actuales
# para determinar si es necesario hacer un rebalanceo.

import sqlite3
import yfinance as yf
from src.utils import conversiones
from src.utils.paths import DB_PATH, DATA_DIR
import pandas as pd
import numpy as np
from tabulate import tabulate


holdingsACWI = DATA_DIR+"datosACWI.csv"
df = pd.read_csv(holdingsACWI, skiprows=9)

proporcionUSA = (df[df['Location'] == 'United States']['Weight (%)'].sum()/100)

proporcionesTickers = [
    ["AVUS", 0.44],
    ["AVUV", 0.22],
    ["AVDE", 0.16],
    ["AVDV", 0.08],
    ["AVEM", 0.10]
]
columnas = ["ticker", "proporción_ideal"]

dfProporcionesIdeales = pd.DataFrame(proporcionesTickers, columns=columnas)
print(dfProporcionesIdeales.head())

print("Las proporciones objetivo son las siguientes:")


    
def calcular_proporciones():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT ticker, SUM(cantidad) as cantidad, SUM(total_clp) as inversion_total_clp, SUM(total_usd) as inversion_total_usd FROM transacciones GROUP BY ticker"
    activos = pd.read_sql_query(query, conn)
    conn.close()
    

    totalActualCLP = activos['inversion_total_clp'].sum()
    totalActualUSD = activos['inversion_total_usd'].sum()

    activos['porcentaje_actual'] = activos["inversion_total_clp"]/totalActualCLP

    activos = pd.merge(activos,dfProporcionesIdeales, on="ticker", how="outer").fillna(0) 
    
    montoInvertirCLP = 560e3
    comisionBroker = max((conversiones.get_usd()*0.49)/100, 5)
    montoInvertirUSD = (montoInvertirCLP/conversiones.get_usd())+comisionBroker
    

    print(f"Se van a inyectar ${montoInvertirCLP:,.0f} CLP, ${montoInvertirUSD:,.2f} USD")
    print("Monto en USD considera comisión broker.")

    activos['inversion_ideal'] = (totalActualUSD+montoInvertirUSD)*activos['proporción_ideal']
    activos['inversion_ideal'] = activos['inversion_ideal'] - activos['inversion_total_usd']
    activos['inversion_ideal'] = activos['inversion_ideal'].clip(lower=0)

    activos['prop_invertir'] = activos['inversion_ideal'] / activos['inversion_ideal'].sum()

    # Esto se hace para que el monto a invertir coincida con la plata que vamos a inyectar de verdad
    activos['monto_invertir'] = montoInvertirUSD*activos['prop_invertir']

    lista_tickers = activos['ticker'].unique().tolist()
    precios_data = yf.download(lista_tickers, period="1d", progress=False)['Close']
    precios_actuales = precios_data.iloc[-1]

    activos['precio_actual_usd'] = activos['ticker'].map(precios_actuales)
    activos['precio_actual_usd'] = activos['precio_actual_usd'].fillna(1)
    activos['cantidad_comprar'] = activos['monto_invertir']/activos["precio_actual_usd"]
    activos['fracciones'] = activos['cantidad_comprar'] % 1
    activos['cantidad_comprar'] = activos['cantidad_comprar'].astype(int)

    activos['sobrante'] = activos['fracciones']*activos['precio_actual_usd']

    totalSobrante = activos['sobrante'].sum()

    activos = activos.sort_values(by="fracciones", ascending=False)

    for i, fila in activos.iterrows():
        precio = fila['precio_actual_usd']
        if totalSobrante >= precio and fila['monto_invertir'] > 0:
            activos.at[i, 'cantidad_comprar'] = activos.at[i, 'cantidad_comprar'] + 1
            totalSobrante -= precio
        else:
            continue

    activos['inversión_nueva'] = activos['inversion_total_usd']+(activos['cantidad_comprar']*activos['precio_actual_usd'])
    activos['proporción_nueva'] = activos['inversión_nueva'] / activos['inversión_nueva'].sum()

    #totalInvertido = activos['cantidad_comprar']*activos


    #print(f"Se inviertieron ${totalInvertido:,.2f} USD de los ${montoInvertirUSD:,.2f} USD originales")
    print(f"Sobraron: ${totalSobrante:,.2f} USD")

    totales = ['inversion_total_usd', 'porcentaje_actual', 'cantidad_comprar', 'inversión_nueva', 'proporción_nueva', 'proporción_ideal']
    activos.loc['TOTAL', totales] = activos[totales].sum()
    activos.loc['TOTAL', 'ticker'] = 'TOTAL'
    activos.loc['TOTAL'] = activos.loc['TOTAL'].fillna(0)

    activos['inversion_total_usd']= activos['inversion_total_usd'].map("$ {:,.2f}".format)
    activos['inversión_nueva']= activos['inversión_nueva'].map("$ {:,.2f}".format)
    activos['porcentaje_actual']= activos['porcentaje_actual'].map("{:,.2%}".format)
    activos['proporción_nueva']= activos['proporción_nueva'].map("{:,.2%}".format)
    activos['proporción_ideal']= activos['proporción_ideal'].map("{:,.2%}".format)



    print(tabulate(
        activos[['ticker', 'inversion_total_usd', 'porcentaje_actual', 'cantidad_comprar', 'inversión_nueva', 'proporción_nueva', 'proporción_ideal']], 
        headers=['Ticker', 'Inversión Actual', 'Prop Actual', 'Comprar', 'Inversión Nueva', 'Prop Nueva', 'Prop Ideal'], 
        tablefmt='fancy_grid',
        numalign='right',
        stralign='right',
        showindex=False
    ))

  
calcular_proporciones()

