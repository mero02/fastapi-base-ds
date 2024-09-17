class ErrorCode:
    # Errores relacionados con Persona
    PERSONA_NO_ENCONTRADA = "La persona no fue encontrada."
    PERSONA_TIENE_MASCOTAS = "La persona tiene mascotas a cargo. No puede ser eliminada."
    PERSONA_TIENE_VEHICULO = "La persona tiene vehículos a cargo. No puede ser eliminada."

    # Errores relacionados con Mascota
    MASCOTA_NO_ENCONTRADA = "La mascota no fue encontrada."
    TIPO_MASCOTA_INVALIDO = "El tipo de mascota indicado es inválido. El valor indicado debiera ser una de las opciones en la lista:"

    # Errores relacionados con Vehículo
    VEHICULO_NO_ENCONTRADA = "El vehículo no fue encontrado."
    TIPO_VEHICULO_INVALIDO = "El tipo de vehículo indicado es inválido. El valor indicado debiera ser una de las opciones en la lista:"

    # Errores relacionados con Paseo
    PASEO_NO_ENCONTRADO = "El paseo no fue encontrado."
    PASEO_TIENE_MASCOTAS = "El paseo tiene mascotas asignadas. No puede ser eliminado."

    # Errores generales
    EMAIL_DUPLICADO = "El email ya existe."
    NOMBRE_DUPLICADO = "El nombre ya existe."