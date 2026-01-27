#[V1.0]
## 2026-01-26
### Agregado
- Lógica de rebalanceo de activos según monto a inyectar, con discretización según valores actuales de cada ETF, y optimización del dinero sobrante.
- Cálculo automático de la proporción de mercado de EE.UU vs El resto del mundo, utilizando como proxy el ETF [iShares MSCI ACWI ETF](https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf).
- Módulo de obtención de datos de Dólar Observado y UF, con sistema de cache de 15 minutos para el dólar, y 1 día para el UF, con el fin de evitar consultar la web constantemente.

# [V0.1]
## 2026-01-15
### Added

### Changed
- Se cambia el nombre de `ganancias.py` a [valoresActuales.py](/src/core/valoresActuales.py) para mejor reflejar lo que hace.
- Se reestructura el [README.md](/README.md) para mostrar los features actuales (que ya están funcionando), y el roadmap de features que se quieren implementar.
### Removed


## 2026-01-14
- Script para calcular las proporciones objetivo y las actuales. [rebalancear](/rebalancear.py).
- Se reordena la estructura del proyecto para que esté más ordenado.
- Se agrega [paths.py](/src/utils/paths.py) para obtener dinámicamente el path de la base de datos, independientemente desde donde se ejecute el script.

- Se cambia el nombre de `ganancias.py` a [valoresActuales.py](/src/core/valoresActuales.py) para mejor reflejar lo que hace.
- Se reestructura el [README.md](/README.md) para mostrar una 

## 2026-01-13
- Script para calcular las proporciones objetivo y las actuales. [rebalancear](/rebalancear.py).

## 2026-01-11
- Crear ambiente de desarrollo con [flake.nix](flake.nix) en NixOS.
- Validación de datos de entrada (Tickers, tipos de cambio y precios).
- Automatización de tipo de cambio USD/CLP y UF vía API.
- Cálculo automático de equivalencias en CLP, USD y UF.
- Agregar los datos obtenidos en [registrarMovimiento.py](/datos/registrarMovimiento.py) a la base de datos [nekoMoney.db](/datos/nekoMoney.db).