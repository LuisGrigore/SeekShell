import enum
from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Enum, String

from db import Base


class SenderTypes(enum.Enum):
    USR = 1
    BOT = 2

class MessageModel(Base):
    __tablename__ = 'messages'

    id:int = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    timestamp:datetime = Column(DateTime, default=func.now())
    sender_type = Column(Enum(SenderTypes), nullable=False)
    content:str = Column(String, nullable=False)
    chat_id:int = Column(Integer, ForeignKey('chats.id'))

