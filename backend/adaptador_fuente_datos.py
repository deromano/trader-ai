import yfinance as yf
from datetime import date

class AdaptadorFuenteDatos:
    def __init__(self):
        # No se necesita inicialización especial para yfinance
        pass

    def obtener_datos(self, simbolo: str, fecha_inicio: date, fecha_fin: date):
        """
        Obtiene los datos históricos de una acción desde Yahoo Finance.

        :param simbolo: El símbolo de la acción.
        :param fecha_inicio: La fecha de inicio del rango de datos.
        :param fecha_fin: La fecha de fin del rango de datos.
        :return: Los datos históricos de la acción como un DataFrame de pandas.
        """
        ticker = yf.Ticker(simbolo)
        datos_historicos = ticker.history(start=fecha_inicio, end=fecha_fin)

        # Renombrar columnas para mantener consistencia con el ejemplo anterior
        datos_historicos = datos_historicos.rename(columns={
            'Open': 'apertura',
            'Close': 'cierre',
            'High': 'alto',
            'Low': 'bajo',
            'Volume': 'volumen'
        })

        return datos_historicos.reset_index()  # Convierte la fecha en una columna
