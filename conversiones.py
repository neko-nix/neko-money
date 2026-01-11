import yfinance as yf
import requests
from datetime import datetime, date, timedelta
import sqlite3

pathDB = "nekoMoney.db"


def get_db_value(indicador):
    conn = sqlite3.connect(pathDB)
    cursor = conn.cursor()
    cursor.execute("SELECT valor, last_update FROM cache_indicadores WHERE indicador = ?", (indicador,))
    res = cursor.fetchone()
    conn.close()
    return res

def save_db_value(indicador, valor):
    conn = sqlite3.connect(pathDB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO cache_indicadores (indicador, valor, last_update) 
        VALUES (?, ?, ?)
    """, (indicador, valor, datetime.now()))
    conn.commit()
    conn.close()

def get_usd():
    cached = get_db_value('USD')
    # Si existe y tiene menos de 15 minutos de antigüedad
    if cached and datetime.strptime(cached[1], '%Y-%m-%d %H:%M:%S.%f') > datetime.now() - timedelta(minutes=15):
        return cached[0]
    
    # Si no, ir a Yahoo
    print("Obteniendo valor del Dólar Observado de hoy...")
    nuevo_valor = yf.Ticker("CLP=X").fast_info['last_price']
    save_db_value('USD', nuevo_valor)
    return nuevo_valor

def get_uf():
    cached = get_db_value('UF')
    # Si existe y es de hoy (la UF cambia a las 00:00)
    if cached and datetime.strptime(cached[1], '%Y-%m-%d %H:%M:%S.%f').date() == datetime.date(datetime.now()):
        return cached[0]
    
    # Si no, ir a la API
    print("Obteniendo el valor de la UF de hoy...")
    url = "https://mindicador.cl/api/uf"
    nuevo_valor = requests.get(url).json()['serie'][0]['valor']
    save_db_value('UF', nuevo_valor)
    return nuevo_valor

if __name__ == "__main__":
    print(f"Dólar: {get_usd()}")
    print(f"UF: {get_uf()}")