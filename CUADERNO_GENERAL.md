# CUADERNO_GENERAL.md — Bitácora maestra del proyecto

## 1. Identificación
**Proyecto:** Diversificación productiva, crecimiento económico y desarrollo sostenible en Ecuador bajo dolarización.  
**Periodo:** 2000-I a 2024-IV.  
**Unidad de análisis:** economía ecuatoriana.  
**Frecuencia:** trimestral.  
**Método central:** índice Herfindahl-Hirschman + series de tiempo.

## 2. Línea de investigación
**Línea de facultad:** Administración y Economía para el desarrollo sostenible de las organizaciones.  
**Sublínea principal:** Economía y Desarrollo sostenible.  
**Sublínea secundaria:** Economía, sociedad y políticas públicas.

## 3. Paper base
Siddiqui y Afzal (2022) analizan la diversificación sectorial de Emiratos Árabes Unidos hacia una economía basada en conocimiento. Usan HHI para medir diversificación sectorial y DEA para eficiencia de pilares de economía del conocimiento.

**Adaptación al Ecuador:**
- Se replica el uso del HHI.
- Se reemplaza el enfoque descriptivo/DEA por análisis econométrico trimestral.
- El eje interpretativo será dolarización, estructura productiva, crecimiento y sostenibilidad.

## 4. Problema de investigación
Ecuador bajo dolarización ha mantenido una estructura productiva y exportadora concentrada en pocos sectores, lo cual puede limitar la estabilidad del crecimiento, la resiliencia ante shocks externos y la transición hacia un desarrollo sostenible. Se requiere medir esa concentración/diversificación de forma trimestral y estimar su relación con el crecimiento económico.

## 5. Pregunta de investigación
¿Cómo ha incidido la diversificación productiva, medida mediante el índice Herfindahl-Hirschman, en el crecimiento económico del Ecuador bajo dolarización durante el período 2000-I a 2024-IV, desde una perspectiva de desarrollo sostenible?

## 6. Objetivo general
Analizar la incidencia de la diversificación productiva, medida mediante el índice Herfindahl-Hirschman, sobre el crecimiento económico del Ecuador bajo dolarización durante el período 2000-I a 2024-IV, mediante evidencia econométrica trimestral, con el fin de aportar criterios para políticas de desarrollo sostenible.

## 7. Objetivos específicos
1. Calcular y describir la evolución del índice Herfindahl-Hirschman trimestral para Ecuador durante 2000-I a 2024-IV.
2. Analizar la relación estadística entre concentración/diversificación productiva y crecimiento económico.
3. Estimar los efectos de corto y largo plazo mediante ARDL o VECM según el orden de integración y la existencia de cointegración.
4. Evaluar la robustez de los resultados incorporando quiebres estructurales y especificaciones alternativas.
5. Formular implicaciones de política económica para desarrollo productivo sostenible.

## 8. Hipótesis iniciales
**H1:** Una mayor concentración productiva/exportadora, medida por un HHI más alto, se asocia con menor estabilidad del crecimiento económico en el largo plazo.  
**H2:** En el corto plazo, la concentración en sectores rentables puede tener efectos positivos transitorios sobre el crecimiento.  
**H3:** La diversificación productiva tiene mayor efecto sobre crecimiento sostenible cuando se combina con inversión, innovación y apertura comercial.

## 9. Variables tentativas
**Dependiente:** crecimiento económico trimestral, preferiblemente variación del PIB real trimestral o diferencia logarítmica del PIB real.  
**Principal:** HHI trimestral de exportaciones o producción.  
**Controles:** FBKF real, precio del petróleo, apertura comercial, empleo, términos de intercambio, crédito al sector privado, proxy de innovación si existe.

## 10. Decisiones metodológicas
- ARDL será el modelo principal si las variables son I(0) e I(1), sin I(2).
- VECM será modelo alternativo solo si hay cointegración clara entre variables I(1).
- Se evaluarán quiebres estructurales por eventos macroeconómicos.
- No se utilizarán datos trimestralizados artificialmente salvo que exista justificación técnica y se declare como limitación.

## 11. Registro de avances
### 2026-05-12
- Se define tema oficial.
- Se selecciona paper base de Siddiqui y Afzal (2022).
- Se decide adaptar HHI al caso ecuatoriano bajo dolarización.
- Se decide no usar DEA como método principal.

## 12. Riesgos actuales
- Falta de datos trimestrales sectoriales completos.
- Confusión entre HHI como concentración y diversificación.
- Sobreparametrización en modelos dinámicos.
- Interpretar Granger o cointegración como causalidad estructural fuerte.

## 13. Próximas acciones
1. Identificar fuentes de datos trimestrales del BCE.
2. Definir si el HHI será exportador, productivo o ambos.
3. Crear diccionario de datos.
4. Construir primer script de cálculo del HHI.
5. Crear matriz de literatura.
