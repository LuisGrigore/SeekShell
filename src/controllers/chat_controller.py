from typing import List, Optional, Callable
import typer
from returns.result import Result, Success, Failure
from app import app
from failures.failurebase import FailureBase
from models.chat_model import ChatModel
from models.message_model import MessageModel, SenderTypes
from services import chat_service, message_service
from views.chat_view import show_chat, show_chat_str_input
from views.failure_view import show_fail
from views.message_view import show_message

current_chat:Optional[ChatModel] = None

def _update_current_chat() -> None:
    updated_current_chat:Result[ChatModel, FailureBase] = chat_service.get_latest_chat()
    if _process_result(updated_current_chat):
        global current_chat
        current_chat = updated_current_chat.unwrap()


def _process_result(result, on_success:Optional[Callable[[ChatModel], None]] = None, on_fail:Optional[Callable[[FailureBase], None]] = show_fail) -> bool:
    match result:
        case Success(chat):
            if on_success:
                on_success(chat)
            return True
        case Failure(error):
            if on_fail:
                on_fail(error)
            return False
    return False

def _command_factory(command_str:str) -> bool:
    if command_str == "::close::":
        return True
    return False


def _command_loop() -> None:
    while (True):
        urs_input = show_chat_str_input()
        if urs_input == "::close::" : break
        message_result:Result[MessageModel, FailureBase] = message_service.create_message(urs_input,SenderTypes.USR,current_chat.id)
        if _process_result(message_result):
            _update_current_chat()
            show_message(message_result.unwrap())
            #chat_service.send_chat(current_chat)



def get_current_chat(id:Optional[int]) -> Result[ChatModel, FailureBase]:
    if not id:
        return chat_service.get_latest_chat()
    else:
        return chat_service.get_chat_by_id(id)


@app.command(name="open-chat", help="Opens chat based on id.")
def open_chat(id:int = typer.Argument(None, help="If blank, opens latest chat.")) -> None:
    chat_result:Result[ChatModel, FailureBase] = get_current_chat(id)

    if _process_result(chat_result):
        show_chat(chat_result.unwrap())
        global current_chat
        current_chat = chat_result.unwrap()
        _command_loop()