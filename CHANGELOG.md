#[V3.0]
## 2026-02-18
### Agregado
- Se escribe documentación básica explicando la estrategia de inversión.
- Nuevos utils:
    - [acciones.py](/src/utils/acciones.py): Calcula las proporciones de los ETFs de acciones manteniendo la neutralidad geográfica según el ACWI.
    - [portafolio.py](/src/utils/portafolio.py): Obtiene los valores actuales de los activos, usando los datos de la base de datos con el último precio del mercado.
    - [demonios.py](/src/utils/demonios.py): Calcula la proporción de cada demonio según ciertas reglas definidas.
### Cambiado
- Rebalanceo ahora incluye los demonios.


#[V2.0]
## 2026-02-08
### Cambiado
- Ahora toda la lógica de rebalanceo se hace con los siguientes ETFs de Avantis:
    - [AVUS](https://www.avantisinvestors.com/avantis-investments/avantis-us-equity-etf/) reemplazando a [ITOT](https://www.blackrock.com/cl/productos/239724/ishares-core-sp-total-us-stock-market-etf)
    - [AVLV](https://www.avantisinvestors.com/avantis-investments/avantis-us-large-cap-value-etf/) reemplazando a [IUSV](https://www.blackrock.com/cl/productos/239715/ishares-russell-3000-value-etf),
    - [AVUV](https://www.avantisinvestors.com/avantis-investments/avantis-us-small-cap-value-etf/) reemplazando a [IJR](https://www.blackrock.com/cl/productos/239774/ishares-core-sp-smallcap-etf),
    - [AVDE](https://www.avantisinvestors.com/avantis-investments/avantis-international-equity-etf/) y [AVEM](https://www.avantisinvestors.com/avantis-investments/avantis-emerging-markets-equity-etf/) reemplazando a [IXUS](https://www.blackrock.com/cl/productos/244048/ishares-core-msci-total-international-stock-etf),
    - [AVDV](https://www.avantisinvestors.com/avantis-investments/avantis-international-small-cap-value-etf/) reemplazando a [SCZ](https://www.blackrock.com/cl/productos/239627/ishares-msci-eafe-smallcap-etf).
- Se refactoriza el código de rebalanceo para usar `pandas` en vez de listas de listas que ni Dios sabe cómo funcionaban.
- El script de [registrarMoviemiento](/scripts/registrarMovimiento.py) fue adaptado para que funcione mejor con el nuevo broker a utilizar.
- Se cambia la licencia MIT por la GNU GENERAL PUBLIC LICENSE V3.

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