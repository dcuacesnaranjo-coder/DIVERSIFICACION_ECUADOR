# Diccionario de datos — plantilla

| Variable | Nombre corto | Frecuencia | Unidad | Transformación | Fuente | Observaciones |
|---|---|---|---|---|---|---|
| PIB real trimestral | pib_real | Trimestral | USD constantes / índice | log y diferencia log | BCE | Variable dependiente sugerida |
| Crecimiento PIB real | g_pib | Trimestral | porcentaje o log-diff | 100*diff(log(pib_real)) | BCE | Medida principal de crecimiento |
| HHI exportador | hhi_exp | Trimestral | índice 0-1 | sum(participación sectorial^2) | BCE/Comercio exterior | Variable principal |
| FBKF real | fbkf_real | Trimestral | USD constantes | log | BCE | Control |
| Precio petróleo | oil_price | Trimestral | USD/barril | log o nivel | BCE/FRED/EIA | Control externo |
| Apertura comercial | apertura | Trimestral | ratio | (X+M)/PIB | BCE | Control |
| Empleo | empleo | Trimestral | personas | log | INEC/BCE | Control si existe consistente |

## Nota metodológica
Si una variable no tiene frecuencia trimestral confiable, no debe ser forzada. Se debe reemplazar por una proxy o mover a sección de limitaciones.
