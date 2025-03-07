from datetime import datetime
from typing import List, Optional

from sqlalchemy import desc

from db import session
from models.chat_model import ChatModel


def get_all_chats() -> List[ChatModel]:
    chat_list: List[ChatModel] = session.query(ChatModel).all()
    return chat_list


def save_chat(new_chat:ChatModel) -> Optional[ChatModel]:
    session.add(new_chat)
    try:
        session.commit()
        return new_chat
    except Exception as e:
        return None


def get_by_id(id:int) -> Optional[ChatModel]:
    chat:ChatModel = session.query(ChatModel).get(id)
    return chat


def remove(id:int) -> Optional[ChatModel]:
    chat:ChatModel = get_by_id(id)
    if chat:
        session.delete(chat)
        session.commit()
        return chat
    return None


def get_latest() -> Optional[ChatModel]:
    return session.query(ChatModel).order_by(desc(ChatModel.last_opened)).first()


def update_last_opened(chat:ChatModel) -> Optional[ChatModel]:
    found_chat:ChatModel = session.query(ChatModel).get(chat.id)
    if not found_chat:
        return None
    found_chat.last_opened = datetime.now()
    session.commit()
    return found_chat