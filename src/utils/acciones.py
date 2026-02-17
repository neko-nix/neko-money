import sqlite3
import yfinance as yf
from src.utils import conversiones
from src.utils.paths import DB_PATH, DATA_DIR
import pandas as pd
import numpy as np
from tabulate import tabulate
import time

def proporcionesAcciones():

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

    totalGlobal = proporcionUSA + proporcionDM + proporcionEM

    # Normalizar porque no siempre da 1 justo
    proporcionUSA /= totalGlobal
    proporcionDM /= totalGlobal
    proporcionEM /= totalGlobal

    proporcionesTickers = [
        ["AVUS", proporcionUSA/3],
        ["AVLV", proporcionUSA/3],
        ["AVUV", proporcionUSA/3],
        ["AVDE", proporcionDM/3],
        ["DFIV", proporcionDM/3],
        ["AVDV", proporcionDM/3],
        ["AVEM", proporcionEM/2],
        ["AVES", proporcionEM/2]
    ]

    columnas = ["ticker", "proporción_ideal"]
    dfTargets = pd.DataFrame(proporcionesTickers, columns=columnas)

    tabla_porcentajes = [[t, f"{p:.2%}"] for t, p in proporcionesTickers]

    print("")
    print(tabulate(tabla_porcentajes,
               headers=["Ticker", "Proporción"],
               tablefmt="rounded_grid",
               numalign='right',
               showindex=False,
               stralign='right'))
    return dfTargets