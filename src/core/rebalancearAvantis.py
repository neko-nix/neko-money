# Este script verifica la estrategia de inversión, y la compara con los valores actuales
# para determinar si es necesario hacer un rebalanceo.

import sqlite3
import yfinance as yf
from src.utils import conversiones
from src.utils.paths import DB_PATH, DATA_DIR
import pandas as pd
import numpy as np
from tabulate import tabulate
import time


holdingsACWI = DATA_DIR+"datosACWI.csv"
df = pd.read_csv(holdingsACWI, skiprows=9)


paises_desarrollados_ex_us = [
    'Japan', 'United Kingdom', 'France', 'Canada', 'Switzerland', 'Germany', 
    'Australia', 'Netherlands', 'Denmark', 'Sweden', 'Spain', 'Hong Kong', 
    'Italy', 'Singapore', 'Finland', 'Belgium', 'Norway', 'Israel', 'Ireland', 'Portugal'
]

paises_emergentes = [
    'China', 'India', 'Taiwan', 'Korea (South)', 'Brazil', 'Saudi Arabia', 
    'South Africa', 'Mexico', 'Thailand', 'Indonesia', 'Malaysia', 
    'United Arab Emirates', 'Qatar', 'Kuwait', 'Turkey', 'Philippines', 
    'Chile', 'Greece', 'Poland', 'Colombia', 'Peru', 'Egypt', 'Czech Republic'
]


proporcionDM = df[df['Location'].isin(paises_desarrollados_ex_us)]['Weight (%)'].sum() / 100
proporcionEM = df[df['Location'].isin(paises_emergentes)]['Weight (%)'].sum() / 100
proporcionUSA = (df[df['Location'] == 'United States']['Weight (%)'].sum()/100)

total_check = proporcionUSA + proporcionDM + proporcionEM

if total_check != 1:
    # Esto porque a veces no siempre da 1 exacto
    proporcionUSA /= total_check
    proporcionDM /= total_check
    proporcionEM /= total_check

proporcionesTickers = [
    ["AVUS", proporcionUSA/3],
    ["AVLV", proporcionUSA/3],
    ["AVUV", proporcionUSA/3],
    ["AVDE", proporcionDM*2/3],
    ["AVDV", proporcionDM/3],
    ["AVEM", proporcionEM]
]


for ticker, prop in proporcionesTickers:
    print(f"{ticker}, {prop:,.2%}")
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

    intentos = 0
    lista_tickers = activos['ticker'].unique().tolist()
    precios_actuales = None
    while intentos < 3:
        try:
            precios_data = yf.download(lista_tickers, period="1d", progress=False)['Close']
            precios_actuales = precios_data.iloc[-1] if len(precios_data.shape) > 1 else precios_data
            if precios_actuales.isnull().any():
                tickers_con_nan = precios_actuales[precios_actuales.isnull()].index.tolist()
                print(f"Intento {intentos + 1}: NaN detectado en {tickers_con_nan}. Reintentando...")
                intentos += 1
                time.sleep(2)
                continue
            break
        except Exception as e:
            print(f"Error de conexión: {e}")
            intentos += 1
            time.sleep(2)
    else:
        raise Exception(f"No se pudieron obtener todos los precios después de {intentos} intentos. Inténtelo más tarde.")


    
    #precios_data = yf.download(lista_tickers, period="1d", progress=False)['Close']
    #print(precios_data)
    #precios_actuales = precios_data.iloc[-1]

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
    comisionBroker = max((dolarObservado*0.49)/100, 5)
    dolarBroker = comisionBroker + dolarObservado
    #montoInvertirUSD = montoInvertirCLP/(dolarObservado+comisionBroker)

    while True:
        montoInvertirUSD = input("Ingrese monto a invertir en USD: ").strip()
        try:
            montoInvertirUSD = float(montoInvertirUSD)
            if montoInvertirUSD < 0:
                print("El monto no puede ser negativo.")
                continue
            break
        except ValueError:
            print(f"'{montoInvertirUSD}' no es un número válido. Inténtelo de nuevo.")
    
    print(f"Se van a invertir: ${montoInvertirUSD:,.2f}")

    montoInvertirCLP = montoInvertirUSD*(dolarObservado-comisionBroker)

    comisionPagada = montoInvertirUSD*comisionBroker
    proporcionComision = (dolarBroker-dolarObservado)/dolarObservado

    print(f"Precio Dólar Mercado: ${dolarObservado:,.2f}")
    print(f"Precio Dólar Broker: ${dolarObservado+comisionBroker:,.2f}")   

    print(f"Se van a inyectar ${montoInvertirUSD:,.2f} USD, ${montoInvertirCLP:,.0f} CLP")
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


    orden_deseado = ["AVUS", "AVLV", "AVUV", "AVDE", "AVDV", "AVEM", "TOTAL"]

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

