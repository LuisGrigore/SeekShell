from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime, func
from sqlalchemy.orm import relationship

from db import Base
from models.message_model import MessageModel


class ChatModel(Base):
    __tablename__ = 'chats'

    id:int = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name:str = Column(String, nullable=False)
    description:str = Column(String, nullable=True)
    timestamp:datetime = Column(DateTime, default=func.now())
    last_opened:datetime = Column(DateTime, nullable=True)
    messages = relationship(MessageModel, backref='chat', cascade="all, delete-orphan")