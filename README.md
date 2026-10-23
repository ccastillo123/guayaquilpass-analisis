# guayaquilpass-analisis

Este repositorio contiene los scripts para el análisis de ventas del proyecto GuayaquilPass desde Supabase.

## Descripción del Proyecto
El objetivo de este proyecto es leer los datos de ventas de Supabase, agruparlos mensualmente para obtener el monto total y la cantidad de ventas, y luego generar visualizaciones claras de esta información. Este análisis forma parte de un pipeline más amplio de análisis de riesgo crediticio.

## Scripts

- `read_supabase_sales.py`: Script para conectarse a Supabase y extraer los datos de ventas de un rango de fechas específico. Utiliza la tabla `ventas`.
- `monthly_summary.py`: Procesa los datos de ventas brutos para generar un resumen mensual, calculando el monto total de ventas y la cantidad total de artículos vendidos por mes.
- `generate_graphs.py`: Genera dos gráficos en formato PNG: un gráfico de barras del monto total de ventas por mes y un gráfico de línea de la cantidad de ventas por mes. Los gráficos están personalizados con títulos, etiquetas en español y meses abreviados.

## Conexiones y Variables de Entorno

Este proyecto se conecta a una base de datos Supabase. Las credenciales de conexión (URL y clave de API) **no deben ser hardcodeadas** en los scripts ni subidas al repositorio por seguridad. En su lugar, deben configurarse como variables de entorno:

- `SUPABASE_URL`: La URL de tu proyecto Supabase (ej. `https://your-project-id.supabase.co`).
- `SUPABASE_KEY`: Tu clave de anon (public anon key) de Supabase.

**Cómo configurar las variables de entorno (ejemplo para Linux/macOS):**

