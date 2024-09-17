from typing import Optional, List
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import auto, StrEnum
from datetime import datetime, UTC
from src.models import BaseModel

class Persona(BaseModel):
    __tablename__ = "personas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
    mascotas: Mapped[Optional[List["Mascota"]]] = relationship(
        "Mascota", back_populates="tutor"
    )
    vehiculos: Mapped[Optional[List["Vehiculo"]]] = relationship(
        "Vehiculo", back_populates="duenio"
    )

class TipoMascota(StrEnum):
    GATO = auto()
    PERRO = auto()
    CONEJO = auto()
    COBAYO = auto()
    PEZ = auto()

class Mascota(BaseModel):
    __tablename__ = "mascotas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    tipo: Mapped[TipoMascota] = mapped_column(String)  # e.g., "Gato", "Perro", etc.
    tutor_id: Mapped[int] = mapped_column(
        ForeignKey("personas.id")
    )  # Foreign key a Persona
    tutor: Mapped[Persona] = relationship("Persona", back_populates="mascotas")
    paseos: Mapped[Optional[List["Paseo"]]] = relationship(
        "Paseo", secondary="paseos_mascotas_vehiculos", back_populates="mascotas"
    )
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    @property
    def nombre_tutor(self):
        return self.tutor.nombre

class TipoVehiculo(StrEnum):
    AUTO = auto()
    CAMION = auto()
    CAMIONETA = auto()

class Vehiculo(BaseModel):
    __tablename__ = "vehiculos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    marca: Mapped[str] = mapped_column(String, index=True)
    tipo: Mapped[TipoVehiculo] = mapped_column(String) 
    duenio_id: Mapped[int] = mapped_column(
        ForeignKey("personas.id")
    )  # Foreign key a Persona
    duenio: Mapped[Persona] = relationship("Persona", back_populates="vehiculos")
    paseos: Mapped[Optional[List["Paseo"]]] = relationship(
        "Paseo", secondary="paseos_mascotas_vehiculos", back_populates="vehiculos"
    )
    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    @property
    def nombre_duenio(self):
        return self.duenio.nombre

# Tabla intermedia para la relación muchos a muchos entre Paseo, Mascota y Vehiculo
paseos_mascotas_vehiculos = Table(
    "paseos_mascotas_vehiculos", BaseModel.metadata,
    Column("paseo_id", ForeignKey("paseos.id"), primary_key=True),
    Column("mascota_id", ForeignKey("mascotas.id"), primary_key=True),
    Column("vehiculo_id", ForeignKey("vehiculos.id"), primary_key=True)
)

class Paseo(BaseModel):
    __tablename__ = "paseos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    #fecha_paseo: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    mascota_id = Column(Integer, ForeignKey('mascotas.id'), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'), nullable=False)
    # Relaciones con Mascota y Vehiculo
    mascotas: Mapped[Optional[List["Mascota"]]] = relationship(
        "Mascota", secondary="paseos_mascotas_vehiculos", back_populates="paseos"
    )
    vehiculos: Mapped[Optional[List["Vehiculo"]]] = relationship(
        "Vehiculo", secondary="paseos_mascotas_vehiculos", back_populates="paseos"
    )

    fecha_creacion: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))
    fecha_modificacion: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )
    
