
Después de HORAS de análisis, podemos concluir lo siguiente:
1. IJR > IWN
	1. Si bien IJR es small cap tipo blend, el filtro del S&P ayuda a evitar los value traps que podrían hacer que el fondo sea terrible. Además, incluso si no tiene la prima de Small Cap Value (por ser Blend), su bajo costo justifica su uso.
	2. IWN por su parte, aparte de ser caro, no tiene ningún filtro para evitar empresas zombies y medio muertas, por lo que hace que el fondo esté lleno de trampas de valor que hacen que tenga un pésimo desempeño, incluso comparado con un Small Cap Blend como IJR
2. Los ETFs de factores no valen la pena:
	1. Si bien podrían utilizarse para abarcar factores que normalmente sería más difícil de exponerse, sus altos costos hacen que sus desempeños sean mediocres en el peor de los casos, y peor que un fondo "normal" que capture los factores de forma más indirecta.
3. SCZ no vale la pena por su costo:
	1. Si bien SCZ podría ser una buena opción para exponerse a Small Caps (Blend) en mercados desarrollados, su alto costo (0.40%) hacen que no valga la pena. Si bien la prima es real, y técnicamente paga su costo alto, la diferencia es tan poca, que simplemente no resulta muy útil añadirle complejidad al portafolio (porque habría que compensar SCZ, que son sólo DM, con IEMG, para quedar neutral geográficamente entre DM y EM) por una ganancia tan minúscula que podría perfectamente ser ruido en los datos.
	2. Si SCZ bajara sus costos (<= 0.15%), o si hubiese alguna otra alternativa de Small Caps internacionales, (o aún mejor, Small Caps Value Internacional), entonces ahí si podría ser, pero por ahora no.


¿Qué opinas de esta estrategia de inversión?

Suponte una estrategia de inversión de acciones globales con tilts hacia value y small cap.
Tus objetivos son maximizar el rendimiento lo más posible, incluso si eso significa no utilizar los tilts. 
El horizonte de inversión son de 30 años.
No tienes restricción en la cantidad de tickers, puedes elegir todos los que quieras, o incluso sólo 1.
La única restricción es que las proporciones de USA vs Internacional sean proporcional a sus respectivos tamaños, esto a la fecha actual, corresponde a 64% USA y 36% Internacional aproximadamente.
También considera que para rebalancear los activos, NUNCA VENDER, sólo compras de más de lo que hace falta. Esto para evitar pago de impuestos y cobro de comisiones al vender.


Tickers disponibles, costos anuales, y benchmark:

| Ticker | Costo Anual | Benchmark                                                   | ¿Disponible? | Elegido  | Fallback de | Razón                                                                                                                                                                                                                                                                                                                          |
| ------ | ----------- | ----------------------------------------------------------- | ------------ | -------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ITOT   | 0.03%       | S&P Total Market Total Return Index                         | Si           | Siempre  |             | El fondo es muy barato, e incluye todo el mercado estadounidense, lo cuál es útil para evitar estar concentrados sólo en factores                                                                                                                                                                                              |
| IUSV   | 0.04%       | S&P 900 Value Total Return Index                            | Si           | Siempre  |             | La mejor opción de bajo costo, filtro S&P, exposición a Value Large y Mid Cap de USA.                                                                                                                                                                                                                                          |
| IXUS   | 0.07%       | MSCI ACWI ex USA IMI Index                                  | Si           | Siempre  |             | La mejor opción de bajo costo a exposición a mercados desarrollados y emergentes, incluye Large, Mid y Small Cap. Tipo Blend                                                                                                                                                                                                   |
| IEMG   | 0.09%       | MSCI Emerging Markets Investable Market Index               | Si           | No       |             | IXUS de por sí ya tiene un 30% de emergentes (al 2026), y sobreponderar emergentes blend no aporta una prima real, como lo sería con small cap value.<br><br>Sólo utilizar si no tienes IXUS, y no tienes exposición a emergentes de alguna otra forma                                                                         |
| ISCV   | 0.06%       | Morningstar US Small Cap Broad Value Extended Index         | No           | Siempre  |             | La mejor opción para capturar Small Cap Value USA con costos bajos.                                                                                                                                                                                                                                                            |
| IJS    | 0.18%       | S&P SmallCap 600(R) Value Index                             | No           | Fallback | ISCV        | Sólo si no hay mejores opciones disponibles como ISCV                                                                                                                                                                                                                                                                          |
| IJR    | 0.06%       | S&P 600 Small Cap TR Index                                  | Si           | Fallback | IJS         | Sólo si no hay mejores opciones disponibles como IJS o ISCV, ya que este es Small cap Blend, aunque tiene el filtro S&P.                                                                                                                                                                                                       |
| IJH    | 0.05%       | S&P 400 Mid Cap Gross TR Index                              | Si           | Fallback | ILCV        | IUSV ya contiene Mid Caps, que además son sólo value, mientras que este es mid cap blend, las cuales incluyen mid cap growth que diluyen los mid caps value de IUSV.<br><br>Sólo vale la pena si ni IUSV, ni ILCV están disponibles, y tienes que hacer ITOT + IJH para mitigar un poco la concentración a large caps de itot. |
| SCZ    | 0.40%       | MSCI EAFE Small Cap Index                                   | Si           | No       |             | Small caps internacionales de por si no aportan una prima relevante, tiene que tener algún tipo de filtro, o tener otro factor, como value.<br><br>Además está re caro                                                                                                                                                         |
| IVE    | 0.18%       | S&P 500 Value TR Index                                      | Si           | No       |             | Costo alto cuando existe alternativa más barata (IUSV)                                                                                                                                                                                                                                                                         |
| VLUE   | 0.15%       | MSCI USA Enhanced Value Index                               | Si           | No       |             | Costo alto cuando existe alternativa más barata (IUSV), y además utiliza "ingeniería quant", que a veces es un desastre.                                                                                                                                                                                                       |
| IWM    | 0.19%       | Russell 2000 Index                                          | Si           | No       |             | Costo alto, con muchas empresas "zombies" cuando existe alternativa más barata y con filtro de calidad del S&P (IJR)                                                                                                                                                                                                           |
| IWN    | 0.24%       | Russell 2000 Value Index                                    | Si           | No       |             | Costo alto, con muchas empresas "zombies", y "value traps" (empresas baratas que lo son porque están mal financieramente).                                                                                                                                                                                                     |
| EWZS   | 0.59%       | MSCI Brazil Small Cap Index                                 | Si           | No       |             | Costo alto, y sobre-exposición a un sólo país                                                                                                                                                                                                                                                                                  |
| ECNS   | 0.59%       | MSCI China Small Cap Index                                  | Si           | No       |             | Costo alto, y sobre-exposición a un sólo país                                                                                                                                                                                                                                                                                  |
| SCJ    | 0.50%       | MSCI Japan Small Cap Index                                  | Si           | No       |             | Costo alto, y sobre-exposición a un sólo país                                                                                                                                                                                                                                                                                  |
| IWD    | 0.18%       | Russell 1000 Value Index                                    | Si           | No       |             | Costo alto cuando existe alternativa más barata y con filtro de calidad del S&P (IUSV)                                                                                                                                                                                                                                         |
| IWS    | 0.23%       | Russell MidCap Value Index                                  | Si           | No       |             | Costo alto cuando existe alternativa más barata y con filtro de calidad del S&P (IMCV)                                                                                                                                                                                                                                         |
| ACWI   | 0.32%       | MSCI ACWI Index                                             | Si           | No       |             | Costos altos que pueden evitarse usando ITOT + IXUS.En el caso ultra extremo que no existan ninguna otra opción internacional, ni factores value o small cap de USA, ahí recién pensar en QUIZÁS incluir ACWI.                                                                                                                 |
| IJJ    | 0.18%       | S&P MidCap 400(R) Value Index                               | No           | No       |             | El costo es muy alto, y la prima Mid Cap Value no es tan alta para justificar el costo.                                                                                                                                                                                                                                        |
| IMCV   | 0.06%       | Morningstar US Mid Cap Broad Value Index                    | No           | No       |             | Si bien es tipo value, la prima en los mid caps value no son la gran cosa, así que es preferible invertir en otras cosas a sobreponderar más mid cap value.                                                                                                                                                                    |
| ILCV   | 0.04%       | Morningstar US Large-Mid Cap Broad Value Index              | No           | Fallback | IUSV        | Sólo si no está IUSV disponible, porque son básicamente lo mismo, y tienen el mismo costo, pero IUSV es de la familia 'CORE' de iShares, y tiene el filtro S&P.                                                                                                                                                                |
| IVV    | 0.03%       | S&P 500 Index                                               | Si           | Fallback | ITOT        | Sólo si ni EUSA, ni ITOT están disponible.                                                                                                                                                                                                                                                                                     |
| EFA    | 0.32%       | MSCI EAFE Index                                             | Si           | Fallback | ACWX        | Sólo si ni IXUS ni IDEV ni IEFA están disponible                                                                                                                                                                                                                                                                               |
| IEFA   | 0.07%       | MSCI EAFE IMI Index                                         | No           | Fallback | IDEV        | Sólo si ni IXUS ni IDEV están disponible                                                                                                                                                                                                                                                                                       |
| IDEV   | 0.04%       | MSCI WORLD ex USA IMI                                       | No           | Fallback | IXUS        | Si bien tiene costos más bajos que IXUS, no incluye mercados emergentes, por lo que tendrías que sobreponderar IEMG, así que al final quedas con los mismos costos.Sólo si IXUS no está disponible                                                                                                                             |
| ACWX   | 0.32%       | MSCI ACWI ex-US Index                                       | Si           | Fallback | IEFA        | En teoría mejor que EFA, a pesar de tener los mismos costos, porque ACWX incluye mercados emergentes.Sólo si ni IXUS, ni IDEV, ni IEFA, ni EFA están disponibles.                                                                                                                                                              |
| EUSA   | 0.09%       | MSCI USA Equal Weighted Index                               | No           | No       |             | Al ser un fondo tipo Equal Weight, es una opción bastante rara la verdad, pero como está muy cargado hacia los midcaps, la mejor opción sería usar ITOT + IJH en ese caso, que es más barato.                                                                                                                                  |
| IWC    | 0.60%       | Russell Microcap Index                                      | Si           | No       |             | No sólo es carísimo, si no que también es parte de los índices de Russell (filtros mínimos). Vaya a saber uno que monstruosidades hay aquí.                                                                                                                                                                                    |
| WSML   | 0.30%       | MSCI World Small Cap Index                                  | No           | No       |             | Si bien es mejor que SCZ en costo, el factor value por si solo no es muy útil, tiene que ser un small cap "limpio", sin small cap growth, ni empresas zombies                                                                                                                                                                  |
| EFV    | 0.31%       | MSCI EAFE Value Index                                       | No           | Fallback | IVLU        | Medio caro, pero aporta Value en países desarrollados EX USA, lo cual si tiene una prima real.<br><br>Utilizar sólo si IVLU no está disponible                                                                                                                                                                                 |
| IVLU   | 0.31%       | MSCI World ex USA Enhanced Value Index                      | No           | Si       |             | Básicamente lo mismo que EFV, pero ligeramente mejor por el enhanced value                                                                                                                                                                                                                                                     |
| EWJV   | 0.15%       | MSCI Japan Value Index                                      | No           | No       |             | Si bien es un fondo de un sólo país, aporta factor Value, y más encima es más barato que EFV y IVLU, que ya incluyen Japón de por si, sin embargo, lo ideal es evitar apuestas concentradas a un sólo país                                                                                                                     |
| ISVL   | 0.31%       | FTSE Developed ex US ex Korea Small Cap Focused Value Index | No           | Si       |             | Es algo caro, pero aporta Small Cap Value fuera de USA en mercados desarrollados, lo cuál es un gran aporte.<br><br>                                                                                                                                                                                                           |
| EVLU   | 0.35%       | MSCI Emerging Markets Value Factor Select Index             | No           | Si       |             | Aporta factor Value en mercados emergentes, lo cuál no tenemos  con ningún otro activo.                                                                                                                                                                                                                                        |




| Ticker | Costo Anual | Benchmark                                                   | ¿Disponible? |
| ------ | ----------- | ----------------------------------------------------------- | ------------ |
| ITOT   | 0.03%       | S&P Total Market Total Return Index                         | Si           |
| IUSV   | 0.04%       | S&P 900 Value Total Return Index                            | Si           |
| IXUS   | 0.07%       | MSCI ACWI ex USA IMI Index                                  | Si           |
| IEMG   | 0.09%       | MSCI Emerging Markets Investable Market Index               | Si           |
| ISCV   | 0.06%       | Morningstar US Small Cap Broad Value Extended Index         | No           |
| IJS    | 0.18%       | S&P SmallCap 600(R) Value Index                             | No           |
| IJR    | 0.06%       | S&P 600 Small Cap TR Index                                  | Si           |
| IJH    | 0.05%       | S&P 400 Mid Cap Gross TR Index                              | Si           |
| SCZ    | 0.40%       | MSCI EAFE Small Cap Index                                   | Si           |
| IVE    | 0.18%       | S&P 500 Value TR Index                                      | Si           |
| VLUE   | 0.15%       | MSCI USA Enhanced Value Index                               | Si           |
| IWM    | 0.19%       | Russell 2000 Index                                          | Si           |
| IWN    | 0.24%       | Russell 2000 Value Index                                    | Si           |
| EWZS   | 0.59%       | MSCI Brazil Small Cap Index                                 | Si           |
| ECNS   | 0.59%       | MSCI China Small Cap Index                                  | Si           |
| SCJ    | 0.50%       | MSCI Japan Small Cap Index                                  | Si           |
| IWD    | 0.18%       | Russell 1000 Value Index                                    | Si           |
| IWS    | 0.23%       | Russell MidCap Value Index                                  | Si           |
| ACWI   | 0.32%       | MSCI ACWI Index                                             | Si           |
| IJJ    | 0.18%       | S&P MidCap 400(R) Value Index                               | No           |
| IMCV   | 0.06%       | Morningstar US Mid Cap Broad Value Index                    | No           |
| ILCV   | 0.04%       | Morningstar US Large-Mid Cap Broad Value Index              | No           |
| IVV    | 0.03%       | S&P 500 Index                                               | Si           |
| EFA    | 0.32%       | MSCI EAFE Index                                             | Si           |
| IEFA   | 0.07%       | MSCI EAFE IMI Index                                         | No           |
| IDEV   | 0.04%       | MSCI WORLD ex USA IMI                                       | No           |
| ACWX   | 0.32%       | MSCI ACWI ex-US Index                                       | Si           |
| EUSA   | 0.09%       | MSCI USA Equal Weighted Index                               | No           |
| IWC    | 0.60%       | Russell Microcap Index                                      | Si           |
| WSML   | 0.30%       | MSCI World Small Cap Index                                  | No           |
| EFV    | 0.31%       | MSCI EAFE Value Index                                       | No           |
| IVLU   | 0.31%       | MSCI World ex USA Enhanced Value Index                      | No           |
| EWJV   | 0.15%       | MSCI Japan Value Index                                      | No           |
| ISVL   | 0.31%       | FTSE Developed ex US ex Korea Small Cap Focused Value Index | No           |
| EVLU   | 0.35%       | MSCI Emerging Markets Value Factor Select Index             | No           |







| Ticker | Nombre                                            | Región                 | Market        | Gross Expense  <br>Ratio (%) | Sub Asset Class               |
| ------ | ------------------------------------------------- | ---------------------- | ------------- | ---------------------------- | ----------------------------- |
| MCHI   | iShares MSCI China ETF                            | Asia Pacífico          | Emergentes    | 0.59                         | Alta / Mediana Capitalización |
| ECH    | iShares MSCI Chile ETF                            | América Latina         | Emergentes    | 0.59                         | All Cap                       |
| EFA    | iShares MSCI EAFE ETF                             | Global                 | Desarrollados | 0.32                         | Alta / Mediana Capitalización |
| EFG    | iShares MSCI EAFE Growth ETF                      | Global                 | Desarrollados | 0.34                         | Alta / Mediana Capitalización |
| ECNS   | iShares MSCI China Small-Cap ETF                  | Asia Pacífico          | Emergentes    | 0.59                         | Baja Capitalización           |
| SCZ    | iShares MSCI EAFE Small-Cap ETF                   | Global                 | Desarrollados | 0.4                          | Baja Capitalización           |
| EFAV   | iShares MSCI EAFE Min Vol Factor ETF              | Global                 | Desarrollados | 0.2                          | Alta / Mediana Capitalización |
| IVVB   | iShares Large Cap Deep Quarterly Laddered ETF     | Norteamérica           | Desarrollados | 0.54                         | Alta capitalización           |
| EEM    | iShares MSCI Emerging Markets ETF                 | Global                 | Emergentes    | 0.72                         | Alta / Mediana Capitalización |
| IVVMCL | iShares Large Cap Moderate Quarterly Laddered ETF | Norteamérica           | Desarrollados | 0.53                         | Alta capitalización           |
| EEMV   | iShares MSCI Emerging Markets Min Vol Factor ETF  | Global                 | Emergentes    | 0.25                         | Alta / Mediana Capitalización |
| EUFN   | iShares MSCI Europe Financials ETF                | Europa                 | Desarrollados | 0.49                         | All Cap                       |
| EZU    | iShares MSCI Eurozone ETF                         | Europa                 | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| EWG    | iShares MSCI Germany ETF                          | Europa                 | Desarrollados | 0.49                         | Alta / Mediana Capitalización |
| EWQ    | iShares MSCI France ETF                           | Europa                 | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| HEFA   | iShares Currency Hedged MSCI EAFE ETF             | Global                 | Desarrollados | 0.7                          | Alta / Mediana Capitalización |
| INDA   | iShares MSCI India ETF                            | Asia Pacífico          | Emergentes    | 0.61                         | Alta / Mediana Capitalización |
| EWH    | iShares MSCI Hong Kong ETF                        | Asia Pacífico          | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| HEWJ   | iShares Currency Hedged MSCI Japan ETF            | Asia Pacífico          | Desarrollados | 1.02                         | Alta / Mediana Capitalización |
| EIS    | iShares MSCI Israel ETF                           | Europa                 | Desarrollados | 0.59                         | All Cap                       |
| EIRL   | iShares MSCI Ireland ETF                          | Europa                 | Desarrollados | 0.5                          | All Cap                       |
| EIDO   | iShares MSCI Indonesia ETF                        | Asia Pacífico          | Emergentes    | 0.59                         | All Cap                       |
| SCJ    | iShares MSCI Japan Small-Cap ETF                  | Asia Pacífico          | Desarrollados | 0.5                          | Baja Capitalización           |
| EWJ    | iShares MSCI Japan ETF                            | Asia Pacífico          | Desarrollados | 0.49                         | Alta / Mediana Capitalización |
| EWI    | iShares MSCI Italy ETF                            | Europa                 | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| EWN    | iShares MSCI Netherlands ETF                      | Europa                 | Desarrollados | 0.5                          | All Cap                       |
| EWW    | iShares MSCI Mexico ETF                           | América Latina         | Emergentes    | 0.5                          | All Cap                       |
| EWM    | iShares MSCI Malaysia ETF                         | Asia Pacífico          | Emergentes    | 0.5                          | Alta / Mediana Capitalización |
| EPHE   | iShares MSCI Philippines ETF                      | Asia Pacífico          | Emergentes    | 0.59                         | All Cap                       |
| EPP    | iShares MSCI Pacific ex Japan ETF                 | Asia Pacífico          | Desarrollados | 0.47                         | Alta / Mediana Capitalización |
| ENZL   | iShares MSCI New Zealand ETF                      | Asia Pacífico          | Desarrollados | 0.5                          | All Cap                       |
| EWS    | iShares MSCI Singapore ETF                        | Asia Pacífico          | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| EPOL   | iShares MSCI Poland ETF                           | Europa                 | Emergentes    | 0.59                         | All Cap                       |
| EWP    | iShares MSCI Spain ETF                            | Europa                 | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| EWY    | iShares MSCI South Korea ETF                      | Asia Pacífico          | Emergentes    | 0.59                         | Alta / Mediana Capitalización |
| EZA    | iShares MSCI South Africa ETF                     | Medio Oriente y África | Emergentes    | 0.59                         | Alta / Mediana Capitalización |
| EWT    | iShares MSCI Taiwan ETF                           | Asia Pacífico          | Emergentes    | 0.59                         | Alta / Mediana Capitalización |
| EWL    | iShares MSCI Switzerland ETF                      | Europa                 | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| EWU    | iShares MSCI United Kingdom ETF                   | Europa                 | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| SIZE   | iShares MSCI USA Size Factor ETF                  | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| TUR    | iShares MSCI Turkey ETF                           | Europa                 | Emergentes    | 0.59                         | All Cap                       |
| THD    | iShares MSCI Thailand ETF                         | Asia Pacífico          | Emergentes    | 0.59                         | All Cap                       |
| USMV   | iShares MSCI USA Min Vol Factor ETF               | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| SUSA   | iShares ESG Optimized MSCI USA ETF                | Norteamérica           | Desarrollados | 0.25                         | Alta / Mediana Capitalización |
| IBB    | iShares Biotechnology ETF                         | Norteamérica           | Desarrollados | 0.44                         | All Cap                       |
| DYNF   | iShares U.S. Equity Factor Rotation Active ETF    | Norteamérica           | Desarrollados | 0.26                         | Alta / Mediana Capitalización |
| IWB    | iShares Russell 1000 ETF                          | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| IWF    | iShares Russell 1000 Growth ETF                   | Norteamérica           | Desarrollados | 0.18                         | Alta / Mediana Capitalización |
| IWM    | iShares Russell 2000 ETF                          | Norteamérica           | Desarrollados | 0.19                         | Baja Capitalización           |
| IWO    | iShares Russell 2000 Growth ETF                   | Norteamérica           | Desarrollados | 0.24                         | Baja Capitalización           |
| IWD    | iShares Russell 1000 Value ETF                    | Norteamérica           | Desarrollados | 0.18                         | Alta / Mediana Capitalización |
| IUSV   | iShares Core S&P U.S. Value ETF                   | Norteamérica           | Desarrollados | 0.04                         | All Cap                       |
| IWV    | iShares Russell 3000 ETF                          | Norteamérica           | Desarrollados | 0.2                          | All Cap                       |
| IUSG   | iShares Core S&P U.S. Growth ETF                  | Norteamérica           | Desarrollados | 0.04                         | All Cap                       |
| IWN    | iShares Russell 2000 Value ETF                    | Norteamérica           | Desarrollados | 0.24                         | Baja Capitalización           |
| IWS    | iShares Russell Mid-Cap Value ETF                 | Norteamérica           | Desarrollados | 0.23                         | Mediana Capitalización        |
| IWR    | iShares Russell Mid-Cap ETF                       | Norteamérica           | Desarrollados | 0.18                         | Mediana Capitalización        |
| QUAL   | iShares MSCI USA Quality Factor ETF               | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| IWP    | iShares Russell Mid-Cap Growth ETF                | Norteamérica           | Desarrollados | 0.23                         | Mediana Capitalización        |
| IWC    | iShares Micro-Cap ETF                             | Norteamérica           | Desarrollados | 0.6                          | Baja Capitalización           |
| OEF    | iShares S&P 100 ETF                               | Norteamérica           | Desarrollados | 0.2                          | Alta capitalización           |
| IVV    | iShares Core S&P 500 ETF                          | Norteamérica           | Desarrollados | 0.03                         | Alta capitalización           |
| IVW    | iShares S&P 500 Growth ETF                        | Norteamérica           | Desarrollados | 0.18                         | Alta capitalización           |
| ITOT   | iShares Core S&P Total U.S. Stock Market ETF      | Norteamérica           | Desarrollados | 0.03                         | All Cap                       |
| IVE    | iShares S&P 500 Value ETF                         | Norteamérica           | Desarrollados | 0.18                         | Alta capitalización           |
| EMIF   | iShares Emerging Markets Infrastructure ETF       | Global                 | Emergentes    | 0.6                          | All Cap                       |
| RXI    | iShares Global Consumer Discretionary ETF         | Global                 | Desarrollados | 0.39                         | All Cap                       |
| ICLN   | iShares Global Clean Energy ETF                   | Global                 | Desarrollados | 0.39                         | All Cap                       |
| IEV    | iShares Europe ETF                                | Europa                 | Desarrollados | 0.6                          | Alta / Mediana Capitalización |
| IXG    | iShares Global Financials ETF                     | Global                 | Desarrollados | 0.41                         | All Cap                       |
| IXC    | iShares Global Energy ETF                         | Global                 | Desarrollados | 0.4                          | All Cap                       |
| KXI    | iShares Global Consumer Staples ETF               | Global                 | Desarrollados | 0.39                         | All Cap                       |
| IDRV   | iShares Self-Driving EV and Tech ETF              | Global                 | Desarrollados | 0.48                         | All Cap                       |
| IGF    | iShares Global Infrastructure ETF                 | Global                 | Desarrollados | 0.39                         | All Cap                       |
| ESGE   | iShares ESG Aware MSCI EM ETF                     | Global                 | Emergentes    | 0.25                         | Alta / Mediana Capitalización |
| ESGD   | iShares ESG Aware MSCI EAFE ETF                   | Global                 | Desarrollados | 0.2                          | Alta / Mediana Capitalización |
| MXI    | iShares Global Materials ETF                      | Global                 | Desarrollados | 0.39                         | All Cap                       |
| IDNA   | iShares Genomics Immunology and Healthcare ETF    | Global                 | Desarrollados | 0.47                         | All Cap                       |
| INDY   | iShares India 50 ETF                              | Asia Pacífico          | Emergentes    | 0.65                         | Alta capitalización           |
| XT     | iShares Future Exponential Technologies ETF       | Global                 | Desarrollados | 0.46                         | Alta capitalización           |
| IJH    | iShares Core S&P Mid-Cap ETF                      | Norteamérica           | Desarrollados | 0.05                         | Mediana Capitalización        |
| ILF    | iShares Latin America 40 ETF                      | América Latina         | Emergentes    | 0.47                         | Alta capitalización           |
| IGE    | iShares North American Natural Resources ETF      | Norteamérica           | Desarrollados | 0.39                         | All Cap                       |
| IHAK   | iShares Cybersecurity and Tech ETF                | Global                 | Desarrollados | 0.47                         | Alta / Mediana Capitalización |
| IJR    | iShares Core S&P Small-Cap ETF                    | Norteamérica           | Desarrollados | 0.06                         | Baja Capitalización           |
| ESML   | iShares ESG Aware MSCI USA Small-Cap ETF          | Norteamérica           | Desarrollados | 0.17                         | Baja Capitalización           |
| CRBN   | iShares Low Carbon Optimized MSCI ACWI ETF        | Global                 | Desarrollados | 0.2                          | Alta / Mediana Capitalización |
| MTUM   | iShares MSCI USA Momentum Factor ETF              | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| VLUE   | iShares MSCI USA Value Factor ETF                 | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| TECB   | iShares U.S. Tech Breakthrough Multisector ETF    | Norteamérica           | Desarrollados | 0.3                          | All Cap                       |
| ESGU   | iShares ESG Aware MSCI USA ETF                    | Norteamérica           | Desarrollados | 0.15                         | Alta / Mediana Capitalización |
| IEMG   | iShares Core MSCI Emerging Markets ETF            | Global                 | Emergentes    | 0.09                         | All Cap                       |
| IXUS   | iShares Core MSCI Total International Stock ETF   | Global                 | Desarrollados | 0.07                         | All Cap                       |
| SUSL   | iShares ESG MSCI USA Leaders ETF                  | Norteamérica           | Desarrollados | 0.1                          | Alta / Mediana Capitalización |
| IYM    | iShares U.S. Basic Materials ETF                  | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| DVY    | iShares Select Dividend ETF                       | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYE    | iShares U.S. Energy ETF                           | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYC    | iShares U.S. Consumer Discretionary ETF           | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| BALICL | iShares U.S. Large Cap Premium Income Active ETF  | Norteamérica           | Desarrollados | 0.35                         | Alta capitalización           |
| IYK    | iShares U.S. Consumer Staples ETF                 | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYH    | iShares U.S. Healthcare ETF                       | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYG    | iShares U.S. Financial Services ETF               | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYF    | iShares U.S. Financials ETF                       | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYJ    | iShares U.S. Industrials ETF                      | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| LDEM   | iShares ESG MSCI EM Leaders ETF                   | Global                 | Emergentes    | 0.16                         | Alta / Mediana Capitalización |
| ITB    | iShares U.S. Home Construction ETF                | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IEZ    | iShares U.S. Oil Equipment & Services ETF         | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| HEZU   | iShares Currency Hedged MSCI Eurozone ETF         | Europa                 | Desarrollados | 1.12                         | Alta / Mediana Capitalización |
| IYZ    | iShares U.S. Telecommunications ETF               | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| IYW    | iShares U.S. Technology ETF                       | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| HEEM   | iShares Currency Hedged MSCI Emerging Markets ETF | Global                 | Emergentes    | 1.51                         | Alta / Mediana Capitalización |
| IDU    | iShares U.S. Utilities ETF                        | Norteamérica           | Desarrollados | 0.38                         | All Cap                       |
| DGRO   | iShares Core Dividend Growth ETF                  | Norteamérica           | Desarrollados | 0.08                         | All Cap                       |
| IFRA   | iShares U.S. Infrastructure ETF                   | Norteamérica           | Desarrollados | 0.3                          | All Cap                       |
| FXI    | iShares China Large-Cap ETF                       | Asia Pacífico          | Emergentes    | 0.73                         | Alta capitalización           |
| ARTY   | iShares Future AI & Tech ETF                      | Global                 | Desarrollados | 0.47                         | All Cap                       |
| LRGF   | iShares U.S. Equity Factor ETF                    | Norteamérica           | Desarrollados | 0.08                         | Alta / Mediana Capitalización |
| HDV    | iShares Core High Dividend ETF                    | Norteamérica           | Desarrollados | 0.08                         | All Cap                       |
| ACWX   | iShares MSCI ACWI ex U.S. ETF                     | Global                 | Desarrollados | 0.32                         | Alta / Mediana Capitalización |
| AAXJ   | iShares MSCI All Country Asia ex Japan ETF        | Asia Pacífico          | Emergentes    | 0.72                         | Alta / Mediana Capitalización |
| ACWI   | iShares MSCI ACWI ETF                             | Global                 | Desarrollados | 0.32                         | Alta / Mediana Capitalización |
| EWA    | iShares MSCI Australia ETF                        | Asia Pacífico          | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| EPU    | iShares MSCI Peru and Global Exposure ETF         | América Latina         | Emergentes    | 0.59                         | All Cap                       |
| ACWV   | iShares MSCI Global Min Vol Factor ETF            | Global                 | Desarrollados | 0.2                          | Alta / Mediana Capitalización |
| USXF   | iShares ESG Advanced MSCI USA ETF                 | Norteamérica           | Desarrollados | 0.1                          | Alta capitalización           |
| EWC    | iShares MSCI Canada ETF                           | Norteamérica           | Desarrollados | 0.5                          | Alta / Mediana Capitalización |
| BKF    | iShares MSCI BIC ETF                              | Global                 | Emergentes    | 0.72                         | Alta / Mediana Capitalización |
| DMXF   | iShares ESG Advanced MSCI EAFE ETF                | Global                 | Desarrollados | 0.12                         | Alta capitalización           |
| EWZS   | iShares MSCI Brazil Small-Cap ETF                 | América Latina         | Emergentes    | 0.59                         | Baja Capitalización           |
| EWZ    | iShares MSCI Brazil ETF                           | América Latina         | Emergentes    | 0.59                         | Alta / Mediana Capitalización |



Estos fueron los resultados:

  
  

[*********************100%***********************] 8 of 8 completed

  

Caso_1.1_Felix_Lite {'ITOT': 0.2114, 'IUSV': 0.2114, 'IJR': 0.2114, 'IXUS': 0.3658}

  

Caso_1vIWN_Felix_Lite {'ITOT': 0.2114, 'IUSV': 0.2114, 'IWN': 0.2114, 'IXUS': 0.3658}

  

Caso_2_Internacional_Plus {'ITOT': 0.2114, 'IUSV': 0.2114, 'IJR': 0.2114, 'IXUS': 0.2923, 'SCZ': 0.0511, 'IEMG': 0.0219}

  

Caso_2vIWN_Internacional_Plus {'ITOT': 0.2114, 'IUSV': 0.2114, 'IWN': 0.2114, 'IXUS': 0.2923, 'SCZ': 0.0511, 'IEMG': 0.0219}

  

Caso_3.1_Brígido_Factor_Aggro {'ITOT': 0.15855, 'IJR': 0.15855, 'QUAL': 0.15855, 'IUSV': 0.15855, 'IXUS': 0.255, 'SCZ': 0.11}

  

Caso_3vIWN_Brígido_Factor_Aggro {'ITOT': 0.15855, 'IWN': 0.15855, 'QUAL': 0.15855, 'IUSV': 0.15855, 'IXUS': 0.255, 'SCZ': 0.11}

  

Market_Cap_Puro (Benchmark) {'ITOT': 0.634, 'IXUS': 0.366}

  

Caso_1vEqualUsInt_Felix_Lite {'ITOT': 0.167, 'IUSV': 0.167, 'IJR': 0.167, 'IXUS': 0.5}

  

Caso_2vEqualUsInt_Internacional_Plus {'ITOT': 0.167, 'IUSV': 0.167, 'IJR': 0.167, 'IXUS': 0.399, 'SCZ': 0.069, 'IEMG': 0.0299}

  

Caso_3vEqualUsInt_Brígido_Factor_Aggro {'ITOT': 0.125, 'IJR': 0.125, 'QUAL': 0.125, 'IUSV': 0.125, 'IXUS': 0.349, 'SCZ': 0.151}

  

Market_Cap_PurovEqual (Benchmark) {'ITOT': 0.5, 'IXUS': 0.5}

  

--- Retorno Total Acumulado (%) ---

  

Caso_1.1_Felix_Lite 229.788053

  

Caso_1vIWN_Felix_Lite 219.309772

  

Caso_2_Internacional_Plus 230.428106

  

Caso_2vIWN_Internacional_Plus 219.929003

  

Caso_3.1_Brígido_Factor_Aggro 244.889476

  

Caso_3vIWN_Brígido_Factor_Aggro 236.717611

  

Market_Cap_Puro (Benchmark) 279.308366

  

Caso_1vEqualUsInt_Felix_Lite 209.821737

  

Caso_2vEqualUsInt_Internacional_Plus 210.304580

  

Caso_3vEqualUsInt_Brígido_Factor_Aggro 222.116409

  

Market_Cap_PurovEqual (Benchmark) 245.447081

  

Name: 2026-01-23 00:00:00, dtype: float64

  
  
  

De aquí podemos concluir que IWN es derechamente inferior a IJR, aunque IJR sea sólo small cap blend. El filtro de S&P hace de las suyas.

  
  

También que los benchmarks superan con creces a los factores con tilt, más que nada porque en estos años, ITOT se ha disparado un montón, las big tech, mag 7 y todas esas hacen que itot suba muchísimo en los benchmarks, pero eso da igual, no significa que me ponga todo a ITOT, o peor aún, full MAG 7 xd.




Además, ignorar cualquier fondo que sea:
- Sectorial
- Growth (especialmente small cap growth)
- Dividend
- Renta fija
- Criptomonedas
- Real Estate
- Commodities (Oro, plata, petróleo, Gas, Vacas) 
- Apalancado
- Covered Call
- Venta corta
- Derivados de cosas que ni entiendes
- Cualquier mezcla de lo anterior
- Cualquier otra cosa rara que no sean Equities puros y duros.


En resumen:
- Invertir en acciones globales con tilts hacia value, small caps y mercados emergentes.
- Distribuir las proporciones de USA vs Internacional según el tamaño de sus mercados (Al 2026 es 64% USA vs 36% Internacional aproximadamente, lo cual obviamente va a ir variando con el tiempo, no es una proporción fija)
- Priorizar comisiones bajas, incluso si eso significa no tener un tilt.
- Para los tilts, priorizar siempre comprar fondos que tengan "filtros" de calidad de algún tipo, porque comprar tilts de small caps blends puede llegar a ser incluso peor al incluir small caps growth que tienen pésimo rendimiento.
- Nunca vender al rebalancear, sólo comprar lo que subió menos. Así compras barato, y dejas que lo caro siga subiendo sin venderlo antes de tiempo.
- Los tilts deben ser fuertes para que hagan una diferencia real. Tener 5% de un fondo con tilt no va a valer la pena.
- Mientras más tracking error tengas por underperformance en la fase de acumulación, mejor todavía, aprovechas de comprar más.


Proporciones propuestas según caso:
- Caso 1, según ETFs disponibles actualmente (2026)
	- Sector USA:
		- ITOT: 21.14%
		- IUSV: 21.14%
		- IJR: 21.14%
	- Sector Internacional:
		- IXUS: 36.57%
	- Costo ponderado: 0.0531%

- Caso 2: Incluyendo SCZ y IEMG para compensar Emergentes:
	- Sector USA:
		- ITOT: 21.14%
		- IUSV: 21.14%
		- IJR: 21.14%
	- Sector Internacional:
		- IXUS: 29.23%
		- SCZ: 5.11%
		- IEMG 2.19%
	- Costo ponderado: 0.0704%

- Caso 2, si tenemos acceso a ISVL, y/o IVLU, o equivalentes, entonces repartirlos equitativamente en el sector develop markets, y agregar EVLU o IEMG para compensar la dilusión del sector Emerging Markets.
	- Sector USA:
		- ITOT: 21.14%
		- IUSV: 21.14%
		- IJR: 21.14%
	- Sector Internacional:.
		- Developed Markets EX USA (25.57% aprox del ACWI IMI)
			- ISVL: 12.19%
			- IVLU: 12.19%
		- Emerging Markets (11% aprox del ACWI IMI):
			- EVLU / IEMG: 
		- DM + EM:
			- IXUS: 

- Caso 3, si tenemos disponible ISCV o IJS:
	- Simplemente reemplazar IJR por ISCV o IJS, el resto se mantiene igual.




| Date            | EFA     | IEFA    | SCZ     | Ixus    | EFA-EIFA | EFA-SCZ | EFA-IXUS | IEFA-IXUS | IEFA-SCZ | IXUS-SCZ |
| --------------- | ------- | ------- | ------- | ------- | -------- | ------- | -------- | --------- | -------- | -------- |
| 2002-12-31      | -15.42% |         |         |         |          |         |          |           |          |          |
| 2003-12-31      | 40.30%  |         |         |         |          |         |          |           |          |          |
| 2004-12-31      | 18.96%  |         |         |         |          |         |          |           |          |          |
| 2005-12-31      | 13.32%  |         |         |         |          |         |          |           |          |          |
| 2006-12-31      | 25.81%  |         |         |         |          |         |          |           |          |          |
| 2007-12-31      | 9.95%   |         |         |         |          |         |          |           |          |          |
| 2008-12-31      | -41.03% |         | -48.54% |         |          | 7.51%   |          |           |          |          |
| 2009-12-31      | 26.99%  |         | 42.88%  |         |          | -15.89% |          |           |          |          |
| 2010-12-31      | 8.17%   |         | 21.52%  |         |          | -13.35% |          |           |          |          |
| 2011-12-31      | -12.23% |         | -15.10% |         |          | 2.87%   |          |           |          |          |
| 2012-12-31      | 18.76%  |         | 21.26%  |         |          | -2.50%  |          |           |          |          |
| 2013-12-31      | 21.44%  | 22.46%  | 28.65%  | 13.69%  | -1.01%   | -7.20%  | 7.75%    | 8.76%     | -6.19%   | -14.95%  |
| 2014-12-31      | -6.19%  | -6.32%  | -6.06%  | -4.99%  | 0.13%    | -0.14%  | -1.20%   | -1.33%    | -0.27%   | 1.06%    |
| 2015-12-31      | -0.99%  | 0.74%   | 9.11%   | -4.67%  | -1.73%   | -10.10% | 3.67%    | 5.40%     | -8.37%   | -13.78%  |
| 2016-12-31      | 1.37%   | 1.58%   | 2.62%   | 4.72%   | -0.21%   | -1.25%  | -3.34%   | -3.14%    | -1.04%   | 2.09%    |
| 2017-12-31      | 25.08%  | 26.57%  | 32.72%  | 28.12%  | -1.49%   | -7.64%  | -3.04%   | -1.55%    | -6.15%   | -4.60%   |
| 2018-12-31      | -13.82% | -14.14% | -17.64% | -14.41% | 0.32%    | 3.82%   | 0.59%    | 0.27%     | 3.49%    | 3.23%    |
| 2019-12-31      | 22.04%  | 22.64%  | 24.68%  | 21.71%  | -0.60%   | -2.64%  | 0.34%    | 0.94%     | -2.04%   | -2.97%   |
| 2020-12-31      | 7.60%   | 8.18%   | 11.71%  | 10.80%  | -0.58%   | -4.11%  | -3.21%   | -2.62%    | -3.53%   | -0.91%   |
| 2021-12-31      | 11.45%  | 11.63%  | 10.12%  | 8.86%   | -0.19%   | 1.33%   | 2.59%    | 2.78%     | 1.52%    | -1.26%   |
| 2022-12-31      | -14.39% | -15.24% | -21.27% | -16.47% | 0.86%    | 6.89%   | 2.08%    | 1.22%     | 6.03%    | 4.81%    |
| 2023-12-31      | 18.36%  | 17.95%  | 12.98%  | 15.83%  | 0.41%    | 5.39%   | 2.53%    | 2.12%     | 4.97%    | 2.85%    |
| 2024-12-31      | 3.49%   | 3.26%   | 1.52%   | 5.19%   | 0.22%    | 1.97%   | -1.70%   | -1.93%    | 1.75%    | 3.68%    |
| 2025-12-31      | 31.55%  | 32.08%  | 32.08%  | 32.40%  | -0.53%   | -0.53%  | -0.85%   | -0.32%    | 0.00%    | 0.32%    |
| 2026-12-31      | 4.10%   | 4.33%   | 5.82%   | 5.43%   | -0.22%   | -1.71%  | -1.33%   | -1.11%    | -1.49%   | -0.38%   |
| Prom desde 2002 | 8.19%   |         |         |         |          |         |          |           |          |          |
| Prom desde 2013 | 7.93%   | 8.26%   | 9.07%   | 7.59%   | -0.33%   |         | 0.35%    | 0.68%     | -0.81%   | -1.49%   |
| Prom desde 2008 | 5.88%   |         | 7.84%   |         |          | -1.96%  |          |           |          |          |



| Estrategia | A          | B       | C       | D       |
| ---------- | ---------- | ------- | ------- | ------- |
| Ticker     | Proporción |         |         |         |
| ITOT       | 16.67%     | 16.67%  | 16.67%  | 16.67%  |
| IUSV       | 16.67%     | 16.67%  | 16.67%  | 16.67%  |
| IJR        | 16.66%     | 16.66%  | 16.66%  | 16.66%  |
| IXUS       | 50.00%     | 25%     | 40%     | 33.40%  |
| SCZ        | 0%         | 25%     | 10%     | 16.60%  |
| Total      | 100.00%    | 100.00% | 100.00% | 100.00% |



| Variaciones ponderadas / Fecha | Estrategia A | Estrategia B | Estrategia C | Estrategia D |
| ------------------------------ | ------------ | ------------ | ------------ | ------------ |
| 2013-12-31                     | 24.65%       | 28.39%       | 26.15%       | 27.13%       |
| 2014-12-31                     | 2.86%        | 2.59%        | 2.75%        | 2.68%        |
| 2015-12-31                     | -3.25%       | 0.19%        | -1.87%       | -0.97%       |
| 2016-12-31                     | 11.97%       | 11.45%       | 11.76%       | 11.62%       |
| 2017-12-31                     | 22.33%       | 23.47%       | 22.79%       | 23.09%       |
| 2018-12-31                     | -11.05%      | -11.85%      | -11.37%      | -11.58%      |
| 2019-12-31                     | 25.01%       | 25.76%       | 25.31%       | 25.51%       |
| 2020-12-31                     | 10.99%       | 11.22%       | 11.08%       | 11.14%       |
| 2021-12-31                     | 17.34%       | 17.66%       | 17.47%       | 17.55%       |
| 2022-12-31                     | -15.08%      | -16.28%      | -15.56%      | -15.88%      |
| 2023-12-31                     | 18.57%       | 17.85%       | 18.28%       | 18.09%       |
| 2024-12-31                     | 10.03%       | 9.11%        | 9.66%        | 9.42%        |
| 2025-12-31                     | 22.16%       | 22.08%       | 22.12%       | 22.10%       |
| 2026-12-31                     | 4.44%        | 4.54%        | 4.48%        | 4.50%        |
| Promedio                       | 10.07%       | 10.44%       | 10.22%       | 10.32%       |





Tabla resumen de proporciones 

|                 |             | Tilt Fuerte | Con SCZ normal | SCZ Barato | Con IJS | Con SCZ normal | SCZ Barato | Con ISCV | Con SCZ normal | SCZ Barato |
| --------------- | ----------- | ----------- | -------------- | ---------- | ------- | -------------- | ---------- | -------- | -------------- | ---------- |
| Ticker          | Costo Anual | A           | B              | C          | D       | E              | F          | G        | H              | I          |
| ITOT            | 0.03%       | 0%          | 0%             | 0%         | 0%      | 0%             | 0%         | 0%       | 0%             | 0%         |
| IUSV            | 0.04%       | 32%         | 32%            | 32%        | 32%     | 32%            | 32%        | 32%      | 32%            | 32%        |
| IJR             | 0.06%       | 32%         | 32%            | 32%        | 0%      | 0%             | 0%         | 0%       | 0%             | 0%         |
| IJS             | 0.18%       | 0%          | 0%             | 0%         | 32%     | 32%            | 32%        | 0%       | 0%             | 0%         |
| ISCV            | 0.06%       | 0%          | 0%             | 0%         | 0%      | 0%             | 0%         | 32%      | 32%            | 32%        |
| IXUS            | 0.07%       | 18%         | 12.24%         | 12.24%     | 18%     | 12.24%         | 12.24%     | 18%      | 12.24%         | 12.24%     |
| IEMG            | 0.09%       | 18%         | 11.88%         | 11.88%     | 18%     | 11.88%         | 11.88%     | 18%      | 11.88%         | 11.88%     |
| SCZ             | 0.40%       | 0%          | 11.88%         | 0%         | 0%      | 11.88%         | 0%         | 0%       | 11.88%         | 0%         |
| SCZ Barato      | 0.15%       | 0%          | 0%             | 11.88%     | 0%      | 0%             | 11.88%     | 0%       | 0%             | 11.88%     |
| Costo Ponderado |             | 0.0608%     | 0.0988%        | 0.0691%    | 0.0992% | 0.1372%        | 0.1075%    | 0.0608%  | 0.0988%        | 0.0691%    |


|                 |             | Tilt Suave | Con SCZ normal | SCZ Barato | Con IJS | Con SCZ normal | SCZ Barato | Con ISCV | Con SCZ normal | SCZ Barato |
| --------------- | ----------- | ---------- | -------------- | ---------- | ------- | -------------- | ---------- | -------- | -------------- | ---------- |
|                 | Costo Anual | A          | B              | C          | D       | E              | F          | G        | H              | I          |
| ITOT            | 0.03%       | 21.76%     | 21.76%         | 21.76%     | 21.76%  | 21.76%         | 21.76%     | 21.76%   | 21.76%         | 21.76%     |
| IUSV            | 0.04%       | 21.12%     | 21.12%         | 21.12%     | 21.12%  | 21.12%         | 21.12%     | 21.12%   | 21.12%         | 21.12%     |
| IJR             | 0.06%       | 21.12%     | 21.12%         | 21.12%     | 0.00%   | 0.00%          | 0.00%      | 0.00%    | 0.00%          | 0.00%      |
| IJS             | 0.18%       | 0.00%      | 0.00%          | 0.00%      | 21.12%  | 21.12%         | 21.12%     | 0.00%    | 0.00%          | 0.00%      |
| ISCV            | 0.06%       | 0.00%      | 0.00%          | 0.00%      | 0.00%   | 0.00%          | 0.00%      | 21.12%   | 21.12%         | 21.12%     |
| IXUS            | 0.07%       | 22.44%     | 18.00%         | 18.00%     | 22.44%  | 18.00%         | 18.00%     | 22.44%   | 18.00%         | 18.00%     |
| IEMG            | 0.09%       | 15.56%     | 9.00%          | 9.00%      | 15.56%  | 9.00%          | 9.00%      | 15.56%   | 9.00%          | 9.00%      |
| SCZ             | 0.40%       | 0.00%      | 9.00%          | 0.00%      | 0.00%   | 9.00%          | 0.00%      | 0.00%    | 9.00%          | 0.00%      |
| SCZ Barato      | 0.15%       | 0.00%      | 0.00%          | 9.00%      | 0.00%   | 0.00%          | 9.00%      | 0.00%    | 0.00%          | 9.00%      |
| Costo Ponderado |             | 0.0562%    | 0.0843%        | 0.0618%    | 0.0811% | 0.1097%        | 0.0872%    | 0.0562%  | 0.0843%        | 0.0618%    |



Rentabilidades anuales de cada ticker:

| Date       | IEMG    | IJH     | IJR     | ITOT    | IUSV    | IXUS    | SCZ     |
| ---------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 2001-12-31 |         | -1.25%  | 6.43%   |         | -4.82%  |         |         |
| 2002-12-31 |         | -14.21% | -14.30% |         | -16.07% |         |         |
| 2003-12-31 |         | 35.20%  | 38.49%  |         | 31.72%  |         |         |
| 2004-12-31 |         | 16.08%  | 22.41%  |         | 16.71%  |         |         |
| 2005-12-31 |         | 12.88%  | 7.53%   | 5.33%   | 6.60%   |         |         |
| 2006-12-31 |         | 9.67%   | 15.09%  | 15.12%  | 21.90%  |         |         |
| 2007-12-31 |         | 7.30%   | -0.48%  | 5.15%   | -1.39%  |         |         |
| 2008-12-31 |         | -36.17% | -31.52% | -36.47% | -36.03% |         | -48.54% |
| 2009-12-31 |         | 37.81%  | 25.89%  | 26.60%  | 19.55%  |         | 42.88%  |
| 2010-12-31 |         | 26.72%  | 26.61%  | 16.22%  | 15.80%  |         | 21.52%  |
| 2011-12-31 |         | -2.17%  | 0.81%   | 1.75%   | -0.28%  |         | -15.10% |
| 2012-12-31 |         | 17.79%  | 16.30%  | 15.83%  | 17.37%  |         | 21.26%  |
| 2013-12-31 | -2.78%  | 33.47%  | 41.33%  | 33.32%  | 32.18%  | 13.69%  | 28.65%  |
| 2014-12-31 | -3.41%  | 9.71%   | 5.85%   | 13.53%  | 12.75%  | -4.99%  | -6.06%  |
| 2015-12-31 | -14.30% | -2.34%  | -2.08%  | 0.90%   | -4.33%  | -4.67%  | 9.11%   |
| 2016-12-31 | 10.28%  | 20.72%  | 26.59%  | 12.60%  | 18.47%  | 4.72%   | 2.62%   |
| 2017-12-31 | 37.38%  | 16.26%  | 13.15%  | 21.37%  | 15.07%  | 28.12%  | 32.72%  |
| 2018-12-31 | -14.92% | -11.19% | -8.51%  | -5.33%  | -9.21%  | -14.41% | -17.64% |
| 2019-12-31 | 17.81%  | 26.10%  | 22.82%  | 30.67%  | 31.47%  | 21.71%  | 24.68%  |
| 2020-12-31 | 17.86%  | 13.60%  | 11.28%  | 20.71%  | 1.56%   | 10.80%  | 11.71%  |
| 2021-12-31 | -0.64%  | 24.72%  | 26.58%  | 25.68%  | 25.22%  | 8.86%   | 10.12%  |
| 2022-12-31 | -19.98% | -13.11% | -16.20% | -19.47% | -5.40%  | -16.47% | -21.27% |
| 2023-12-31 | 11.52%  | 16.41%  | 16.06%  | 26.12%  | 21.73%  | 15.83%  | 12.98%  |
| 2024-12-31 | 6.50%   | 13.92%  | 8.63%   | 23.80%  | 12.18%  | 5.19%   | 1.52%   |
| 2025-12-31 | 32.56%  | 7.42%   | 5.89%   | 17.00%  | 12.85%  | 32.40%  | 32.08%  |
| 2026-12-31 | 7.71%   | 5.52%   | 6.58%   | 1.53%   | 2.23%   | 5.43%   | 5.82%   |


Como sugerencia, se tienen las dos siguientes opciones de inversión, pero estas pueden ser modificadas, o construir una nueva totalmente.

| Ticker | Opción A | Opción B | Gasto Anual | Costo Ponderado Opción A | Costo Ponderado Opción B |
| ------ | -------- | -------- | ----------- | ------------------------ | ------------------------ |
| Itot   | 21.14%   | 21.14%   | 0.03%       | 0.0063%                  | 0.0063%                  |
| IUSV   | 21.14%   | 21.14%   | 0.04%       | 0.0085%                  | 0.0085%                  |
| IJR    | 21.14%   | 21.14%   | 0.06%       | 0.0127%                  | 0.0127%                  |
| IXUS   | 29.26%   | 36.57%   | 0.07%       | 0.0205%                  | 0.0256%                  |
| SCZ    | 7.31%    | 0%       | 0.40%       | 0.0292%                  | 0.0000%                  |
| Total  | 100%     | 100%     |             | 0.0772%                  | 0.0531%                  |








| Ticker Name                                                                           | Net Expense Ratio (%) | 12m Trailing Yield (%) | YTD Return (%) |
| ------------------------------------------------------------------------------------- | --------------------- | ---------------------- | -------------- |
| iShares Core S&P 500 ETF  <br>IVVFactsheet                                            | 0.03                  | 1.17                   | 1.05           |
| iShares Core MSCI EAFE ETF  <br>IEFAFactsheet                                         | 0.07                  | 3.53                   | 3.88           |
| iShares Core MSCI Emerging Markets ETF  <br>IEMGFactsheet                             | 0.09                  | 2.75                   | 6.76           |
| iShares Russell 1000 Growth ETF  <br>IWFFactsheet                                     | 0.18                  | 0.36                   | -1.5           |
| iShares Core S&P Mid-Cap ETF  <br>IJHFactsheet                                        | 0.05                  | 1.36                   | 6.59           |
| iShares Core S&P Small-Cap ETF  <br>IJRFactsheet                                      | 0.06                  | 1.44                   | 8.5            |
| iShares Core S&P Total U.S. Stock Market ETF  <br>ITOTFactsheet                       | 0.03                  | 1.11                   | 1.67           |
| iShares Russell 2000 ETF  <br>IWMFactsheet                                            | 0.19                  | 1.04                   | 9.58           |
| iShares MSCI EAFE ETF  <br>EFAFactsheet                                               | 0.32                  | 3.36                   | 3.66           |
| iShares Russell 1000 Value ETF  <br>IWDFactsheet                                      | 0.18                  | 1.69                   | 4.5            |
| iShares S&P 500 Growth ETF  <br>IVWFactsheet                                          | 0.18                  | 0.4                    | -0.18          |
| iShares Core MSCI Total International Stock ETF  <br>IXUSFactsheet                    | 0.07                  | 3.22                   | 4.75           |
| iShares S&P 500 Value ETF  <br>IVEFactsheet                                           | 0.18                  | 1.61                   | 2.46           |
| iShares Russell Mid-Cap ETF  <br>IWRFactsheet                                         | 0.18                  | 1.29                   | 4.97           |
| iShares Russell 1000 ETF  <br>IWBFactsheet                                            | 0.15                  | 1                      | 1.28           |
| iShares S&P 100 ETF  <br>OEFFactsheet                                                 | 0.2                   | 0.81                   | -0.52          |
| iShares MSCI EAFE Value ETF  <br>EFVFactsheet                                         | 0.31                  | 4.13                   | 2.89           |
| iShares Core S&P U.S. Growth ETF  <br>IUSGFactsheet                                   | 0.04                  | 0.54                   | 0.19           |
| iShares MSCI ACWI ETF  <br>ACWIFactsheet                                              | 0.32                  | 1.55                   | 2.29           |
| iShares Core MSCI International Developed Markets ETF  <br>IDEVFactsheet              | 0.04                  | 3.39                   | 3.87           |
| iShares MSCI Emerging Markets ETF  <br>EEMFactsheet                                   | 0.72                  | 2.22                   | 6.99           |
| iShares Core S&P U.S. Value ETF  <br>IUSVFactsheet                                    | 0.04                  | 1.78                   | 2.67           |
| iShares Russell Mid-Cap Growth ETF  <br>IWPFactsheet                                  | 0.23                  | 0.37                   | 2.68           |
| iShares Russell 3000 ETF  <br>IWVFactsheet                                            | 0.2                   | 0.96                   | 1.64           |
| iShares MSCI Japan ETF  <br>EWJFactsheet                                              | 0.49                  | 4.48                   | 5.37           |
| iShares Russell Top 200 Growth ETF  <br>IWYFactsheet                                  | 0.2                   | 0.36                   | -1.93          |
| iShares MSCI Emerging Markets ex China ETF  <br>EMXCFactsheet                         | 0.25                  | 2.81                   | 8              |
| iShares Russell Mid-Cap Value ETF  <br>IWSFactsheet                                   | 0.23                  | 1.53                   | 5.68           |
| iShares MSCI Intl Quality Factor ETF  <br>IQLTFactsheet                               | 0.3                   | 2.33                   | 3.76           |
| iShares Russell 2000 Growth ETF  <br>IWOFactsheet                                     | 0.24                  | 0.56                   | 9.42           |
| iShares MSCI EAFE Small-Cap ETF  <br>SCZFactsheet                                     | 0.4                   | 3.3                    | 5.2            |
| iShares Russell 2000 Value ETF  <br>IWNFactsheet                                      | 0.24                  | 1.69                   | 9.74           |
| iShares ESG Aware MSCI EAFE ETF  <br>ESGDFactsheet                                    | 0.2                   | 3.6                    | 3.65           |
| iShares MSCI South Korea ETF  <br>EWYFactsheet                                        | 0.59                  | 2.07                   | 17.54          |
| iShares MSCI EAFE Growth ETF  <br>EFGFactsheet                                        | 0.34                  | 2.51                   | 4.45           |
| iShares S&P Mid-Cap 400 Growth ETF  <br>IJKFactsheet                                  | 0.17                  | 0.66                   | 7.1            |
| iShares MSCI Eurozone ETF  <br>EZUFactsheet                                           | 0.5                   | 2.84                   | 3.07           |
| iShares Global Infrastructure ETF  <br>IGFFactsheet                                   | 0.39                  | 3.22                   | 2.24           |
| iShares MSCI India ETF  <br>INDAFactsheet                                             | 0.61                  | 0                      | -4.46          |
| iShares MSCI ACWI ex U.S. ETF  <br>ACWXFactsheet                                      | 0.32                  | 2.83                   | 4.56           |
| iShares MSCI Brazil ETF  <br>EWZFactsheet                                             | 0.59                  | 5.18                   | 12.78          |
| iShares S&P Mid-Cap 400 Value ETF  <br>IJJFactsheet                                   | 0.18                  | 1.79                   | 6.05           |
| iShares MSCI China ETF  <br>MCHIFactsheet                                             | 0.59                  | 2.11                   | 4.44           |
| iShares Global 100 ETF  <br>IOOFactsheet                                              | 0.4                   | 0.92                   | 0.21           |
| iShares MSCI Taiwan ETF  <br>EWTFactsheet                                             | 0.59                  | 1.55                   | 7.3            |
| iShares S&P Small-Cap 600 Value ETF  <br>IJSFactsheet                                 | 0.18                  | 1.62                   | 8.9            |
| iShares Core MSCI Europe ETF  <br>IEURFactsheet                                       | 0.1                   | 2.97                   | 3.12           |
| iShares International Select Dividend ETF  <br>IDVFactsheet                           | 0.5                   | 4.92                   | 3.55           |
| iShares MSCI World ETF  <br>URTHFactsheet                                             | 0.24                  | 1.49                   | 1.71           |
| iShares Currency Hedged MSCI EAFE ETF  <br>HEFAFactsheet                              | 0.35                  | 3.35                   | 3.6            |
| iShares S&P Small-Cap 600 Growth ETF  <br>IJTFactsheet                                | 0.18                  | 0.91                   | 8.11           |
| iShares China Large-Cap ETF  <br>FXIFactsheet                                         | 0.73                  | 2.4                    | 2.94           |
| iShares Global Tech ETF  <br>IXNFactsheet                                             | 0.39                  | 0.32                   | 1.35           |
| iShares ESG Aware MSCI EM ETF  <br>ESGEFactsheet                                      | 0.25                  | 2.54                   | 6.27           |
| iShares MSCI EAFE Min Vol Factor ETF  <br>EFAVFactsheet                               | 0.2                   | 3.2                    | 1.26           |
| iShares Global Healthcare ETF  <br>IXJFactsheet                                       | 0.4                   | 1.4                    | 2.8            |
| iShares MSCI Canada ETF  <br>EWCFactsheet                                             | 0.5                   | 1.45                   | 2.49           |
| iShares Russell Top 200 Value ETF  <br>IWXFactsheet                                   | 0.2                   | 1.59                   | 3.95           |
| iShares MSCI Intl Momentum Factor ETF  <br>IMTMFactsheet                              | 0.3                   | 2.31                   | 4.73           |
| iShares MSCI Emerging Markets Min Vol Factor ETF  <br>EEMVFactsheet                   | 0.25                  | 2.64                   | 4.21           |
| iShares MSCI All Country Asia ex Japan ETF  <br>AAXJFactsheet                         | 0.72                  | 1.79                   | 6.1            |
| iShares Latin America 40 ETF  <br>ILFFactsheet                                        | 0.47                  | 4.38                   | 12.93          |
| iShares MSCI Intl Value Factor ETF  <br>IVLUFactsheet                                 | 0.31                  | 3.71                   | 4.21           |
| iShares MSCI Global Min Vol Factor ETF  <br>ACWVFactsheet                             | 0.2                   | 2.09                   | 0.88           |
| iShares Morningstar Mid-Cap Growth ETF  <br>IMCGFactsheet                             | 0.06                  | 0.78                   | 4.42           |
| iShares International Equity Factor ETF  <br>INTFFactsheet                            | 0.16                  | 2.87                   | 3.82           |
| iShares MSCI United Kingdom ETF  <br>EWUFactsheet                                     | 0.5                   | 3.74                   | 2.5            |
| iShares Morningstar Growth ETF  <br>ILCGFactsheet                                     | 0.04                  | 0.47                   | 0.24           |
| iShares Core MSCI Pacific ETF  <br>IPACFactsheet                                      | 0.09                  | 4.33                   | 5.08           |
| iShares Paris-Aligned Climate Optimized MSCI USA ETF  <br>PABUFactsheet               | 0.1                   | 0.9                    | -1.48          |
| iShares Russell 2500 ETF  <br>SMMDFactsheet                                           | 0.15                  | 1.28                   | 8.35           |
| iShares Asia 50 ETF  <br>AIAFactsheet                                                 | 0.5                   | 1.58                   | 9.8            |
| iShares Russell Top 200 ETF  <br>IWLFactsheet                                         | 0.15                  | 0.9                    | 0.37           |
| iShares MSCI Mexico ETF  <br>EWWFactsheet                                             | 0.5                   | 3.48                   | 9.43           |
| iShares Global Clean Energy ETF  <br>ICLNFactsheet                                    | 0.39                  | 1.63                   | 10.04          |
| iShares Global Energy ETF  <br>IXCFactsheet                                           | 0.4                   | 3.68                   | 7.34           |
| iShares MSCI Pacific ex Japan ETF  <br>EPPFactsheet                                   | 0.47                  | 3.77                   | 3.75           |
| iShares MSCI Spain ETF  <br>EWPFactsheet                                              | 0.5                   | 2.28                   | 2.22           |
| iShares MSCI Germany ETF  <br>EWGFactsheet                                            | 0.49                  | 1.6                    | 1.55           |
| iShares Europe ETF  <br>IEVFactsheet                                                  | 0.6                   | 2.72                   | 3.1            |
| iShares MSCI Emerging Markets Asia ETF  <br>EEMAFactsheet                             | 0.49                  | 1.48                   | 5.96           |
| iShares MSCI Switzerland ETF  <br>EWLFactsheet                                        | 0.5                   | 1.71                   | 1.08           |
| iShares Morningstar Mid-Cap ETF  <br>IMCBFactsheet                                    | 0.04                  | 1.42                   | 4.28           |
| iShares Emerging Markets Equity Factor ETF  <br>EMGFFactsheet                         | 0.26                  | 2.52                   | 6.96           |
| iShares U.S. Carbon Transition Readiness Aware Active ETF  <br>LCTUFactsheet          | 0.15                  | 1.02                   | 0.85           |
| iShares MSCI Chile ETF  <br>ECHFactsheet                                              | 0.59                  | 2.01                   | 14.05          |
| iShares Micro-Cap ETF  <br>IWCFactsheet                                               | 0.6                   | 1.1                    | 11.02          |
| iShares MSCI Australia ETF  <br>EWAFactsheet                                          | 0.5                   | 3.2                    | 3.27           |
| iShares Morningstar Value ETF  <br>ILCVFactsheet                                      | 0.04                  | 1.77                   | 1.84           |
| iShares Morningstar U.S. Equity ETF  <br>ILCBFactsheet                                | 0.03                  | 1.11                   | 1.06           |
| iShares International Dividend Growth ETF  <br>IGROFactsheet                          | 0.15                  | 2.51                   | 2.86           |
| iShares Emerging Markets Dividend ETF  <br>DVYEFactsheet                              | 0.5                   | 5.84                   | 7.28           |
| iShares Global Industrials ETF  <br>EXIFactsheet                                      | 0.39                  | 1.32                   | 6.6            |
| iShares Low Carbon Optimized MSCI ACWI ETF  <br>CRBNFactsheet                         | 0.2                   | 2.21                   | 2.2            |
| iShares Morningstar Mid-Cap Value ETF  <br>IMCVFactsheet                              | 0.06                  | 2.23                   | 4.13           |
| iShares Global Consumer Staples ETF  <br>KXIFactsheet                                 | 0.39                  | 2.3                    | 3.66           |
| iShares Morningstar Small-Cap Growth ETF  <br>ISCGFactsheet                           | 0.06                  | 0.61                   | 7.81           |
| iShares MSCI World Small-Cap ETF  <br>WSMLFactsheet                                   | 0.3                   | -                      | 7.62           |
| iShares Cybersecurity and Tech ETF  <br>IHAKFactsheet                                 | 0.47                  | 0.08                   | 0.59           |
| iShares MSCI Singapore ETF  <br>EWSFactsheet                                          | 0.5                   | 4.09                   | 1.76           |
| iShares MSCI Israel ETF  <br>EISFactsheet                                             | 0.59                  | 1.44                   | 7.56           |
| iShares MSCI South Africa ETF  <br>EZAFactsheet                                       | 0.59                  | 6.19                   | 10.08          |
| iShares Global Comm Services ETF  <br>IXPFactsheet                                    | 0.4                   | 2.92                   | -0.11          |
| iShares MSCI Italy ETF  <br>EWIFactsheet                                              | 0.5                   | 2.81                   | 0.97           |
| iShares MSCI Hong Kong ETF  <br>EWHFactsheet                                          | 0.5                   | 5.17                   | 6.61           |
| iShares ESG Select Screened S&P 500 ETF  <br>XVVFactsheet                             | 0.08                  | 0.94                   | 0.32           |
| iShares ESG Advanced MSCI EAFE ETF  <br>DMXFFactsheet                                 | 0.12                  | 4.83                   | 3.71           |
| iShares MSCI Saudi Arabia ETF  <br>KSAFactsheet                                       | 0.75                  | 3.81                   | 6.58           |
| iShares Currency Hedged MSCI Eurozone ETF  <br>HEZUFactsheet                          | 0.53                  | 2.92                   | 3.16           |
| iShares Global Financials ETF  <br>IXGFactsheet                                       | 0.41                  | 2.04                   | 0.15           |
| iShares MSCI India Small-Cap ETF  <br>SMINFactsheet                                   | 0.74                  | 0                      | -6.46          |
| iShares Morningstar Small-Cap Value ETF  <br>ISCVFactsheet                            | 0.06                  | 2.04                   | 7.12           |
| iShares India 50 ETF  <br>INDYFactsheet                                               | 0.65                  | 0.57                   | -4.53          |
| iShares MSCI Japan Value ETF  <br>EWJVFactsheet                                       | 0.15                  | 5.38                   | 5.65           |
| iShares International Small-Cap Equity Factor ETF  <br>ISCFFactsheet                  | 0.24                  | 3.76                   | 5.53           |
| iShares MSCI Poland ETF  <br>EPOLFactsheet                                            | 0.59                  | 4.8                    | 6.29           |
| iShares Currency Hedged MSCI Japan ETF  <br>HEWJFactsheet                             | 0.49                  | 4.54                   | 6.44           |
| iShares MSCI Peru and Global Exposure ETF  <br>EPUFactsheet                           | 0.59                  | 1.65                   | 19.17          |
| iShares MSCI Emerging Markets Small-Cap ETF  <br>EEMSFactsheet                        | 0.72                  | 3.09                   | 4.86           |
| iShares MSCI France ETF  <br>EWQFactsheet                                             | 0.5                   | 2.63                   | 0.44           |
| iShares MSCI Indonesia ETF  <br>EIDOFactsheet                                         | 0.59                  | 3.89                   | 1.65           |
| iShares ESG Select Screened S&P Mid-Cap ETF  <br>XJHFactsheet                         | 0.12                  | 1.25                   | 6.46           |
| iShares MSCI Sweden ETF  <br>EWDFactsheet                                             | 0.51                  | 3.27                   | 5              |
| iShares Copper and Metals Mining ETF  <br>ICOPFactsheet                               | 0.47                  | 2.06                   | 12.97          |
| iShares Currency Hedged MSCI ACWI ex U.S. ETF  <br>HAWXFactsheet                      | 0.35                  | 2.81                   | 4.66           |
| iShares MSCI Netherlands ETF  <br>EWNFactsheet                                        | 0.5                   | 4.87                   | 8.66           |
| iShares MSCI Malaysia ETF  <br>EWMFactsheet                                           | 0.5                   | 3.4                    | 3.11           |
| iShares Paris-Aligned Climate Optimized MSCI World ex USA ETF  <br>PABDFactsheet      | 0.12                  | 2.75                   | 3.06           |
| iShares Global Materials ETF  <br>MXIFactsheet                                        | 0.39                  | 2.02                   | 10.01          |
| iShares MSCI Turkey ETF  <br>TURFactsheet                                             | 0.59                  | 2.41                   | 13.51          |
| iShares Global Consumer Discretionary ETF  <br>RXIFactsheet                           | 0.39                  | 1.55                   | 2.51           |
| iShares Global Timber & Forestry ETF  <br>WOODFactsheet                               | 0.4                   | 2.5                    | 6.59           |
| iShares Morningstar Small-Cap ETF  <br>ISCBFactsheet                                  | 0.04                  | 1.38                   | 7.44           |
| iShares Global Utilities ETF  <br>JXIFactsheet                                        | 0.39                  | 2.56                   | 1.45           |
| iShares MSCI Thailand ETF  <br>THDFactsheet                                           | 0.59                  | 3.38                   | 5.6            |
| iShares World ex U.S. Carbon Transition Readiness Aware Active ETF  <br>LCTDFactsheet | 0.22                  | 3.61                   | 3.4            |
| iShares MSCI Kokusai ETF  <br>TOKFactsheet                                            | 0.25                  | 1.37                   | 1.5            |
| iShares MSCI Denmark ETF  <br>EDENFactsheet                                           | 0.53                  | 2.79                   | 7.3            |
| iShares MSCI China A ETF  <br>CNYAFactsheet                                           | 0.6                   | 1.92                   | 3.32           |
| iShares Currency Hedged MSCI Emerging Markets ETF  <br>HEEMFactsheet                  | 0.72                  | 2.24                   | 7.53           |
| iShares MSCI Brazil Small-Cap ETF  <br>EWZSFactsheet                                  | 0.59                  | 3.85                   | 11.12          |
| iShares MSCI Global Quality Factor ETF  <br>AQLTFactsheet                             | 0.2                   | 1.06                   | 2.85           |
| iShares MSCI Japan Small-Cap ETF  <br>SCJFactsheet                                    | 0.5                   | 3.14                   | 5.16           |
| iShares Large Cap 10% Target Buffer Mar ETF  <br>TENMFactsheet                        | 0.5                   | -                      | 0.75           |
| iShares Currency Hedged MSCI EAFE Small-Cap ETF  <br>HSCZFactsheet                    | 0.43                  | 3.26                   | 5.22           |
| iShares MSCI UAE ETF  <br>UAEFactsheet                                                | 0.59                  | 4.09                   | 6.99           |
| iShares MSCI Global Sustainable Development Goals ETF  <br>SDGFactsheet               | 0.5                   | 1.99                   | 0.38           |
| iShares US Small Cap Value Factor ETF  <br>SVALFactsheet                              | 0.2                   | 2.3                    | 8.64           |
| iShares Large Cap Max Buffer Jun ETF  <br>MAXJFactsheet                               | 0.5                   | 0.76                   | 0.36           |
| iShares MSCI Philippines ETF  <br>EPHEFactsheet                                       | 0.59                  | 2.11                   | 5.45           |
| iShares Global Equity Factor ETF  <br>GLOFFactsheet                                   | 0.2                   | 1.7                    | 1.87           |
| iShares MSCI Europe Small-Cap ETF  <br>IEUSFactsheet                                  | 0.41                  | 3.2                    | 4.13           |
| iShares Genomics Immunology and Healthcare ETF  <br>IDNAFactsheet                     | 0.47                  | 1.18                   | 14.86          |
| iShares Large Cap Moderate Quarterly Laddered ETF  <br>IVVMFactsheet                  | 0.5                   | 0.62                   | 0.69           |
| iShares MSCI Austria ETF  <br>EWOFactsheet                                            | 0.49                  | 2.39                   | 5.02           |
| iShares ESG Advanced MSCI EM ETF  <br>EMXFFactsheet                                   | 0.16                  | 3.51                   | 5.27           |
| iShares Large Cap Deep Quarterly Laddered ETF  <br>IVVBFactsheet                      | 0.51                  | 1.22                   | 0.75           |
| iShares Large Cap Max Buffer Dec ETF  <br>DMAXFactsheet                               | 0.5                   | 0.9                    | 0.23           |
| iShares Large Cap Max Buffer Sep ETF  <br>SMAXFactsheet                               | 0.5                   | 0.78                   | 0.48           |
| iShares International Equity Factor Rotation Active ETF  <br>IDYNFactsheet            | 0.45                  | -                      | 4.53           |
| iShares ESG Select Screened S&P Small-Cap ETF  <br>XJRFactsheet                       | 0.12                  | 1.14                   | 8.14           |
| iShares JPX-Nikkei 400 ETF  <br>JPXNFactsheet                                         | 0.48                  | 3.15                   | 5.4            |
| iShares Large Cap Value Active ETF  <br>BLCVFactsheet                                 | 0.46                  | 1.37                   | 3.79           |
| iShares International Developed Small Cap Value Factor ETF  <br>ISVLFactsheet         | 0.31                  | 2.68                   | 5.39           |
| iShares MSCI China Small-Cap ETF  <br>ECNSFactsheet                                   | 0.59                  | 6.15                   | 8.3            |
| iShares MSCI BIC ETF  <br>BKFFactsheet                                                | 0.72                  | 1.8                    | 2.31           |
| iShares MSCI Kuwait ETF  <br>KWTFactsheet                                             | 0.75                  | 5.38                   | -0.97          |
| iShares MSCI Qatar ETF  <br>QATFactsheet                                              | 0.6                   | 3.5                    | 5.42           |
| iShares MSCI Ireland ETF  <br>EIRLFactsheet                                           | 0.5                   | 2.72                   | 1.39           |
| iShares MSCI New Zealand ETF  <br>ENZLFactsheet                                       | 0.5                   | 2.23                   | 3.31           |
| iShares Asia/Pacific Dividend ETF  <br>DVYAFactsheet                                  | 0.49                  | 4.69                   | 7.07           |
| iShares Defense Industrials Active ETF  <br>IDEFFactsheet                             | 0.55                  | -                      | 14.45          |
| iShares MSCI China Multisector Tech ETF  <br>TCHIFactsheet                            | 0.59                  | 2.44                   | 7.55           |
| iShares MSCI United Kingdom Small-Cap ETF  <br>EWUSFactsheet                          | 0.59                  | 3.59                   | 5.15           |
| iShares MSCI Norway ETF  <br>ENORFactsheet                                            | 0.53                  | 2.96                   | 5.14           |
| iShares Large Cap 10% Target Buffer Dec ETF  <br>TENDFactsheet                        | 0.5                   | -                      | 0.75           |
| iShares MSCI Finland ETF  <br>EFNLFactsheet                                           | 0.53                  | 3.4                    | 3.53           |
| iShares ESG MSCI EM Leaders ETF  <br>LDEMFactsheet                                    | 0.16                  | 3.24                   | 5.66           |
| iShares Large Cap Max Buffer Mar ETF  <br>MMAXFactsheet                               | 0.5                   | -                      | 0.34           |
| iShares Large Cap 10% Target Buffer Sep ETF  <br>STENFactsheet                        | 0.5                   | -                      | 0.91           |
| iShares Energy Storage & Materials ETF  <br>IBATFactsheet                             | 0.47                  | 1.15                   | 12.97          |
| iShares MSCI Belgium ETF  <br>EWKFactsheet                                            | 0.49                  | 1.74                   | 5.05           |
| iShares Large Cap Accelerated Outcome ETF  <br>TWOXFactsheet                          | 0.5                   | -                      | 1.11           |
| iShares Lithium Miners and Producers ETF  <br>ILITFactsheet                           | 0.47                  | 2.24                   | 20.15          |
| iShares Infrastructure Active ETF  <br>BILTFactsheet                                  | 0.6                   | -                      | 2.51           |
| iShares International Country Rotation Active ETF  <br>COROFactsheet                  | 0.55                  | 3.62                   | 5              |
| iShares Large Cap 10% Target Buffer Jun ETF  <br>TENJFactsheet                        | 0.5                   | -                      | 0.79           |
| iShares Emerging Markets Infrastructure ETF  <br>EMIFFactsheet                        | 0.6                   | 4.97                   | 7.5            |
| iShares FinTech Active ETF  <br>BPAYFactsheet                                         | 0.55                  | 2.61                   | 0.49           |
| iShares Large Cap Growth Active ETF  <br>BGROFactsheet                                | 0.55                  | 0.04                   | 0.84           |
| iShares Future Metaverse Tech and Communications ETF  <br>IVRSFactsheet               | 0.47                  | 0.32                   | 2.12           |
| iShares Environmental Infrastructure and Industrials ETF  <br>EFRAFactsheet           | 0.47                  | 1.67                   | 6.18           |
| iShares Neuroscience and Healthcare ETF  <br>IBRNFactsheet                            | 0.47                  | 0.98                   | 3.79           |
| iShares Breakthrough Environmental Solutions ETF  <br>ETECFactsheet                   | 0.47                  | 0.33                   | 5.56           |


|                                                                   |
| ----------------------------------------------------------------- |
|                                                                   |
| Ticker  <br>Nombre del Fondo                                      |
| iShares MSCI Australia ETF  <br>EWA                               |
| iShares MSCI Canada ETF  <br>EWC                                  |
| iShares MSCI France ETF  <br>EWQ                                  |
| iShares MSCI Germany ETF  <br>EWG                                 |
| iShares MSCI Hong Kong ETF  <br>EWH                               |
| iShares MSCI Italy ETF  <br>EWI                                   |
| iShares MSCI Japan ETF  <br>EWJ                                   |
| iShares MSCI Malaysia ETF  <br>EWM                                |
| iShares MSCI Mexico ETF  <br>EWW                                  |
| iShares MSCI Netherlands ETF  <br>EWN                             |
| iShares MSCI Singapore ETF  <br>EWS                               |
| iShares MSCI Spain ETF  <br>EWP                                   |
| iShares MSCI Switzerland ETF  <br>EWL                             |
| iShares MSCI United Kingdom ETF  <br>EWU                          |
| iShares MSCI South Korea ETF  <br>EWY                             |
| iShares U.S. Technology ETF  <br>IYW                              |
| iShares Russell 1000 ETF  <br>IWB                                 |
| iShares Core S&P 500 ETF  <br>IVV                                 |
| iShares U.S. Financials ETF  <br>IYF                              |
| iShares U.S. Telecommunications ETF  <br>IYZ                      |
| iShares Russell 1000 Growth ETF  <br>IWF                          |
| iShares Russell 1000 Value ETF  <br>IWD                           |
| iShares Russell 2000 ETF  <br>IWM                                 |
| iShares Russell 3000 ETF  <br>IWV                                 |
| iShares S&P 500 Growth ETF  <br>IVW                               |
| iShares S&P 500 Value ETF  <br>IVE                                |
| iShares Core S&P Mid-Cap ETF  <br>IJH                             |
| iShares Core S&P Small-Cap ETF  <br>IJR                           |
| iShares U.S. Basic Materials ETF  <br>IYM                         |
| iShares U.S. Consumer Staples ETF  <br>IYK                        |
| iShares U.S. Consumer Discretionary ETF  <br>IYC                  |
| iShares U.S. Energy ETF  <br>IYE                                  |
| iShares U.S. Financial Services ETF  <br>IYG                      |
| iShares U.S. Healthcare ETF  <br>IYH                              |
| iShares U.S. Industrials ETF  <br>IYJ                             |
| iShares U.S. Utilities ETF  <br>IDU                               |
| iShares MSCI Taiwan ETF  <br>EWT                                  |
| iShares MSCI Brazil ETF  <br>EWZ                                  |
| iShares Russell 2000 Growth ETF  <br>IWO                          |
| iShares Russell 2000 Value ETF  <br>IWN                           |
| iShares Core S&P U.S. Growth ETF  <br>IUSG                        |
| iShares Core S&P U.S. Value ETF  <br>IUSV                         |
| iShares MSCI Eurozone ETF  <br>EZU                                |
| iShares Europe ETF  <br>IEV                                       |
| iShares S&P 100 ETF  <br>OEF                                      |
| iShares Biotechnology ETF  <br>IBB                                |
| iShares Russell Mid-Cap Growth ETF  <br>IWP                       |
| iShares Russell Mid-Cap ETF  <br>IWR                              |
| iShares Russell Mid-Cap Value ETF  <br>IWS                        |
| iShares MSCI EAFE ETF  <br>EFA                                    |
| iShares North American Natural Resources ETF  <br>IGE             |
| iShares MSCI Pacific ex Japan ETF  <br>EPP                        |
| iShares Latin America 40 ETF  <br>ILF                             |
| iShares Global Energy ETF  <br>IXC                                |
| iShares Global Financials ETF  <br>IXG                            |
| iShares MSCI South Africa ETF  <br>EZA                            |
| iShares MSCI Emerging Markets ETF  <br>EEM                        |
| iShares Select Dividend ETF  <br>DVY                              |
| iShares Core S&P Total U.S. Stock Market ETF  <br>ITOT            |
| iShares China Large-Cap ETF  <br>FXI                              |
| iShares ESG Optimized MSCI USA ETF  <br>SUSA                      |
| iShares MSCI EAFE Growth ETF  <br>EFG                             |
| iShares Micro-Cap ETF  <br>IWC                                    |
| iShares U.S. Home Construction ETF  <br>ITB                       |
| iShares U.S. Oil Equipment & Services ETF  <br>IEZ                |
| iShares Global Consumer Discretionary ETF  <br>RXI                |
| iShares Global Consumer Staples ETF  <br>KXI                      |
| iShares Global Materials ETF  <br>MXI                             |
| iShares MSCI BIC ETF  <br>BKF                                     |
| iShares MSCI Chile ETF  <br>ECH                                   |
| iShares MSCI EAFE Small-Cap ETF  <br>SCZ                          |
| iShares Global Infrastructure ETF  <br>IGF                        |
| iShares MSCI Japan Small-Cap ETF  <br>SCJ                         |
| iShares MSCI ACWI ex U.S. ETF  <br>ACWX                           |
| iShares MSCI ACWI ETF  <br>ACWI                                   |
| iShares MSCI Israel ETF  <br>EIS                                  |
| iShares MSCI Thailand ETF  <br>THD                                |
| iShares MSCI Turkey ETF  <br>TUR                                  |
| iShares Global Clean Energy ETF  <br>ICLN                         |
| iShares MSCI All Country Asia ex Japan ETF  <br>AAXJ              |
| iShares Emerging Markets Infrastructure ETF  <br>EMIF             |
| iShares MSCI Peru and Global Exposure ETF  <br>EPU                |
| iShares India 50 ETF  <br>INDY                                    |
| iShares MSCI Europe Financials ETF  <br>EUFN                      |
| iShares MSCI Indonesia ETF  <br>EIDO                              |
| iShares MSCI Ireland ETF  <br>EIRL                                |
| iShares Core S&P 500 UCITS ETF  <br>CSPX                          |
| iShares MSCI Poland ETF  <br>EPOL                                 |
| iShares MSCI New Zealand ETF  <br>ENZL                            |
| iShares MSCI Brazil Small-Cap ETF  <br>EWZS                       |
| iShares MSCI China Small-Cap ETF  <br>ECNS                        |
| iShares MSCI Philippines ETF  <br>EPHE                            |
| iShares Core High Dividend ETF  <br>HDV                           |
| iShares MSCI China ETF  <br>MCHI                                  |
| iShares MSCI Global Min Vol Factor ETF  <br>ACWV                  |
| iShares MSCI EAFE Min Vol Factor ETF  <br>EFAV                    |
| iShares MSCI Emerging Markets Min Vol Factor ETF  <br>EEMV        |
| iShares MSCI USA Min Vol Factor ETF  <br>USMV                     |
| iShares MSCI ACWI UCITS ETF  <br>ISAC                             |
| iShares MSCI India ETF  <br>INDA                                  |
| iShares Core MSCI Total International Stock ETF  <br>IXUS         |
| iShares Core MSCI Emerging Markets ETF  <br>IEMG                  |
| iShares MSCI USA Size Factor ETF  <br>SIZE                        |
| iShares MSCI USA Momentum Factor ETF  <br>MTUM                    |
| iShares MSCI USA Value Factor ETF  <br>VLUE                       |
| iShares MSCI USA Quality Factor ETF  <br>QUAL                     |
| iShares Currency Hedged MSCI EAFE ETF  <br>HEFA                   |
| iShares Currency Hedged MSCI Japan ETF  <br>HEWJ                  |
| iShares Core MSCI EM IMI UCITS ETF  <br>EIMI                      |
| iShares Core Dividend Growth ETF  <br>DGRO                        |
| iShares Currency Hedged MSCI Eurozone ETF  <br>HEZU               |
| iShares Currency Hedged MSCI Emerging Markets ETF  <br>HEEM       |
| iShares Low Carbon Optimized MSCI ACWI ETF  <br>CRBN              |
| iShares Future Exponential Technologies ETF  <br>XT               |
| iShares MSCI China A UCITS ETF  <br>CNYA                          |
| iShares U.S. Equity Factor ETF  <br>LRGF                          |
| iShares S&P 500 Information Technology Sector UCITS ETF  <br>IUIT |
| iShares S&P 500 Financials Sector UCITS ETF  <br>IUFS             |
| iShares ESG Aware MSCI EM ETF  <br>ESGE                           |
| iShares ESG Aware MSCI EAFE ETF  <br>ESGD                         |
| iShares MSCI USA SRI UCITS ETF  <br>SUAS                          |
| iShares MSCI EM SRI UCITS ETF  <br>SUSM                           |
| iShares Healthcare Innovation UCITS ETF  <br>HEAL                 |
| iShares Digitalisation UCITS ETF  <br>DGTL                        |
| iShares Automation & Robotics UCITS ETF  <br>RBOT                 |
| iShares ESG Aware MSCI USA ETF  <br>ESGU                          |
| iShares U.S. Infrastructure ETF  <br>IFRA                         |
| iShares ESG Aware MSCI USA Small-Cap ETF  <br>ESML                |
| iShares Future AI & Tech ETF  <br>ARTY                            |
| iShares U.S. Equity Factor Rotation Active ETF  <br>DYNF          |
| iShares Self-Driving EV and Tech ETF  <br>IDRV                    |
| iShares ESG MSCI USA Leaders ETF  <br>SUSL                        |
| iShares Cybersecurity and Tech ETF  <br>IHAK                      |
| iShares Genomics Immunology and Healthcare ETF  <br>IDNA          |
| iShares U.S. Tech Breakthrough Multisector ETF  <br>TECB          |
| iShares ESG MSCI EM Leaders ETF  <br>LDEM                         |
| iShares ESG Advanced MSCI EAFE ETF  <br>DMXF                      |
| iShares ESG Advanced MSCI USA ETF  <br>USXF                       |
| iShares MSCI Europe SRI UCITS ETF  <br>IDSE                       |
| iShares Large Cap Moderate Quarterly Laddered ETF  <br>IVVMCL     |
| iShares Large Cap Deep Quarterly Laddered ETF  <br>IVVB           |
| iShares U.S. Large Cap Premium Income Active ETF  <br>BALICL      |
|                                                                   |