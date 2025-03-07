from typing import List, Optional
import typer
from returns.result import Result, Failure, Success
from app import app
from failures.failurebase import FailureBase
from models.chat_model import ChatModel
from services import manage_chat_service
from views import chat_view
from views.chat_view import show_chat_remove
from views.failure_view import show_fail



@app.command(name="list-chats", help="Shows a table containing all availible chats.")
def list_chats() -> None:
    result:Result[List[ChatModel],FailureBase] = manage_chat_service.get_all_chats()
    match result:
        case Success(chat_list):
            chat_view.show_chats(chat_list)


@app.command(name="create-chat", help="Creates a new chat with the specified name and description.")
def create_chat(name:str = typer.Argument(help="Name of the chat."), description: Optional[str] = typer.Option(None, help="Description of the chat (Should be between 1 and 200 chars).")) -> None:
    result: Result[ChatModel, FailureBase] = manage_chat_service.create_chat(name, description)
    match result:
        case Success():
            list_chats()
        case Failure(error):
            show_fail(error)

@app.command(name="remove-chat", help="Removes a chat based on id.")
def remove_chat(id:int = typer.Argument(help="Id of the chat to remove.")) -> None:
    result:Result[ChatModel,FailureBase] = manage_chat_service.remove_chat(id)
    match result:
        case Success(chat):
            show_chat_remove(chat)
            list_chats()
        case Failure(error):
            show_fail(error)