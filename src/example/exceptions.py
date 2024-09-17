from typing import List
from src.example.constants import ErrorCode
from src.exceptions import NotFound, BadRequest, PermissionDenied

# Excepciones para Persona
class PersonaNoEncontrada(NotFound):
    DETAIL = ErrorCode.PERSONA_NO_ENCONTRADA

class PersonaTieneMascotas(BadRequest):
    DETAIL = ErrorCode.PERSONA_TIENE_MASCOTAS

class PersonaTieneVehiculo(BadRequest):
    DETAIL = ErrorCode.PERSONA_TIENE_VEHICULO

# Excepciones para Mascota
class MascotaNoEncontrada(NotFound):
    DETAIL = ErrorCode.MASCOTA_NO_ENCONTRADA

class TipoMascotaInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]):
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.TIPO_MASCOTA_INVALIDO}: {posibles_tipos}."
        super().__init__(message)

# Excepciones para Vehiculo
class VehiculoNoEncontrada(NotFound):
    DETAIL = ErrorCode.VEHICULO_NO_ENCONTRADA

class TipoVehiculoInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]):
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.TIPO_VEHICULO_INVALIDO}: {posibles_tipos}."
        super().__init__(message)

# Excepciones para Paseo
class PaseoNoEncontrado(NotFound):
    DETAIL = ErrorCode.PASEO_NO_ENCONTRADO

class PaseoTieneMascotas(BadRequest):
    DETAIL = ErrorCode.PASEO_TIENE_MASCOTAS