import os
from pathlib import Path

# __file__ es la ubicación de este archivo (src/utils/paths.py)
# .parent es src/utils/
# .parent.parent es src/
# .parent.parent.parent es la raíz del proyecto (neko-money/)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Definimos las rutas importantes
DATA_DIR = str(ROOT_DIR)+"/data/"
DB_PATH = str(DATA_DIR)+"/nekoMoney.db"

# Tip pro: Asegurémonos de que la carpeta data existe para que no explote
def inicializar_carpetas():
    DATA_DIR.mkdir(exist_ok=True)


