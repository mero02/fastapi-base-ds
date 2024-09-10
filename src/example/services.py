from typing import List
from sqlalchemy.orm import Session
from src.example.models import Persona, Mascota, Vehiculo
from src.example import schemas, exceptions

# operaciones CRUD para Personas


def crear_persona(db: Session, persona: schemas.PersonaCreate) -> Persona:
    return Persona.create(db, nombre=persona.nombre, email=persona.email)


def listar_personas(db: Session) -> List[Persona]:
    return Persona.get_all(db)


def leer_persona(db: Session, persona_id: int) -> Persona:
    db_persona = Persona.get(db, persona_id)
    if db_persona is None:
        raise exceptions.PersonaNoEncontrada()
    return db_persona


def modificar_persona(
    db: Session, persona_id: int, persona: schemas.PersonaUpdate
) -> Persona:
    db_persona = leer_persona(db, persona_id)
    return db_persona.update(db, nombre=persona.nombre, email=persona.email)


def eliminar_persona(db: Session, persona_id: int) -> Persona:
    db_persona = leer_persona(db, persona_id)
    if len(db_persona.mascotas) > 0:
        raise exceptions.PersonaTieneMascotas()
    db_persona.delete(db)
    return db_persona


# operaciones CRUD para Mascota


def crear_mascota(db: Session, mascota: schemas.MascotaCreate) -> Mascota:
    return Mascota.create(db, nombre=mascota.nombre, tipo=mascota.tipo, tutor_id=mascota.tutor_id)



def listar_mascotas(db: Session) -> List[Mascota]:
    return Mascota.get_all(db)


def leer_mascota(db: Session, mascota_id: int) -> Mascota:
    db_mascota = Mascota.get(db, mascota_id)
    if db_mascota is None:
        raise exceptions.MascotaNoEncontrada()
    return db_mascota


def modificar_mascota(
    db: Session, mascota_id: int, mascota: schemas.MascotaUpdate
) -> Mascota:
    db_mascota = leer_mascota(db, mascota_id)
    return db_mascota.update(db, nombre=mascota.nombre, tipo=mascota.tipo)


def eliminar_mascota(db: Session, mascota_id: int) -> Mascota:
    db_mascota = leer_mascota(mascota_id)
    db_mascota.delete(db)
    return db_mascota

# operaciones CRUD para Vehiculo


def crear_vehiculo(db: Session, vehiculo: schemas.VehiculoCreate) -> Vehiculo:
    return Vehiculo.create(db, vehiculo)



def listar_vehiculos(db: Session) -> List[Vehiculo]:
    return Vehiculo.get_all(db)


def leer_vehiculo(db: Session, vehiculo_id: int) -> Vehiculo:
    db_vehiculo = Vehiculo.get(db, vehiculo_id)
    if db_vehiculo is None:
        raise exceptions.VehiculoNoEncontrada()
    return db_vehiculo


def modificar_vehiculo(
    db: Session, vehiculo_id: int, vehiculo: schemas.VehiculoUpdate
) -> Vehiculo:
    db_vehiculo = leer_vehiculo(db, vehiculo_id)
    return db_vehiculo.update(db, nombre=vehiculo.nombre, tipo=vehiculo.tipo)


def eliminar_vehiculo(db: Session, vehiculo_id: int) -> Vehiculo:
    db_vehiculo = leer_vehiculo(vehiculo_id)
    db_vehiculo.delete(db)
    return db_vehiculo