# Este script es para agregar nuevas compras en la cartera de inversión

import sqlite3
from datetime import datetime
import yfinance as yf
import requests


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
            if valor <= 0:
                print("El valor debe ser mayor a 0")
                continue
            return valor
        except ValueError:
            nombre_tipo = "entero" if tipo_esperado == int else "decimal"
            print(f"'{entrada}' no es un número {nombre_tipo} válido.")



TICKERS_VALIDOS = ["ITOT", "IUSV", "IJR", "IXUS", "SCZ"]
OPCIONES_VALIDAS = ["COMPRA", "VENTA"]
nombreDB = "nekoMoney.db"


ticker   = leer_dato(f"Ticker ({', '.join(TICKERS_VALIDOS)}): ", opciones=TICKERS_VALIDOS)
tipo     = leer_dato("¿Compra o Venta?: ", opciones=OPCIONES_VALIDAS)
fecha    = input(f"Fecha AAAA-MM-DD ({datetime.now().date()}): ") or str(datetime.now().date())
cantidad = leer_dato("Cantidad de acciones: ", tipo_esperado=int)
precio   = leer_dato("Precio unitario (CLP): ", tipo_esperado=float)
comision = leer_dato("Comisión total (CLP): ", tipo_esperado=float)

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


# Obtener el valor de la UF
fechaUF = datetime.strptime(fecha, "%Y-%m-%d").strftime("%d-%m-%Y")
url = f"https://mindicador.cl/api/uf/{fechaUF}"
print(f"Consultado valor UF para la fecha {fecha}...")
response = requests.get(url, timeout=5)
data = response.json()
if "serie" in data and len(data["serie"]) > 0:
    valorUF = float(data["serie"][0]["valor"])
else:
    print(f"No hay datos disponibles para la fecha {fecha}. Ingrese el valor manualmente.")

mensajeUF = f"Valor UF ({valorUF})" if valorUF else "Valor UF: "
uf = leer_dato(f"{mensajeUF}: ", tipo_esperado=float, sugerencia=valorUF)


# Valores equivalentes:
precioUSD   = round(precio / dolar,2)
comisionUSD = round(comision / dolar,2)

precioUF   = round(precio / uf,4)
comisionUF = round(comision / uf,4)

totalCLP = (cantidad * precio) + comision
totalUSD = round(totalCLP / dolar,2)
totalUF  = round(totalCLP / uf,2)



print(f"\n{'='*40}")
print("Se han registrado los siguientes datos:")
print(f"{'='*40}")
print(f"Ticker: {ticker}")
print(f"Tipo: {tipo}")
print(f"Fecha: {fecha}")
print(f"Cantidad: {cantidad}")
print(f"Precio por acción (CLP): ${precio}")
print(f"Comisión (CLP): ${comision}")
print(f"Total Invertido (CLP): ${totalCLP}")

print(f"{'-'*40}")
print("Equivalente en Dólares Estadounidenses")
print(f"{'-'*40}")
print(f"Dólar Observado: ${dolar}")
print(f"Preciopor acción (USD): ${precioUSD}")
print(f"Comisión (USD): ${comisionUSD}")
print(f"Total Invertido (USD): ${totalUSD}")

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
        conn = sqlite3.connect('nekoMoney.db')
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
            precio,
            comision,
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
                        print(f"{columnas[i]:<25}: {valor:>17,.0f}")
                else:
                    print(f"{columnas[i]:<25}: {valor:>17}")            
            print(f"{'='*40}")
        

    except Exception as e:
        print(f"\nError al guardar en la base de datos: {e}")
else:
    print("\nRegistro cancelado.")