from abc import ABC, abstractmethod
from errores import LongitudClaveError, MayusculaClaveError, MinusculaClaveError, NumeroClaveError, CaracterEspecialError, CalistoClaveError

class ReglaValidacion(ABC, _longitud_esperada: int):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(clave: str)-> bool:
        pass
    def _validar_longitud(clave: str) -> bool:
        if len(clave) < self._longitud_esperada:
            raise LongitudClaveError()

    def _contiene_mayuscula(clave: str)-> bool:
        if not any(char.isupper() for char in clave):
            raise MayusculaClaveError()

    def _contiene_minuscula(clave: str)-> bool:
        if not any(char.islower() for char in clave):
            raise MinusculaClaveError()

    def _contiene_numero(clave: str)-> bool:
        if not any(char.isdigit() for char in clave):
            raise NumeroClaveError()


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):

    def contiene_caracter_especial(self, clave: str)-> bool:
        if not any(char in '@_#$%' for char in clave):
            raise CaracterEspecialError()

    def es_valida(self, clave: str)-> bool:
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
    def contiene_calisto(self, clave: str)-> bool:
        if clave.find('calisto') == -1:
            raise CalistoClaveError()

    def es_valida(self, clave: str)-> bool:
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str)-> bool:
        return self.regla.es_valida(clave)
