
from sqlalchemy import Column, Integer, String
from database import Base


class EquipmentDB(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False)


class IncidentDB(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    status = Column(String, nullable=False)
    equipment_id = Column(Integer, nullable=False)


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)
