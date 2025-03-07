from typing import List

from returns.result import Result, Failure, Success

from config.config import MAX_NAME_LEN, MAX_DESCRIPTION_LEN
from datasources import chat_datasource
from failures.chat_failures import NoChatsFoundFailure, ChatCouldNotBeCreatedFailure, ChatCouldNotBeRemovedFailure, \
    ChatNameTooLongFailure, ChatDescriptionTooLongFailure
from models.chat_model import ChatModel


def get_all_chats() -> Result[List[ChatModel], NoChatsFoundFailure]:
    chat_list:List[ChatModel] = chat_datasource.get_all_chats()
    return Success(chat_list)


def create_chat(name:str, description:str = None) -> Result[ChatModel, ChatCouldNotBeCreatedFailure]:
    if len(name) > MAX_NAME_LEN : return Failure(ChatNameTooLongFailure())
    if description and len(description) > MAX_DESCRIPTION_LEN : return Failure(ChatDescriptionTooLongFailure())

    new_chat:ChatModel = ChatModel(name=name, description=description)
    saved_chat:ChatModel = chat_datasource.save_chat(new_chat)

    if saved_chat:
        return Success(saved_chat)
    return Failure(ChatCouldNotBeCreatedFailure())


def remove_chat(id:int) -> Result[ChatModel, ChatCouldNotBeRemovedFailure]:
    selected_chat:ChatModel = chat_datasource.remove(id)
    if selected_chat:
        return Success(selected_chat)
    return Failure(ChatCouldNotBeRemovedFailure())
