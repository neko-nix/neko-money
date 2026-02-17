# Este script es para agregar nuevas compras en la cartera de inversión

import sqlite3
from datetime import datetime
import yfinance as yf
import requests
from src.utils.paths import DB_PATH


def leer_dato(prompt, tipo_esperado=float, opciones=None, sugerencia=None):
    while True:

        entrada = input(prompt).strip()

        if entrada == "" and sugerencia is not None:
            return sugerencia
        
        if opciones:
            entrada = entrada.upper()
            if entrada in opciones:
                return entrada
            print(f"Error. Opciones válidas: {', '.join(opciones)}")
            continue

        try:
            valor = tipo_esperado(entrada.replace(",", "."))
            if valor < 0:
                print("El valor debe ser mayor a 0")
                continue
            return valor
        except ValueError:
            nombre_tipo = "entero" if tipo_esperado == int else "decimal"
            print(f"'{entrada}' no es un número {nombre_tipo} válido.")




TICKERS_VALIDOS = [ "IAUM", "SLV", "IBIT", "ETHA", "PDBC",  # Metales y Crypto
                    "AVUS", "AVLV", "AVUV", "AVDE", "AVDV", "DFIV", "AVEM", "AVES", # ETFs Avantis/DFA
                    "TLT"] # Para el Yield

OPCIONES_VALIDAS = ["COMPRA", "VENTA"]


ticker   = leer_dato(f"Ticker ({', '.join(TICKERS_VALIDOS)}): ", opciones=TICKERS_VALIDOS)
tipo     = leer_dato("¿Compra o Venta?: ", opciones=OPCIONES_VALIDAS)
fecha    = input(f"Fecha AAAA-MM-DD ({datetime.now().date()}): ") or str(datetime.now().date())
totalUSD = leer_dato("Monto invertido (USD): ", tipo_esperado=float)

if tipo == "VENTA":
    totalUSD *= -1

precioUSD   = leer_dato("Precio unitario (USD): ", tipo_esperado=float)
cantidad = totalUSD/precioUSD



# Obtener el valor del dólar
dolarObservado = None

print(f"Consultando dólar observado para la fecha {fecha}...")
dolarHistorico = yf.Ticker("CLP=X")
hist = dolarHistorico.history(start=fecha, period="5d")    
if not hist.empty:
    dolarObservado = round(hist.iloc[0]['Close'], 2)
else:
    print(f"No hay datos disponibles para la fecha {fecha}. Ingrese el valor manualmente.")


mensajeDolar = f"Dólar Observado ({dolarObservado}): " if dolarObservado else "Dólar Observado: "
dolar = leer_dato(mensajeDolar, tipo_esperado=float, sugerencia=dolarObservado)
dolarBroker = dolar + max(dolar*0.49/100, 5)

comisionProporcional = (dolarBroker-dolar)/dolar
comisionEstimada = totalUSD*comisionProporcional
comisionUSD = leer_dato(f"Comisión total USD (${comisionEstimada:,.2f}): ", tipo_esperado=float, sugerencia=comisionEstimada)

# Obtener el valor de la UF
fechaUF = datetime.strptime(fecha, "%Y-%m-%d").strftime("%d-%m-%Y")
url = f"https://mindicador.cl/api/uf/{fechaUF}"
print(f"Consultado valor UF para la fecha {fecha}...")
response = requests.get(url, timeout=50)
data = response.json()
if "serie" in data and len(data["serie"]) > 0:
    valorUF = float(data["serie"][0]["valor"])
else:
    print(f"No hay datos disponibles para la fecha {fecha}. Ingrese el valor manualmente.")

mensajeUF = f"Valor UF ({valorUF})" if valorUF else "Valor UF: "
uf = leer_dato(f"{mensajeUF}: ", tipo_esperado=float, sugerencia=valorUF)

# uf = 39716.32
# print(f"Valor Uf: {uf}")

# Valores equivalentes:
precioCLP   = precioUSD*dolar
comisionCLP = comisionUSD*dolar

precioUF   = precioCLP/uf
comisionUF = comisionCLP/uf

totalCLP = totalUSD*dolar
totalUF  = totalCLP/uf


print(f"\n{'='*40}")
print("Se han registrado los siguientes datos:")
print(f"{'='*40}")
print(f"Ticker: {ticker}")
print(f"Tipo: {tipo}")
print(f"Fecha: {fecha}")
print(f"Cantidad: {cantidad}")
print(f"Dólar Observado: ${dolar}")
print(f"Precio por acción (USD): ${precioUSD}")
print(f"Comisión (USD): ${comisionUSD}")
print(f"Total Invertido (USD): ${totalUSD}")

print(f"{'-'*40}")
print("Equivalente en Pesos Chilenos")
print(f"{'-'*40}")

print(f"Precio por acción (CLP): ${precioCLP}")
print(f"Comisión (CLP): ${comisionCLP}")
print(f"Total Invertido (CLP): ${totalCLP}")

print(f"{'-'*40}")
print("Equivalente en Unidad de Fomento")
print(f"{'-'*40}")

print(f"Valor UF: UF{uf}")
print(f"Precio por acción (UF): UF{precioUF}")
print(f"Comisión (UF): UF{comisionUF}")
print(f"Total Invertido (UF): UF{totalUF}")
print(f"{'='*40}")



# Guardar los datos en el .db

confirmar = input("\n¿Guardar este movimiento en la base de datos? (s/n): ").lower()

if confirmar == 's':
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        query = """
        INSERT INTO transacciones (
            ticker, tipo, fecha, cantidad,
            precio_ejecucion_clp, comision_clp, total_clp,
            dolar_observado, precio_ejecucion_usd, comision_usd, total_usd,
            valor_uf, precio_ejecucion_uf, comision_uf, total_uf
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        datos = (
            ticker,
            tipo.lower(),
            fecha,
            cantidad,
            precioCLP,
            comisionCLP,
            totalCLP,
            dolar,
            precioUSD,
            comisionUSD,
            totalUSD,
            uf,
            precioUF,
            comisionUF,
            totalUF
        )

        cursor.execute(query, datos)
        ultimoIngresado = cursor.lastrowid     
        conn.commit()        

        cursor.execute("SELECT * FROM transacciones WHERE id = ?", (ultimoIngresado,))
        f = cursor.fetchone()  
        columnas = [descripcion[0] for descripcion in cursor.description]
        conn.close()

        if f:
            print(f"\n{'='*40}")
            print(f"\nEl siguiente movimiento ha sido registrado en nekoMoney.db (ID: {f[0]})")
            print(f"{'='*40}")
            
            for i in range(len(columnas)):
                valor = f[i]
                if isinstance(valor, float):
                    valor_espaciado = f"{valor:,.2f}".replace(",", " ")
                    if "clp" in columnas[i]:                        
                        print(f"{columnas[i]:<25}: CLP {valor_espaciado:>13}")
                    elif "usd" in columnas[i]:
                        print(f"{columnas[i]:<25}: USD {valor_espaciado:>13}")
                    elif "uf" in columnas[i]:
                        print(f"{columnas[i]:<25}: UF {valor_espaciado:>14}")
                    elif "cantidad" in columnas[i]:
                        print(f"{columnas[i]:<25}: {valor_espaciado:>17}")
                else:
                    print(f"{columnas[i]:<25}: {valor:>17}")            
            print(f"{'='*40}")
        

    except Exception as e:
        print(f"\nError al guardar en la base de datos: {e}")
else:
    print("\nRegistro cancelado.")