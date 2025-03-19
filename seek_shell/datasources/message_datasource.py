from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

from db import session
from models.message_model import MessageModel


def save_message(message:MessageModel) -> Optional[MessageModel]:
    try:
        session.add(message)
        session.commit()
        return message
    except:
        return None

def update_message(mssg:MessageModel) -> Optional[MessageModel]:
    try:
        session.merge(mssg)
        session.commit()
        return mssg
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al actualizar entidad: {e}")
        return None

