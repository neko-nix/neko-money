import sqlite3
import yfinance as yf
from src.utils import conversiones
from src.utils.paths import DB_PATH

def obtener_estado_cartera():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT ticker, SUM(cantidad), SUM(total_clp), SUM(total_usd)
        FROM transacciones GROUP BY ticker HAVING SUM(cantidad) > 0
    """)
    mis_activos = cursor.fetchall()
    conn.close()

    if not mis_activos:
        return {}

    tickers = [a[0] for a in mis_activos]
    precios = yf.download(tickers, period="1d", progress=False)['Close'].iloc[-1]
    
    dolar = conversiones.get_usd()
    cartera = {}

    totalInvCLP = 0
    totalActCLP = 0
    totalUSD = 0

    print(f"\n{'TICKER':<10} | {'CANT':<7} | {'INVERTIDO CLP':<12} | {'ACTUAL CLP':<12} | {'DIF %':<8}")
    print("-" * 65)

    for ticker, cant, inv_clp, inv_usd in mis_activos:
        precio_usd = precios[ticker] if len(tickers) > 1 else precios
        
        valor_actual_clp = cant * precio_usd * dolar
        ganancia_clp = valor_actual_clp - inv_clp
        porcentaje = (ganancia_clp / inv_clp) * 100

        totalInvCLP += inv_clp
        totalActCLP += valor_actual_clp 
        #totalUSD += inv_usd

        print(f"{ticker:<10} | {cant:<7.0f} | {inv_clp:>12,.0f} | {valor_actual_clp:>12,.0f} | {porcentaje:>7.2f}%")


        cartera[ticker] = {
            'cantidad': cant,
            'valor_total_clp': valor_actual_clp,
            'porcentaje_en_cartera': 0 
        }

    ganancia_total_clp = totalActCLP - totalInvCLP
    porcentaje_total = (ganancia_total_clp / totalInvCLP) * 100
    
    print("-" * 65)
    print(f"{'TOTAL CARTERA':<10} | Invertido: CLP {totalInvCLP:>12,.0f}")
    print(f"{'':<13} | Actual:    CLP {totalActCLP:>12,.0f}")
    print(f"{'':<13} | Ganancia:  CLP {ganancia_total_clp:>12,.0f} ({porcentaje_total:.2f}%)")
    print("-" * 65)

    return cartera

if __name__ == "__main__":
    obtener_estado_cartera()