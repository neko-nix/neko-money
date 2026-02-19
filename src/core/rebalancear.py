from src.utils.demonios import propporcionesPicantes
from src.utils.acciones import proporcionesAcciones
from src.utils.portafolio import valoresActuales
from src.utils import conversiones
import pandas as pd
from tabulate import tabulate
import numpy as np
import sys


import yfinance as yf

tickers_list = [
    "GC=F", "SI=F", "BTC-USD", "ETH-USD",
    "IAUM", "SLV", "IBIT", "ETHA", "PDBC",
    "AVUS", "AVLV", "AVUV", "AVDE", "AVDV", "DFIV", "AVEM", "AVES",
    "TLT"
]

import yfinance as yf

print("Descargando datos de mercado...")
df_precios = yf.download(tickers_list, period="5d", group_by='ticker', progress=False)

precios = {}
for t in tickers_list:
    try:
        series_close = df_precios[t]['Close']
        series_validas = series_close.dropna()
        if not series_validas.empty:
            precios[t] = series_validas.iloc[-1]
        else:
            print(f"⚠️ No hay datos para {t}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error crítico en {t}: {e}")
        sys.exit(1)


pGold   = precios["GC=F"]
pSilver = precios["SI=F"]
pBTC    = precios["BTC-USD"]
pETH    = precios["ETH-USD"]


print("Obteniendo Yield de TLT...")
tlt_obj = yf.Ticker("TLT")


y30 = tlt_obj.info.get('yield') or tlt_obj.info.get('dividendYield') or 0.04 


pGold = precios["GC=F"]
pSilver = precios["SI=F"]
pBTC = precios["BTC-USD"]
pETH = precios["ETH-USD"]

targetPicantes = propporcionesPicantes(y30,pGold,pSilver,pBTC,pETH)
print("")

targetAcciones = proporcionesAcciones()
print("")

pesoPicantes = targetPicantes["proporción_ideal"].sum()
pesoAcciones = 1 - pesoPicantes

targetAcciones["proporción_ideal"] *= pesoAcciones

targetTotal = pd.concat([targetAcciones,targetPicantes], ignore_index=True)

# Los ETFs para tu tabla
etf_list = ["AVUS", "AVLV", "AVUV", "AVDE", "AVDV", "DFIV", "AVEM", "AVES",
            "IAUM", "SLV", "IBIT", "ETHA", "PDBC", "TLT"]
etf_prices = {t: precios[t] for t in etf_list}


#print(etf_prices)


activos = valoresActuales(etf_prices)


activos = activos.sort_values('ticker')


#print(targetTotal)
#print(targetTotal["Proporción"].sum())

totalActualUSD = activos["totalUSD"].sum()

activos = pd.merge(activos,targetTotal, on="ticker", how="outer").fillna(0)
#print(f"Total Actual: {totalActual:,.2f}")


orden_deseado = ["AVUS", "AVLV", "AVUV", "AVDE", "DFIV", "AVDV", "AVEM", "AVES", "TLT", "IAUM", "SLV", "IBIT", "ETHA", "PDBC"]
activos['ticker'] = pd.Categorical(activos['ticker'], categories=orden_deseado, ordered=True)

# Montos a invertir
dolarObservado = conversiones.get_usd()
comisionBroker = max((dolarObservado*0.49)/100, 5)
dolarBroker = comisionBroker + dolarObservado

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


# Variación 
activos['variacionProporcion'] = (activos["proporcionActual"] - activos['proporción_ideal']) / activos['proporción_ideal']


# TOLERANCIA = input("¿Tolerancia? (15%): ")

# if TOLERANCIA == ""
#     TOLERANCIA = 0.15
# print(f"La tolerancia es {TOLERANCIA:.2%}")

TOLERANCIA = 0.15

def definir_estado(variacion):
    if variacion > TOLERANCIA:
        return "VENDER"
    elif variacion > TOLERANCIA/2:
        return "VIGILAR"
    elif variacion < -TOLERANCIA:
        return "COMPRAR"
    else:
        return "MANTENER"

activos['Status'] = activos['variacionProporcion'].apply(definir_estado)

# Inversión ideal
activos['inversion_ideal'] = (totalActualUSD+montoInvertirUSD)*activos['proporción_ideal']

activos['monto_comprar'] = np.where(activos['inversion_ideal'] - activos['totalUSD'] >  0, activos['inversion_ideal'] - activos['totalUSD'], 0)
activos['monto_vender']  = np.where(activos['inversion_ideal'] - activos['totalUSD'] <= 0, activos['inversion_ideal'] - activos['totalUSD'], 0)


# vender = input("¿Sólo ventas? (s/N): ")
# vender = vender.upper()
# if vender != "S":
#     print("Se va a COMPRAR y VENDER.\n")
#     activos['monto_vender']  = np.where(activos['inversion_ideal'] - activos['totalUSD'] <= 0, activos['inversion_ideal'] - activos['totalUSD'], 0)
# elif vender == "S":
#     print("Se va sólo VENDER.\n")
#     activos['monto_vender']  = 0



#activos['monto_vender']  = 0



#print(f"\nANTES DEL FILTRO")
#orden_deseado = ["AVUS", "AVLV", "AVUV", "AVDE", "DFIV", "AVDV", "AVEM", "AVES", "TOTAL"]
orden_deseado = ["AVUS", "AVLV", "AVUV", "AVDE", "DFIV", "AVDV", "AVEM", "AVES", "TLT", "IAUM", "SLV", "IBIT", "ETHA", "PDBC"]
activos['ticker'] = pd.Categorical(activos['ticker'], categories=orden_deseado, ordered=True)
activos = activos.sort_values('ticker')

for index, row in activos.iterrows():
    ticker = row['ticker']    
    if row['monto_comprar'] > 0:
        print(f"{ticker: <4} | 🟢 COMPRAR:  ${row['monto_comprar']:>9,.2f}")        
    elif row['monto_vender'] < 0:
        print(f"{ticker: <4} | 🔴 VENDER:   ${row['monto_vender']:>9,.2f}")
    else:
        print(f"{ticker: <4} | 🟡 MANTENER: ${row['monto_vender']:>9,.2f}")


totalComprar = activos['monto_comprar'].sum()
totalVender = activos['monto_vender'].sum()
print(f"Total Comprar: ${totalComprar:>9,.2f}\nTotal Vender:  ${totalVender:>9,.2f}\n")



# activos['monto_comprar'] = np.where(activos['variacionProporcion'].abs() > TOLERANCIA, activos['monto_comprar'], 0)
# activos['monto_vender']  = np.where(activos['variacionProporcion'].abs() > TOLERANCIA, activos['monto_vender'],  0)

# print(f"DESPUÉS DEL FILTRO")
# for index, row in activos.iterrows():
#     # Usamos el Ticker (asumiendo que es el index o una columna)
#     ticker = row['ticker'] # O index si el ticker es el índice del DF
    
#     if row['monto_comprar'] > 0:
#         print(f"{ticker: <4} | 🟢 COMPRAR:  ${row['monto_comprar']:>9,.2f}")
        
#     elif row['monto_vender'] < 0:
#         print(f"{ticker: <4} | 🔴 VENDER:   ${row['monto_vender']:>9,.2f}")
#     else:
#         print(f"{ticker: <4} | 🟡 MANTENER: ${row['monto_vender']:>9,.2f}")


# totalComprarFiltrado = activos['monto_comprar'].sum()
# totalVenderFiltrado = activos['monto_vender'].sum()
# print(f"Total Comprar: ${totalComprarFiltrado:>9,.2f}\nTotal Vender:  ${totalVenderFiltrado:>9,.2f}\n")

# print(f"DESPUÉS DEL AJUSTE")

# comprasMax = abs(totalVenderFiltrado) + montoInvertirUSD

# print(f"Compras máximas permitdas: ${comprasMax:,.2f}")
# activos['proporcionCompras'] = activos['monto_comprar'] / totalComprarFiltrado
# activos['monto_comprar'] = comprasMax * activos['proporcionCompras']

# totalComprarAjustado = activos['monto_comprar'].sum()
# totalVenderAjustado  = activos['monto_vender'].sum()
# print(f"Total Comprar: ${totalComprarAjustado:>9,.2f}\nTotal Vender:  ${totalVenderAjustado:>9,.2f}\n")

# for index, row in activos.iterrows():
#     # Usamos el Ticker (asumiendo que es el index o una columna)
#     ticker = row['ticker'] # O index si el ticker es el índice del DF
    
#     if row['monto_comprar'] > 0:
#         print(f"{ticker: <4} | 🟢 COMPRAR:  ${row['monto_comprar']:>9,.2f}")
        
#     elif row['monto_vender'] < 0:
#         print(f"{ticker: <4} | 🔴 VENDER:   ${row['monto_vender']:>9,.2f}")
#     else:
#         print(f"{ticker: <4} | 🟡 MANTENER: ${row['monto_vender']:>9,.2f}")



# if totalComprarFiltrado < abs(totalVenderFiltrado):

#     print("Las compras son más grandes que las ventas + monto a inyectar.")
#     print("Recalculando compras...")
#     comprasMax = abs(totalVenderFiltrado) + montoInvertirUSD

#     print(f"Compras máximas permitdas: ${comprasMax:,.2f}")
#     activos['proporcionCompras'] = activos['monto_comprar'] / totalComprarFiltrado
#     activos['monto_comprar'] *= activos['proporcionCompras']

#     print(f"DESPUÉS DEL RECÁLCULO")
#     for index, row in activos.iterrows():
#         # Usamos el Ticker (asumiendo que es el index o una columna)
#         ticker = row['ticker'] # O index si el ticker es el índice del DF
        
#         if row['monto_comprar'] > 0:
#             print(f"{ticker: <6} | COMPRAR:  ${row['monto_comprar']:>9,.2f}")
            
#         elif row['monto_vender'] < 0:
#             print(f"{ticker: <6} | VENDER:   ${row['monto_vender']:>9,.2f}")
#         else:
#             print(f"{ticker: <6} | MANTENER: ${row['monto_vender']:>9,.2f}")



activos['inversion_ideal'] = activos['inversion_ideal'] - activos['totalUSD']
inversionTotal = activos['inversion_ideal'].abs().sum()

def calcular_monto_final(row):
    # Si está fuera de las bandas, ejecutamos el monto ideal para corregir
    if (row['Status'] == "VENDER" or row['Status'] == "COMPRAR") and abs(row['inversion_ideal']) > 10:
        #print(row['Status'], row['inversion_ideal'])
        return row['inversion_ideal'], row['Status']
    return 0.0, "MANTENER"

#activos[['inversion_ideal', 'Status']] = activos.apply(calcular_monto_final, axis=1, result_type='expand')

#vuelto = inversionTotal - activos['inversion_ideal'].abs().sum()

#activos['inversion_ideal'] = activos['inversion_ideal'].clip(lower=0)

activos['prop_invertir'] = activos['inversion_ideal'] / activos['inversion_ideal'].abs().sum()

# Esto se hace para que el monto a invertir coincida con la plata que vamos a inyectar de verdad
#activos['monto_invertir'] = (activos['inversion_ideal'].abs().sum()+vuelto)*activos['prop_invertir']
activos['monto_invertir'] = activos['monto_comprar']+activos['monto_vender']
activos['comisión_pagada'] = abs(activos['monto_invertir']*proporcionComision)

#print(activos['prop_invertir'])
#print(activos['monto_invertir'])

#activos['cantidad_comprar'] = activos['monto_invertir']/activos["precio_actual_usd"]

# Cantidades nuevas estimadas
activos['inversión_nueva'] = activos['totalUSD']+activos['monto_invertir']
activos['proporción_nueva'] = activos['inversión_nueva'] / activos['inversión_nueva'].sum()


#orden_deseado = ["AVUS", "AVLV", "AVUV", "AVDE", "DFIV", "AVDV", "AVEM", "AVES", "TOTAL"]
orden_deseado = ["AVUS", "AVLV", "AVUV", "AVDE", "DFIV", "AVDV", "AVEM", "AVES", "TLT", "IAUM", "SLV", "IBIT", "ETHA", "PDBC", "TOTAL"]
activos['ticker'] = pd.Categorical(activos['ticker'], categories=orden_deseado, ordered=True)
activos = activos.sort_values('ticker')

totales = ['totalUSD', 'proporcionActual', 'proporción_ideal', 'variacionProporcion', 'monto_invertir', 'comisión_pagada', 'inversión_nueva', 'proporción_nueva']

activos.loc['TOTAL', totales] = activos[totales].sum()
activos.loc['TOTAL', 'ticker'] = 'TOTAL'
activos.loc['TOTAL'] = activos.loc['TOTAL'].fillna(0)

activos['totalUSD'] = activos['totalUSD'].map("$ {:,.2f}".format)
activos['inversión_nueva']= activos['inversión_nueva'].map("$ {:,.2f}".format)
activos['variacionProporcion']= activos['variacionProporcion'].map("{:,.2%}".format)
activos['proporcionActual']= activos['proporcionActual'].map("{:,.2%}".format)
activos['proporción_nueva']= activos['proporción_nueva'].map("{:,.2%}".format)
activos['proporción_ideal']= activos['proporción_ideal'].map("{:,.2%}".format)
activos['monto_invertir']= activos['monto_invertir'].map("$ {:,.2f}".format)
activos['comisión_pagada']= activos['comisión_pagada'].map("$ {:,.2f}".format)



print(tabulate(
    activos[['ticker',
            'totalUSD',
            'proporcionActual',
            'proporción_ideal',
            'variacionProporcion',
            'Status',
            'monto_invertir',
            'comisión_pagada',
            'inversión_nueva',
            'proporción_nueva']],
    headers=['Ticker',
                'Total',
                'Actual',
                'Ideal',
                'Variación',
                'Tipo',
                'Monto',
                'Comisión',
                'Nuevo',
                'Nueva'], 
    tablefmt='rounded_grid',
    numalign='right',
    stralign='right',
    showindex=False
))