# Script: generate_graphs.py
# Descripción: Genera gráficos de barras (monto total por mes) y de línea (cantidad de ventas por mes).

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def generate_sales_graphs(df_monthly: pd.DataFrame, output_path: str = "."):
    """
    Genera y guarda dos gráficos de ventas:
    1. Barras: Monto total de ventas por mes.
    2. Línea: Cantidad de ventas por mes.
    
    Los gráficos se guardan como archivos PNG.
    """
    # Configuración de matplotlib para español y meses abreviados
    plt.rcParams['figure.figsize'] = (10, 6) # Tamaño de la figura
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10

    # Nombres abreviados de los meses en español
    meses_abreviados = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    df_monthly['mes_abreviado'] = df_monthly['fecha'].dt.month.apply(lambda x: meses_abreviados[x-1])

    # --- Gráfico de Barras: Monto Total por Mes ---
    fig1, ax1 = plt.subplots()
    bars = ax1.bar(df_monthly['mes_abreviado'], df_monthly['monto_total'], color='skyblue')
    ax1.set_title('Monto Total de Ventas Mensuales (Ene-Sep 2026)')
    ax1.set_xlabel('Mes')
    ax1.set_ylabel('Monto Total ($)')
    ax1.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.2f')) # Formato de moneda
    plt.xticks(rotation=45, ha='right')
    
    # Añadir el valor encima de cada barra
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'${yval:,.2f}', ha='center', va='bottom', rotation=45)
    
    plt.tight_layout()
    plt.savefig(f'{output_path}/monto_total_ventas_mensuales.png')
    plt.close(fig1)

    # --- Gráfico de Línea: Cantidad de Ventas por Mes ---
    fig2, ax2 = plt.subplots()
    ax2.plot(df_monthly['mes_abreviado'], df_monthly['cantidad_ventas'], marker='o', color='lightcoral', linestyle='-')
    ax2.set_title('Cantidad de Ventas Mensuales (Ene-Sep 2026)')
    ax2.set_xlabel('Mes')
    ax2.set_ylabel('Cantidad de Ventas')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig(f'{output_path}/cantidad_ventas_mensuales.png')
    plt.close(fig2)

    print(f"Gráficos guardados en: {output_path}/")

if __name__ == "__main__":
    # Ejemplo de uso (crear un DataFrame de resumen mensual de ejemplo)
    data_monthly = {
        'fecha': pd.to_datetime(['2026-01-01', '2026-02-01', '2026-03-01', '2026-04-01',
                                 '2026-05-01', '2026-06-01', '2026-07-01', '2026-08-01',
                                 '2026-09-01']),
        'cantidad_ventas': [150, 180, 200, 160, 220, 190, 250, 230, 210],
        'monto_total': [15000.50, 18500.75, 21000.00, 16500.25, 23000.80, 19500.10, 26000.40, 24000.60, 22000.90]
    }
    df_example_monthly = pd.DataFrame(data_monthly)
    generate_sales_graphs(df_example_monthly, output_path=".")
