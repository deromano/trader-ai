import pandas as pd

class CalculadorMACD:
    def __init__(self, periodo_rapido=12, periodo_lento=26, periodo_senal=9):
        self.periodo_rapido = periodo_rapido
        self.periodo_lento = periodo_lento
        self.periodo_senal = periodo_senal

    def calcular_macd(self, datos):
        """
        Calcula el indicador MACD para una serie de datos.

        :param datos: DataFrame con los datos históricos de la acción.
        :return: DataFrame con los valores del MACD, la señal y el histograma.
        """
        # Asegurarse de que 'fecha' es el índice
        if 'fecha' in datos.columns:
            datos = datos.set_index('fecha')

        # Calcular las medias móviles exponenciales
        ema_rapida = datos['cierre'].ewm(span=self.periodo_rapido, adjust=False).mean()
        ema_lenta = datos['cierre'].ewm(span=self.periodo_lento, adjust=False).mean()

        # Calcular la línea MACD
        datos['macd'] = ema_rapida - ema_lenta

        # Calcular la línea de señal
        datos['senal'] = datos['macd'].ewm(span=self.periodo_senal, adjust=False).mean()

        # Calcular el histograma
        datos['histograma'] = datos['macd'] - datos['senal']

        return datos[['macd', 'senal', 'histograma']]
