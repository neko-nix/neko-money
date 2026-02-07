# Neko-Money 🐱💸
![Python](https://img.shields.io/badge/python-3.12+-orange?logo=python&logoColor=white) 
![NixOS](https://img.shields.io/badge/NixOS-blue?logo=nixos&logoColor=white&color=5277C3)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?logo=sqlite&logoColor=white)
![Version](https://img.shields.io/badge/version-2.0-brightgreen)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Last Commit](https://img.shields.io/github/last-commit/neko-nix/neko-money)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/neko-nix/neko-money)
![GitHub issues](https://img.shields.io/github/issues/neko-nix/neko-money?color=informational)

Sistema personal de seguimiento de inversiones en ETFs automático, utilizando las APIs de [Yahoo Finance](https://ranaroussi.github.io/yfinance/index.html), [Mindicador.cl](https://mindicador.cl/) y SQLite, optimizado para el mercado chileno y desarrollado sobre NixOS.

## Features Actuales
- **Gestión de Movimientos:** Registro en SQLite de compras, ventas y comisiones de cada transacción en CLP, y cálculo automático de equivalentes en USD y UF.
- **Valor Actual de Inversión:** Cálculo de ganancias/pérdidas del portafolio invertido a la fecha actual.
- **Entorno Nix:** Ambiente de desarrollo reproducible mediante [flake.nix](/flake.nix) sin tener que depender de documentos tipo `requierements.txt`.
- **[Rebalanceo de Activos (PR #8)](https://github.com/neko-nix/neko-money/pull/8):** Lógica de flujo de caja basada en el índice MSCI ACWI.

## Roadmap (Próximos Pasos)
- **[Documentación de Estrategia de Inversión (Issue #3)](https://github.com/neko-nix/neko-money/issues/3)**: Documentar y explicar la estrategia de inversión.
- **Análisis Visual:** Generar gráficos de distintos tipos para analizar visualmente el comportamiento del portafolio.
- **Análisis de Componentes:** Scrapping de los componentes internos de cada ETF, y generar un análisis detallado de las posiciones, geografía, industrias, etc, del portafolio.
- **Notificaciones Telegram:** Enviar resúmenes diarios, semanales, mensuales y/o anuales del comportamiento del portafolio.
- **Históricos:** Guardar datos históricos del portafolio, para poder hacer análisis en el tiempo.
- **Proyecciones:** Implementar distintos tipos de proyecciones para el portafolio.
- **Comparaciones:** Comparar los resultados del portafolio con otros utilizados comúnmente, y ver sus diferencias.

Todos los cambios se encuentran en [CHANGELOG](/CHANGELOG.md)

## Entorno en NixOS
Para activar el entorno de desarrollo, descargando e instalando todas sus dependencias, se requiere utilizar NixOS, y ejecutar el siguiente comando estando en el directorio del proyecto:
```sh
nix develop
```

## Estructura del proyecto:
```text
├── data                            # Base de datos, no versionada
│   └── nekoMoney.db                
├── docs
├── scripts                         # Scripts de automatización
│   └── registrarMovimiento.py
├── src                             # Núcleo del programa
│   ├── core                        # Lógica matemática y financiera
│   │   ├── rebalancear.py
│   │   └── valoresActuales.py
│   ├── database                    # Gestión de base de datos
│   │   └── crearDB.py
│   └── utils                       # Herramientas y rutas dinámicas
│       ├── conversiones.py
│       ├── etfData.py
│       └── paths.py
├── tests                           # Validación de cálculos
└── flake.nix                       # Entorno NixOS reproducible
```

## Licencia
Este proyecto está bajo la Licencia GNU GENERAL PUBLIC LICENSE V3. Consulta el archivo [LICENSE](LICENSE) para más detalles.