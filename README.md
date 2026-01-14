Sistema personal de seguimiento de inversiones en ETFs automático, utilizando las APIs de [Yahoo Finance](https://ranaroussi.github.io/yfinance/index.html), [Mindicador.cl](https://mindicador.cl/) y SQLite, optimizado para el mercado chileno y desarrollado sobre NixOS.

# Tareas Completas
- [x] Script para calcular las proporciones objetivo y las actuales. [rebalancear](/rebalancear.py).
- [x] Se reordena la estructura del proyecto para que esté más ordenado.
- [x] Se agrega [paths.py](/src/utils/paths.py) para obtener dinámicamente el path de la base de datos, independientemente desde donde se ejecute el script.

Todos los cambios se encuentran en [CHANGELOG](/CHANGELOG.md)

# Pendientes
- [ ] Script que sea capaz de obtener las proporciones del mercado estadounidense comparado con el resto de mundo basándose en el indicador MSCI ACWI.
- [ ] Crear script que indice el rebalanceo de los ETFs según la estrategia de inversión y las cantidades actuales.
- [ ] Obtener los valores actuales de los ETFs, y calcular ganancias en CLP, USD y UF.
- [ ] Obtener valores históricos de los ETFs y sus equivalentes en CLP, USD y UF.
- [ ] Generar gráficos de la variación de los precios.
- [ ] Proyecciones: Implementar módulo de interés compuesto basado en el promedio de depósitos históricos y diferentes escenarios de rentabilidad.


# Entorno en NixOS
Para activar el entorno de desarrollo, descargando e instalando todas sus dependencias, se requiere utilizar NixOS, y ejecutar el siguiente comando:
```sh
nix develop
```

# Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
