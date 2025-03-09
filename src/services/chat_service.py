from returns.result import Result, Success, Failure

from datasources import chat_datasource
from failures.chat_failures import ChatNotFoundFailure
from models.chat_model import ChatModel


def get_latest_chat() -> Result[ChatModel, ChatNotFoundFailure]:
    chat:ChatModel = chat_datasource.get_latest()
    if chat:
        chat_datasource.update_last_opened(chat)
        return Success(chat)
    return Failure(ChatNotFoundFailure())

def get_chat_by_id(id:int) -> Result[ChatModel, ChatNotFoundFailure]:
    chat: ChatModel = chat_datasource.get_by_id(id)
    if chat:
        chat_datasource.update_last_opened(chat)
        return Success(chat)
    return Failure(ChatNotFoundFailure(id=id))


def send_chat(current_chat):
    return None