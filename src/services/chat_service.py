from typing import Optional

from groq import Stream
from groq.types.chat import ChatCompletionChunk
from returns.result import Result, Success, Failure

from datasources import chat_datasource, deep_seek_datasource
from failures.chat_failures import ChatNotFoundFailure, DeepSeekNoResponseFailure
from models.chat_model import ChatModel
from models.message_model import MessageModel



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


def send_chat(chat:ChatModel) -> Result[Stream[ChatCompletionChunk],DeepSeekNoResponseFailure]:
    response:Stream[ChatCompletionChunk] = deep_seek_datasource.send_chat_stream(chat)
    return Success(response)