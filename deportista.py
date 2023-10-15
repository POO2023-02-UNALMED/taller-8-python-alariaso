class Deportista:
    def __init__(self, deporte: str, añosPracticando: int) -> None:
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, deporte: str):
        self._deporte = deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAnosPracticando(self, añosPracticando: int):
        self._añosPracticando = añosPracticando
