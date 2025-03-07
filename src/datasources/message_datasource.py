from typing import Optional

from db import session
from models.message_model import MessageModel


def save_message(message:MessageModel) -> Optional[MessageModel]:
    try:
        session.add(message)
        session.commit()
        return message
    except:
        return None