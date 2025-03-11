from dataclasses import dataclass
from typing import Optional
import typer
from groq import Stream
from groq.types.chat import ChatCompletionChunk

from app import app
from manage_result import manage_result
from models.chat_model import ChatModel
from models.message_model import SenderTypes, MessageModel
from services import chat_service, message_service
from views.chat_view import show_chat, show_chat_str_input
from views.message_view import show_message, MarkdownPrinter
from views.symbols_view import show_thinking


@dataclass
class ChatController:
    current_chat:Optional[ChatModel] = None

    def _command_loop(self):
        def on_response_success(stream: Stream[ChatCompletionChunk]):
            show_thinking()
            def on_message_create(mssg: MessageModel) -> MessageModel:
                show_message(mssg)
                return mssg

            mssg: MessageModel = manage_result(
                message_service.create_message('', SenderTypes.BOT, self.current_chat.id),
                on_message_create
            )

            printer = MarkdownPrinter()
            line_buffer = []
            message_buffer = []
            inside_think_tag = False

            for chunk in stream:
                string = chunk.choices[0].delta.content
                if string:
                    for char in string:
                        line_buffer.append(char)
                        current_line = ''.join(line_buffer)

                        if "<think>" in current_line:
                            inside_think_tag = True
                            line_buffer.clear()
                            show_thinking()
                            continue

                        if "</think>" in current_line:
                            inside_think_tag = False
                            line_buffer.clear()
                            continue

                        if not inside_think_tag:
                            if char == '\n':
                                printer.print_markdown_line(current_line)
                                message_buffer.append(current_line)
                                line_buffer.clear()

            if line_buffer:
                final_line = ''.join(line_buffer)
                printer.print_markdown_line(final_line)
                message_buffer.append(final_line)

            mssg.content = ''.join(message_buffer)
            manage_result(message_service.update_message(mssg))

        while(True):
            usr_input:str = show_chat_str_input()
            if usr_input == ":q":
                break
            manage_result(message_service.create_message(usr_input, SenderTypes.USR, self.current_chat.id),
                          lambda mssg: show_message(mssg))
            show_thinking()
            manage_result(chat_service.send_chat(self.current_chat), on_response_success)

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
        return
    chat_controller.open_latest_chat()