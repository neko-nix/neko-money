# Este script verifica la estrategia de inversión, y la compara con los valores actuales
# para determinar si es necesario hacer un rebalanceo.

import sqlite3
import yfinance as yf
from src.utils import conversiones
from src.utils.paths import DB_PATH, DATA_DIR
import pandas as pd


holdingsACWI = DATA_DIR+"datosACWI.csv"
df = pd.read_csv(holdingsACWI, skiprows=9)

proporcionUSA = (df[df['Location'] == 'United States']['Weight (%)'].sum()/100)

proporcionesTickers = {
    # Sector USA
    "ITOT": proporcionUSA/3,
    "IUSV": proporcionUSA/3,
    "IJR": proporcionUSA/3,
    # Sector Internacional
    "IXUS": 1-proporcionUSA,
    "SCZ": 0
}

print("Las proporciones objetivo son las siguientes:")

print(f"{'TICKER':<6} | {'PROP'}")
print("=" * 17)
for ticker, proporcion in proporcionesTickers.items():
    print(f"{ticker:<6} | {proporcion*100:>6.2f} %")
#tickersUSA = [["ITOT", 1/3],["IUSV",1/3],["IJR",1/3]]
#tickersINT = [["IXUS", propIXUS], ["IVLU",propIVLU], ["ISVL", propISVL], ["EVLU", propEVLU ]]



    
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

        precioUnitarioCLP = precio_actual_usd * dolar  
        #print(f"$ {precioUnitarioCLP:,.0f}")
        valor_actual_posicion_usd = cant * precio_actual_usd
        valor_actual_clp = valor_actual_posicion_usd * dolar

        totales.append([ticker,cant,inv_clp,valor_actual_clp,precioUnitarioCLP])

    conn.close()

    sumaFinal = 0
    sumaInicial = 0
    gananciaTotal = 0

    print(f"\n{'Ticker':<6} | {'Inv Inicial':<13} | {'Inv Final':<13} | {'Variación':<9}")
    print("=" * 54)

    for ticker, cantidad, invInicial, invActual, pua in totales:
        sumaFinal = invActual + sumaFinal
        sumaInicial = invInicial + sumaInicial
        variacion = (invActual-invInicial)/invInicial

        print(f"{ticker:<6} | $ {invInicial:>11,.0f} | $ {invActual:>11,.0f} | {variacion*100:>7.2f} %")
    
    gananciaTotal = (sumaFinal - sumaInicial) / sumaInicial
    print("-" * 54)
    print(f"{'TOTAL':<6} | $ {sumaInicial:>11,.0f} | $ {sumaFinal:>11,.0f} | {gananciaTotal*100:>7.2f} %")

    print("")
    print(f"Valor inicial de la cartera: {sumaInicial:>11,.0f} (100%)")
    print(f"Valor actual de la cartera: {sumaFinal:>12,.0f} ({(1+gananciaTotal)*100:<1.2f}%)")
    print(f"Variación de la cartera: {sumaFinal-sumaInicial:>15,.0f} ({gananciaTotal*100:.2f}%)")

    print("")
    #print("Las proporciones actuales son:")

    # REBALANCEO

    # Suma de lo que se agrega
    nuevaSuma = 0
    sumaSobrante = 0
    residuoCompra = []
    comprasTickers = []

    # Esta es la inversión mínima que define el broker para tener las comisiones más favorables
    # Esto puede variar con el tiempo, así que hay que estar atento a los cambios que se hagan.
    invMinima = (0.12*1.19*conversiones.get_uf()/(0.595/100))
    print(f"Inversión mínima para obtener las comisiones más favorables: ${invMinima:,.0f}")

    cantidadInyectar = input(f"Ingrese el monto a inyectar (${invMinima:,.0f}):")
    
    if cantidadInyectar == "":
        cantidadInyectar = invMinima
    else:
        cantidadInyectar = int(cantidadInyectar)
    print(f"Se van a inyectar ${cantidadInyectar:,.0f}\n")



    #print(f"{'Ticker':<6} | {'Inv Actual':<13} | {'Prop Actual':<11} | {'Agregar':<12} | {'Precio Unitario':<15} | {'Comprar':>7} | {'Sobrante':>10}")
    #print("=" * 100)

    for ticker, cantidad, invInicial, invActual, pua in totales:
        #if ticker != "SCZ":
        propoActual = invActual/sumaFinal       

        #print(f"{ticker} tiene ${invActual:,.0f}, y su proporción actual es {propoActual*100:.2f}%")

        totalNuevo = sumaFinal + cantidadInyectar

        invIdeal = proporcionesTickers[ticker]* totalNuevo
        diferencia = invIdeal - invActual

        if diferencia > 0:
            nuevaSuma += diferencia

            
            spreadBroker = (pua*1.5)/100

            cantidadComprarEstimada = (diferencia) / (pua+spreadBroker)
            montoCompraEstimado = int(cantidadComprarEstimada) * (pua+spreadBroker)

            comisionVariable = (montoCompraEstimado)*(0.595/100)

            comision = max(comisionVariable, 0.12*1.19*conversiones.get_uf())

            cantidadComprar = (diferencia - comision) / (pua+spreadBroker)
            fraccionAccion = cantidadComprar - int(cantidadComprar)

            if cantidadComprar < 1:                
                dineroSobrante = diferencia
                cantidadComprar = 0
            else:                
                dineroSobrante = fraccionAccion * (pua+spreadBroker)            

            sumaSobrante += dineroSobrante

            #residuoCompra.append([ticker,fraccionAccion])

            

            #print(f"{ticker:<6} | $ {invActual:>11,.0f} | {propoActual*100:>9.2f} % | $ {diferencia:>10,.0f} | $ {pua:>13,.0f} | {int(cantidadComprar):>7.0f} | $ {dineroSobrante:>8,.0f}")
            #print(f"A {ticker} se deben agregar ${diferencia:,.0f} para alcanzar su proporción ideal ({propDict[ticker]*100:.2f}%)")
            #print(f"{ticker} ahora tiene ${invActual+diferencia:,.0f} (Actual: ${invActual:,.0f} + Agregar: ${diferencia:,.0f})\n")

        else:
            diferencia = 0
            cantidadComprar = 0
            fraccionAccion = 0
            #comprasTickers.append([ticker, int(cantidadComprar), fraccionAccion])
            #print(f"{ticker:<6} | $ {invActual:>11,.0f} | {propoActual*100:>9.2f} % | $ {0:>10,.0f}")
            #print(f"A {ticker} no hay que agregarle nada, porque está sobreponderado.")
            #print(f"{ticker} se queda en ${invActual:,.0f}\n")

        comprasTickers.append([ticker, cantidad, invInicial, invActual, pua, int(cantidadComprar), dineroSobrante, fraccionAccion, propoActual, diferencia])
        print(f"Se van a comprar {int(cantidadComprar)} de {ticker}")

    
    sobraron = cantidadInyectar-nuevaSuma+sumaSobrante


    print(f"\nSobraron inicialmente: ${sobraron:,.0f}\n")
    #print(f"Sobró por discretización ${sumaSobrante:,.0f}")

    
    comprasTickers.sort(key=lambda x: x[7], reverse=True) 

    # Sólo se consideran los tickers que sí se iban a comprar, esto para evitar gastar más en comprar 1 sólo ticker
    # y pagando comisiones extra
    candidatos = [c for c in comprasTickers if c[5] > 0]

    for i in range(len(comprasTickers)):
        if comprasTickers[i][5] > 0:
            pua = comprasTickers[i][4]
            spread = (pua * 1.5) / 100
            costo_unidad = pua + spread

            # Para este cálculo sólo se considera comisión variable, porque se va a hacer una sóla compra del ticker
            # Y si la comisión fija ya se pagó antes, entonces sólo se paga la variable
            while sobraron >= (costo_unidad * 1.01):
                comprasTickers[i][5] += 1
                sobraron -= costo_unidad
                print(f"Con lo que sobró se va a agregar 1 {comprasTickers[i][0]}, para un total de {comprasTickers[i][5]}")

                break

    print("")
    print(f"{'Ticker':<6} | {'Inv Actual':<13} | {'Prop Actual':<11} | {'Agregar':<12} | {'Precio Unitario':<15} | {'Comprar':<7} | {'Inv Nueva':<12} | {'Prop Nueva':<11} | {'Prop Ideal':<10}")
    print("=" * 121)


    for ticker, cantidad, invInicial, invActual, pua, cantidadComprar, dineroSobrante, fraccionAccion, propoActual, diferencia in comprasTickers:
        spreadBroker = (pua*0.6)/100
        if int(cantidadComprar) > 0:
            invNuevaEstimada = int(cantidadComprar)*(pua+spreadBroker) + invInicial
        else:
            invNuevaEstimada = invActual

        propNuevaEstimada = invNuevaEstimada / (sumaFinal+cantidadInyectar-sobraron)
        print(f"{ticker:<6} | $ {invActual:>11,.0f} | {propoActual*100:>9.2f} % | $ {diferencia:>10,.0f} | $ {pua:>13,.0f} | {int(cantidadComprar):>7.0f} | ${invNuevaEstimada:>11,.0f} | {propNuevaEstimada*100:>9.2f} % | {proporcionesTickers[ticker]*100:.2f} %")


    print(f"\nInversión total nueva estimada: ${sumaFinal+cantidadInyectar-sobraron:,.0f}")
    print(f"\nSobró ${sobraron:.0f}")

    print("\nNOTA: Aunque un ticker esté sobreponderado, se calcula lo que se debe inyectar considerando TODOS LO QUE SE SUME A LOS OTROS TICKERS.")



calcular_proporciones()

