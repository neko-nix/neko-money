# [V0.1]
## 2026-01-15
### Added

### Changed
- [x] Se cambia el nombre de `ganancias.py` a [valoresActuales.py](/src/core/valoresActuales.py) para mejor reflejar lo que hace.
- [x] Se reestructura el [README.md](/README.md) para mostrar los features actuales (que ya están funcionando), y el roadmap de features que se quieren implementar.
### Removed


## 2026-01-14
- [x] Script para calcular las proporciones objetivo y las actuales. [rebalancear](/rebalancear.py).
- [x] Se reordena la estructura del proyecto para que esté más ordenado.
- [x] Se agrega [paths.py](/src/utils/paths.py) para obtener dinámicamente el path de la base de datos, independientemente desde donde se ejecute el script.

- [x] Se cambia el nombre de `ganancias.py` a [valoresActuales.py](/src/core/valoresActuales.py) para mejor reflejar lo que hace.
- [x] Se reestructura el [README.md](/README.md) para mostrar una 

## 2026-01-13
- [x] Script para calcular las proporciones objetivo y las actuales. [rebalancear](/rebalancear.py).

## 2026-01-11
- [x] Crear ambiente de desarrollo con [flake.nix](flake.nix) en NixOS.
- [x] Validación de datos de entrada (Tickers, tipos de cambio y precios).
- [x] Automatización de tipo de cambio USD/CLP y UF vía API.
- [x] Cálculo automático de equivalencias en CLP, USD y UF.
- [x] Agregar los datos obtenidos en [registrarMovimiento.py](/datos/registrarMovimiento.py) a la base de datos [nekoMoney.db](/datos/nekoMoney.db).