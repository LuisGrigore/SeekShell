from dataclasses import dataclass
from typing import Optional
import typer
from app import app
from manage_result import manage_result
from models.chat_model import ChatModel
from models.message_model import SenderTypes
from services import chat_service, message_service
from views.chat_view import show_chat, show_chat_str_input
from views.message_view import show_message


@dataclass
class ChatController:
    current_chat:Optional[ChatModel] = None

    def _command_loop(self):

        while(True):
            usr_input:str = show_chat_str_input()
            if usr_input == ":q":
                break
            manage_result(message_service.create_message(usr_input, SenderTypes.USR, self.current_chat.id),
                          lambda mssg: show_message(mssg))
            manage_result(chat_service.send_chat(self.current_chat),
                          lambda mssg: show_message(mssg))


    def _on_chat_success(self, chat:ChatModel) -> None:
        self.current_chat = chat
        show_chat(chat)
        self._command_loop()

    def open_latest_chat(self) -> None:
        manage_result(chat_service.get_latest_chat(), self._on_chat_success)

    def open_chat_by_id(self, id:int):
        manage_result(chat_service.get_chat_by_id(id), self._on_chat_success)



@app.command(name="open-chat", help="Opens chat based on id (if no id provided, opens latest chat).")
def open_chat(id:int = typer.Argument(None, help="If blank, opens latest chat.")) -> None:
    chat_controller:ChatController = ChatController()
    if id:
        chat_controller.open_chat_by_id(id)
    chat_controller.open_latest_chat()