from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID  # Импортируем UUID
from sqlalchemy.orm import relationship
import uuid  # Для генерации UUID

from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    api_token = Column(String, unique=True)
    token_bot = Column(String)
    is_active = Column(Boolean, default=False)

class Tasks(Base):
    __tablename__='tasks'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Используйте UUID
    name = Column(String)
    description = Column(String)
    data_start = Column(String)
    data_end = Column(String)

class BeenCloseTasks(Base):
    __tablename__ = 'closed_tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)  
