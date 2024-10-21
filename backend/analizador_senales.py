import pandas as pd

class AnalizadorSenales:
    def __init__(self):
        pass

    def identificar_senales_compra(self, datos_macd):
        """
        Identifica señales de compra basadas en el MACD.

        :param datos_macd: DataFrame con los valores del MACD, la señal y el histograma.
        :return: DataFrame con las señales de compra identificadas.
        """
        senales = pd.DataFrame(index=datos_macd.index)

        # Señal de compra: cuando el MACD cruza por encima de la línea de señal
        senales['senal_compra'] = (datos_macd['macd'] > datos_macd['senal']) & (datos_macd['macd'].shift(1) <= datos_macd['senal'].shift(1))

        # Señal de venta: cuando el MACD cruza por debajo de la línea de señal
        senales['senal_venta'] = (datos_macd['macd'] < datos_macd['senal']) & (datos_macd['macd'].shift(1) >= datos_macd['senal'].shift(1))

        # Fuerza de la señal: basada en la magnitud del histograma
        senales['fuerza_senal'] = abs(datos_macd['histograma'])

        return senales
