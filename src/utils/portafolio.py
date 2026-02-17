import sqlite3
import yfinance as yf
from src.utils.paths import DB_PATH, DATA_DIR
import pandas as pd
from tabulate import tabulate

def valoresActuales(precios):

    conn = sqlite3.connect(DB_PATH)
    query = "SELECT ticker, SUM(cantidad) as cantidad FROM transacciones GROUP BY ticker"
    df = pd.read_sql_query(query, conn)
    conn.close()

    #dfTickersCompletos = pd.DataFrame(tickers, columns=["ticker"])
    #df = pd.merge(df,dfTickersCompletos, on="ticker", how="outer").fillna(0)
    
    # Obtener precios actuales
    #print(f"Descargando precios para {len(tickers)} activos...")

    # Mapear precios
    df['unitarioUSD'] = df['ticker'].map(precios)
    df['totalUSD'] = df['cantidad'] * df['unitarioUSD']
    df["proporcionActual"] = df["totalUSD"] / df["totalUSD"].sum()


    print(tabulate(df,
               headers=["Ticker", "Cantidad", "Precio USD", "Total USD", "Proporción Actual"],
               tablefmt="rounded_grid",
               numalign='right',
               showindex=False,
               stralign='right'))
    
    return df