from typing import List

import typer
from returns.result import Result, Success, Failure

from app import app
from failures.failurebase import FailureBase
from models.chat_model import ChatModel
from services import chat_service
from views.chat_view import show_chat, show_chat_str_input
from views.failure_view import show_fail

def _command_factory(command_str:str) -> bool:
    if command_str == "::close::":
        return True
    return False

def _process_command(exit:List[bool], command_str:str) -> None:
    if command_str == "::close::":
        exit[0] = True
    else:
        pass

def _command_loop() -> None:
    exit:List[bool] = [False]
    while not exit[0]:
        _process_command(exit, show_chat_str_input())

def _process_result(result:Result[ChatModel, FailureBase]) -> None:
    match result:
        case Success(chat):
            show_chat(chat)
            _command_loop()
        case Failure(error):
            show_fail(error)



@app.command(name="open-chat", help="Opens chat based on id.")
def open_chat(id:int = typer.Argument(None, help="If blank, opens latest chat.")) -> None:
    current_chat:Result[ChatModel, FailureBase]
    if not id:
        current_chat = chat_service.get_latest_chat()
    else:
        current_chat = chat_service.get_chat_by_id(id)
    _process_result(current_chat)