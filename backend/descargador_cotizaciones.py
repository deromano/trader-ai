from datetime import date
from adaptador_fuente_datos import AdaptadorFuenteDatos

class DescargadorCotizaciones:
    def __init__(self):
        self.adaptador_fuente_datos = AdaptadorFuenteDatos()

    def descargar_datos_historicos(self, simbolo: str, fecha_inicio: date, fecha_fin: date):
        """
        Descarga los datos históricos de una acción desde Yahoo Finance.

        :param simbolo: El símbolo de la acción.
        :param fecha_inicio: La fecha de inicio del rango de datos.
        :param fecha_fin: La fecha de fin del rango de datos.
        :return: Los datos históricos de la acción como un DataFrame de pandas.
        """
        return self.adaptador_fuente_datos.obtener_datos(simbolo, fecha_inicio, fecha_fin)
