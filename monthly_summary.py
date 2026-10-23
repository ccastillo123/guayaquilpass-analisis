# Script: monthly_summary.py
# Descripción: Procesa los datos de ventas para generar un resumen mensual (monto total y cantidad de ventas).

import pandas as pd

def generate_monthly_summary(df_sales: pd.DataFrame) -> pd.DataFrame:
    """
    Genera un resumen mensual de las ventas a partir de un DataFrame de ventas.
    Calcula el monto total de ventas y la cantidad total de artículos vendidos por mes.
    """
    # Asegurarse de que 'fecha' sea tipo datetime
    df_sales['fecha'] = pd.to_datetime(df_sales['fecha'])

    # Calcular el monto total por cada fila
    df_sales['monto_total_fila'] = df_sales['cantidad'] * df_sales['precio_unitario']

    # Agrupar por mes y sumar la cantidad y el monto total
    df_monthly = df_sales.groupby(df_sales['fecha'].dt.to_period('M')).agg(
        cantidad_ventas=('cantidad', 'sum'),
        monto_total=('monto_total_fila', 'sum')
    ).reset_index()

    # Convertir el periodo a formato de fecha para mejor visualización
    df_monthly['fecha'] = df_monthly['fecha'].dt.to_timestamp()

    return df_monthly

if __name__ == "__main__":
    # Ejemplo de uso (crear un DataFrame de ejemplo)
    data = {
        'fecha': pd.to_datetime(['2026-01-15', '2026-01-20', '2026-02-10', '2026-02-25', '2026-03-05']),
        'cantidad': [10, 5, 8, 12, 7],
        'precio_unitario': [10.50, 20.00, 15.25, 5.00, 25.75]
    }
    df_example_sales = pd.DataFrame(data)
    df_monthly_summary = generate_monthly_summary(df_example_sales)
    print("Resumen mensual generado:")
    print(df_monthly_summary)
