from typing import Optional
import typer
from app import app
from manage_result import manage_result
from services import manage_chat_service
from views import chat_view
from views.chat_view import show_chat_remove



@app.command(name="list-chats", help="Shows a table containing all availible chats.")
def list_chats() -> None:
    manage_result(manage_chat_service.get_all_chats(), chat_view.show_chats)

@app.command(name="create-chat", help="Creates a new chat with the specified name and description.")
def create_chat(name:str = typer.Argument(help="Name of the chat."), description: Optional[str] = typer.Option(None, help="Description of the chat (Should be between 1 and 200 chars).")) -> None:
    manage_result(manage_chat_service.create_chat(name, description))
    list_chats()

@app.command(name="remove-chat", help="Removes a chat based on id.")
def remove_chat(id:int = typer.Argument(help="Id of the chat to remove.")) -> None:
    manage_result(manage_chat_service.remove_chat(id), show_chat_remove)
    list_chats()
