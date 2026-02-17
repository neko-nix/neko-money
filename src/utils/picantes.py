import yfinance as yf
from tabulate import tabulate
import pandas as pd

def propporcionesPicantes(y30, pGold, pSilver, pBTC, pETH):

    # # Esto calcula los yields máximos y mínimos para TLT según el promedio de 200 días
    # histYield = yf.Ticker("^TYX").history(period="1y")['Close']
    # sma200Yield = histYield.tail(200).mean()
    # # Los yHigh y yLow tienen límites duros para evitar cálculos raros
    # yHigh = min(sma200Yield * 1.20, 4.5)
    # yLow = min(sma200Yield * 0.80, 2.5)

    # print(f"SMA200: {sma200Yield}")
    # print(f"High: {yHigh}, Low: {yLow}")
    # # Proporciones máximas y mínimas para el GSR
    # histGSR = yf.Ticker("^TYX").history(period="1y")['Close']
    # sma200GSR = histGSR.tail(200).mean()
    
    # Proporciones TLT
    tTLTMax = 0.10
    tTLTMin = 0.01
    ## Límites Altos y Bajos de Yields 10 años
    yHigh = 0.045
    yLow = 0.025

    # Proporciones sector Precious Metals
    tPM = 0.05
    tSilverMax = 0.80
    tSilverMin = 0.20
    ## Valores máximos y mínimos para el Gold Silver Ratio (GSR)
    GSRMax = 95
    GSRMin = 65

    # Proporciones sector Crypto
    tCrypto = 0.05
    tEtheMax = 0.80
    tEtheMin = 0.20
    ## Valores máximos y mínimos para el Ethereum Bitcoin Ratio (EBR)
    EBRMax = 0.075
    EBRMin = 0.035

    # Proporción Commodities
    tVacas = 0.05
    

    #y30 = (yf.Ticker("^TYX").history(period="1d")['Close'].iloc[-1]) / 100
    #y10 = (yf.Ticker("^TNX").history(period="1d")['Close'].iloc[-1]) / 100
    #r10 = 0.0186
    #ultimaVerificacion = "2026-02-12"

    #usuario = input(f"Ingrese el valor de la tasa real (al {ultimaVerificacion}: {r10:.2%}): ")
    #if usuario != "":
    #    tasaReal = float(usuario)


    #print(f"\nTasa nominal 30 años: {y30:.4%}")
    #print(f"Tasa nominal 10 años: {y10:.4%}")
    #print(f"Tasa real 10 años: {r10:.4%}")

    # Proporción de TLT
    if y30 < yLow:
        tTLT = tTLTMin
    elif y30 > yHigh:
        tTLT = tTLTMax
    else:
        # y = mx + b
        mTLT = (tTLTMax - tTLTMin) / (yHigh - yLow)
        bTLT = tTLTMax - mTLT * yHigh

        tTLT = mTLT* y30 + bTLT

    print(f"Yield High: {yHigh:.2%}, Yield Low: {yLow:.2%}")
    print(f"Yield TLT {y30:.2%}, Target TLT {tTLT:.2%}")


    # Proporciones Oro / Plata
    #pGold = yf.Ticker("GC=F").history(period="1d")['Close'].iloc[-1]
    #pSilver = yf.Ticker("SI=F").history(period="1d")['Close'].iloc[-1]

    GSR = pGold/pSilver

    print(f"\nGSR Max: {GSRMax}, GSR Min: {GSRMin}")
    print(f"Oro: ${pGold:,.2f} USD, Plata: ${pSilver:,.2f} USD")
    print(f"GSR: {GSR:,.2f}")

    if GSR >= GSRMax:
        tSilver = tSilverMax
    elif GSR <= GSRMin:
        tSilver = tSilverMin
    else:
        # y = mx + b
        mSilver = (tSilverMax - tSilverMin) / (GSRMax - GSRMin)
        bSilver = tSilverMax - mSilver * GSRMax

        tSilver = mSilver * GSR + bSilver
    tGold = 1 - tSilver    

    print(f"Oro {tGold:.2%}, Plata {tSilver:.2%}")

    tSilver *= tPM
    tGold *= tPM

    # Los commodities son fijos
    # tVacas = 0.05

    # Proporción Bitcoin Ethereum
    #pBTC = yf.Ticker("BTC-USD").history(period="1d")['Close'].iloc[-1]
    #pETH = yf.Ticker("ETH-USD").history(period="1d")['Close'].iloc[-1]

    EBR = pETH/pBTC

    print(f"\nEBR Max: {EBRMax}, EBR Min: {EBRMin}")
    print(f"Ethereum: ${pETH:,.2f} USD, Bitcoin: ${pBTC:,.2f} USD")
    print(f"EBR: {EBR:,.4f}")


    if EBR >= EBRMax:
        tEthe = tEtheMin
    elif EBR <= EBRMin:
        tEthe = tEtheMax
    else:
        # y = mx + b
        mEthe = (tEtheMax - tEtheMin) / (EBRMax - EBRMin)
        bEthe = tEtheMax - mEthe * EBRMax

        tEthe = mEthe * EBR + bEthe
    tBTC = 1 - tEthe   

    print(f"Ethereum {tEthe:.2%}, Bitcoin {tBTC:.2%}")

    tEthe *= tCrypto
    tBTC *= tCrypto

    #totalPicantes = tTLT + tSilver + tGold + tBTC + tEthe + tVacas
    #totalAcciones = 1-totalPicantes

    targets = [
        ["TLT", tTLT],
        ["IAUM", tGold],
        ["SLV", tSilver],
        ["IBIT", tBTC],
        ["ETHA", tEthe],
        ["PDBC", tVacas]
    ]
    columnas = ["ticker", "proporción_ideal"]
    dfTargets = pd.DataFrame(targets, columns=columnas)

    tabla_porcentajes = [[t, f"{p:.2%}"] for t, p in targets]

    print("")
    print(tabulate(tabla_porcentajes,
               headers=["Ticker", "Proporción"],
               tablefmt="rounded_grid",
               numalign='right',
               showindex=False,
               stralign='right'))
    #print(f"\nTotal Picantes: {totalPicantes:.2%}")
    #print(f"Total Acciones: {totalAcciones:.2%}")

    return dfTargets