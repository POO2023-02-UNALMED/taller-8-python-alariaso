from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(
        self,
        nombre: str,
        edad: int,
        altura: str,
        sexo: str,
        añosPracticando: int,
        golesMarcados: int,
        tarjetasRojas: int,
        piernaHabil: str,
    ) -> None:
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, golesMarcados: int):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, tarjetasRojas: int):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, piernaHabil: str):
        self._piernaHabil = piernaHabil

    def __str__(self) -> str:
        nombre = self.getNombre()
        deporte = self.getDeporte()
        edad = self.getEdad()
        años = self.getAñosPracticando()
        return f"Mi nombre es {nombre} soy profesional en el deporte {deporte} Tengo {edad} años de edad y llevo {años} años en el deporte"
