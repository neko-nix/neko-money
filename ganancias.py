import sqlite3
import yfinance as yf
import conversiones

def calcular_ganancias():
    conn = sqlite3.connect('nekoMoney.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT ticker, 
               SUM(cantidad) as total_titulos, 
               SUM(total_clp) as inversion_total_clp,
               SUM(total_usd) as inversion_total_usd,
               SUM(total_uf) as inversion_total_uf
        FROM transacciones 
        GROUP BY ticker
    """)
    mis_activos = cursor.fetchall()
    
    total_cartera_clp = 0
    total_ganancia_clp = 0
    total_cartera_usd = 0
    total_ganancia_usd = 0
    total_cartera_uf = 0
    total_ganancia_uf = 0

    dolar = conversiones.get_usd()
    uf = conversiones.get_uf()

    #print(f"{'TICKER':<10} | {'CANT':<7} | {'PPC CLP':<12} | {'ACTUAL CLP':<12} | {'GANANCIA %':<10}")
    print("-" * 65)

    for ticker, cant, inv_clp, inv_usd, inv_uf in mis_activos:
        # 2. Obtenemos precio actual del mercado
        # Ojo: yfinance entrega USD, hay que multiplicarlo por el dólar actual 
        # o usar el precio en CLP si tuvieras un ticker local
        data = yf.Ticker(ticker)
        precio_actual_usd = data.fast_info['last_price']
        
        # Necesitamos el dólar actual para comparar peras con peras
        
        
        # 3. Cálculos
        ppa_usd = inv_usd / cant
        valor_actual_posicion_usd = cant * precio_actual_usd
        ganancia_usd = valor_actual_posicion_usd - inv_usd
        porcentaje_usd = (ganancia_usd / inv_usd) * 100

        precio_actual_clp = precio_actual_usd * dolar
        ppa_clp = ppa_usd * dolar
        valor_actual_posicion_clp = valor_actual_posicion_usd * dolar
        ganancia_clp = ganancia_usd * dolar
        porcentaje_clp = (ganancia_clp / inv_clp) * 100

        precio_actual_uf = precio_actual_clp / uf
        ppa_uf = ppa_clp / uf
        valor_actual_posicion_uf = valor_actual_posicion_clp / uf
        ganancia_uf = ganancia_clp / uf
        porcentaje_uf = (ganancia_uf / inv_uf) * 100
        
        print(f"{ticker:<10} | {cant:<7.0f} | {ppa_clp:>12,.0f} | {precio_actual_clp:>12,.0f} | {porcentaje_clp:>9.2f}%")
        #print(f"{ticker:<10} | {cant:<7.0f} | {ppa_uf:>12,.2f} | {precio_actual_uf:>12,.2f} | {porcentaje_uf:>9.2f}%")
        #print(f"{ticker:<10} | {cant:<7.0f} | {ppa_usd:>12,.2f} | {precio_actual_usd:>12,.2f} | {porcentaje_usd:>9.2f}%")
        
    conn.close()

# Ejecutar
calcular_ganancias()