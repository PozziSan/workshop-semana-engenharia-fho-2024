from __future__ import annotations

from sqlalchemy import Column, DateTime, Integer

from datetime import datetime, timezone

from database import SessionLocal, Base

from typing import Type


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    deleted_at = Column(DateTime, default=datetime.now(timezone.utc))

    @classmethod
    def _get_primary_key(cls) -> Column:
        return cls.__mapper__.primary_key[0]

    @classmethod
    def all(cls, session_maker=SessionLocal) -> list[Type[BaseModel]]:
        with session_maker() as session:
            return session.query(cls).all()

    @classmethod
    def get_by_id(cls, _id: int, session_maker=SessionLocal) -> Type[BaseModel] | None:
        with session_maker() as session:
            primary_key = cls._get_primary_key()
            return session.query(cls).filter(primary_key == _id).one()

    @classmethod
    def first(cls, session_maker=SessionLocal) -> Type[BaseModel] | None:
        with session_maker() as session:
            return session.query(cls).first()

    @classmethod
    def create(cls, session_maker=SessionLocal, **kwargs) -> Type[BaseModel]:
        instance = cls(**kwargs)

        with session_maker() as session:
            session.add(instance)
            session.commit()
            session.refresh(instance)

            return instance

    def update(self, session_maker=SessionLocal, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

        with session_maker() as session:
            session.add(self)
            session.commit()

    def delete(self, session_maker=SessionLocal) -> None:
        with session_maker() as session:
            session.delete(self)
            session.commit()
