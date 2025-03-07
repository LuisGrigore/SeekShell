from returns.result import Result, Success

from datasources import message_datasource
from failures.message_failures import MessageCouldNotBeCreatedFailure
from models.message_model import MessageModel, SenderTypes


def create_message(content:str, sender_type:SenderTypes, chat_id:int) -> Result[MessageModel, MessageCouldNotBeCreatedFailure]:
    new_message:MessageModel = MessageModel(content=content, sender_type=sender_type, chat_id=chat_id)
    saved_message:MessageModel = message_datasource.save_message(new_message)
    if saved_message:
        return Success(saved_message)
