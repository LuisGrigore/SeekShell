from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func

from db import Base


class ApiKeyModel(Base):
    __tablename__ = 'api_key'

    id:int = Column(Integer, primary_key=True, default=1)
    key:str = Column(String, nullable=False)
    timestamp:datetime = Column(DateTime, default=func.now())
    alias:str = Column(String, nullable=False)