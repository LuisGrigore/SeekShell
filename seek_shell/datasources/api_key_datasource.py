from db import session
from models.api_key_model import ApiKeyModel


def set_current_api_key(key:ApiKeyModel) -> ApiKeyModel:
    current_key:ApiKeyModel = session.query(ApiKeyModel).first()
    if current_key:
        session.delete(current_key)
        session.commit()
    session.add(key)
    session.commit()
    new_key:ApiKeyModel = session.query(ApiKeyModel).first()
    return new_key

def remove_current_api_key() -> ApiKeyModel:
    current_key: ApiKeyModel = session.query(ApiKeyModel).first()
    if current_key:
        session.delete(current_key)
        session.commit()
    return current_key

def get_current_key() -> ApiKeyModel:
    return session.query(ApiKeyModel).first()
