from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()  # Metadados das tabelas


# mapeando numa dataclass(classe de dados, sem atributos)
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    # O Mapped faz o sqA se virar nos tipos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_name: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    #Exercício aula 04
    updated_at: Mapped[datetime] = mapped_column(init=False, onupdate=func.now())
