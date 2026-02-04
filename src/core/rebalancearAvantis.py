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
    ["AVUS", 0.4227],
    ["AVUV", 0.2113],
    ["AVDE", 0.1693],
    ["AVDV", 0.0847],
    ["AVEM", 0.1120]
]
columnas = ["ticker", "proporción_ideal"]

dfProporcionesIdeales = pd.DataFrame(proporcionesTickers, columns=columnas)


# Creamos una versión formateada para mostrar
tabla_porcentajes = [[t, f"{p:.2%}"] for t, p in proporcionesTickers]

print(tabulate(tabla_porcentajes,
               headers=["Ticker", "Prop Ideal"],
               tablefmt="rounded_grid",
               numalign='right',
               stralign='right'))



    
def calcular_proporciones():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT ticker, SUM(cantidad) as cantidad, \
            SUM(total_clp) as inversion_inicial_clp, \
            SUM(total_usd) as inversion_inicial_usd  \
            FROM transacciones GROUP BY ticker"
    activos = pd.read_sql_query(query, conn)
    conn.close()

    # Inveriones inciales 
    totalInicialCLP = activos['inversion_inicial_clp'].sum()
    totalInicialUSD = activos['inversion_inicial_usd'].sum()

    # Valores actuales
    lista_tickers = activos['ticker'].unique().tolist()
    precios_data = yf.download(lista_tickers, period="1d", progress=False)['Close']
    precios_actuales = precios_data.iloc[-1]

    activos['precio_actual_usd'] = activos['ticker'].map(precios_actuales)
    activos['precio_actual_usd'] = activos['precio_actual_usd'].fillna(1)
    activos['inversion_actual_usd'] = activos['precio_actual_usd'] * activos['cantidad']
    

    totalActualUSD = activos['inversion_actual_usd'].sum()

    dolarObservado = conversiones.get_usd()
    totalActualCLP = activos['inversion_actual_usd'].sum()*dolarObservado

    # Porcentajes
    activos['porcentaje_actual'] = activos["inversion_actual_usd"]/totalActualUSD
    activos = pd.merge(activos,dfProporcionesIdeales, on="ticker", how="outer").fillna(0) 


    # Montos a invertir
    montoInvertirCLP = 560e3
    comisionBroker = max((dolarObservado*0.49)/100, 5)
    dolarBroker = comisionBroker + dolarObservado
    montoInvertirUSD = montoInvertirCLP/(dolarObservado+comisionBroker)
    comisionPagada = montoInvertirUSD*comisionBroker
    proporcionComision = (dolarBroker-dolarObservado)/dolarObservado

    print(f"Precio Dólar Mercado: ${dolarObservado:,.2f}")
    print(f"Precio Dólar Broker: ${dolarObservado+comisionBroker:,.2f}")   

    print(f"Se van a inyectar ${montoInvertirCLP:,.0f} CLP, ${montoInvertirUSD:,.2f} USD")
    print(f"Comisión total pagada por cambio de divisa: ${comisionPagada:,.2f} CLP, ${comisionPagada/dolarObservado:,.2f} USD")


    # Inversión ideal
    activos['inversion_ideal'] = (totalActualUSD+montoInvertirUSD)*activos['proporción_ideal']
    activos['inversion_ideal'] = activos['inversion_ideal'] - activos['inversion_actual_usd']
    activos['inversion_ideal'] = activos['inversion_ideal'].clip(lower=0)

    activos['prop_invertir'] = activos['inversion_ideal'] / activos['inversion_ideal'].sum()

    # Esto se hace para que el monto a invertir coincida con la plata que vamos a inyectar de verdad
    activos['monto_invertir'] = montoInvertirUSD*activos['prop_invertir']
    activos['comisión_pagada'] = activos['monto_invertir']*proporcionComision

    #activos['cantidad_comprar'] = activos['monto_invertir']/activos["precio_actual_usd"]

    # Cantidades nuevas estimadas
    activos['inversión_nueva'] = activos['inversion_actual_usd']+activos['monto_invertir']
    activos['proporción_nueva'] = activos['inversión_nueva'] / activos['inversión_nueva'].sum()

    totales = ['inversion_actual_usd', 'porcentaje_actual', 'monto_invertir', 'comisión_pagada', 'inversión_nueva', 'proporción_nueva', 'proporción_ideal']

    activos.loc['TOTAL', totales] = activos[totales].sum()
    activos.loc['TOTAL', 'ticker'] = 'TOTAL'
    activos.loc['TOTAL'] = activos.loc['TOTAL'].fillna(0)

    activos['inversion_actual_usd']= activos['inversion_actual_usd'].map("$ {:,.2f}".format)
    activos['inversión_nueva']= activos['inversión_nueva'].map("$ {:,.2f}".format)
    activos['porcentaje_actual']= activos['porcentaje_actual'].map("{:,.2%}".format)
    activos['proporción_nueva']= activos['proporción_nueva'].map("{:,.2%}".format)
    activos['proporción_ideal']= activos['proporción_ideal'].map("{:,.2%}".format)
    activos['monto_invertir']= activos['monto_invertir'].map("$ {:,.2f}".format)
    activos['comisión_pagada']= activos['comisión_pagada'].map("$ {:,.2f}".format)


    orden_deseado = ["AVUS", "AVUV", "AVDE", "AVDV", "AVEM", "TOTAL"]

    activos['ticker'] = pd.Categorical(activos['ticker'], categories=orden_deseado, ordered=True)

    activos = activos.sort_values('ticker')


    print(tabulate(
        activos[['ticker',
                'inversion_actual_usd',
                'porcentaje_actual',
                'monto_invertir',
                'comisión_pagada',
                'inversión_nueva',
                'proporción_nueva',
                'proporción_ideal']],
        headers=['Ticker',
                 'Total Actual',
                 'Prop Actual',
                 'Monto Invertir',
                 'Comisión',
                 'Total Nuevo',
                 'Prop Nueva',
                 'Prop Ideal'], 
        tablefmt='rounded_grid',
        numalign='right',
        stralign='right',
        showindex=False
    ))

  
calcular_proporciones()

