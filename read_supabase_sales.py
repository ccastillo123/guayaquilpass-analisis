# Script: read_supabase_sales.py
# Descripción: Conecta a Supabase para leer los datos de ventas.
# Asume que las credenciales de Supabase están configuradas como variables de entorno.

import os
from supabase import create_client, Client
import pandas as pd

def read_sales_data_from_supabase(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Lee los datos de ventas de la tabla 'ventas' de Supabase
    para un rango de fechas específico.
    """
    # Asegúrate de que las variables de entorno estén configuradas
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("Las variables de entorno SUPABASE_URL y SUPABASE_KEY deben estar configuradas.")

    supabase: Client = create_client(url, key)

    # Consulta para obtener los datos de ventas
    # En un caso real, podrías necesitar un ID de venta o ajustar la consulta
    response = supabase.table('ventas').select('fecha, cantidad, precio_unitario').gte('fecha', start_date).lte('fecha', end_date).order('fecha').execute()

    # Supabase devuelve un objeto Response, necesitamos acceder a la data
    data = response.data

    # Convertir a DataFrame de pandas
    df = pd.DataFrame(data)

    # Convertir 'precio_unitario' a tipo numérico (float)
    df['precio_unitario'] = df['precio_unitario'].astype(float)

    return df

if __name__ == "__main__":
    # Ejemplo de uso: leer ventas de enero a septiembre de 2026
    df_sales = read_sales_data_from_supabase('2026-01-01', '2026-09-30')
    print("Datos de ventas leídos correctamente:")
    print(df_sales.head())
    print(f"Total de registros: {len(df_sales)}")
