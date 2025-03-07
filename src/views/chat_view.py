from typing import List

import typer

from app import console
from models.chat_model import ChatModel
from rich.table import Table

def show_chat(chat:ChatModel) -> None:
    table: Table = Table(show_header=True, header_style="bold")
    table.add_column("Id", justify="center")
    table.add_column("Name", justify="center")
    table.add_column("Description", justify="center")
    table.add_column("Creation_date", justify="center")

    table.add_row(str(chat.id), chat.name,
                            chat.description if chat.description is not None else "EMPTY",
                            chat.timestamp.strftime("%Y-%m-%d %H:%M:%S"))

    console.print(table)


def show_chats(chat_list:List[ChatModel]) -> None:
    table:Table = Table(show_header=True,header_style="bold")
    table.add_column("Id", justify="center")
    table.add_column("Name", justify="center")
    table.add_column("Description", justify="center")
    table.add_column("Creation_date", justify="center")

    list(map(lambda chat: table.add_row(str(chat.id), chat.name, chat.description if chat.description is not None else "EMPTY", chat.timestamp.strftime("%Y-%m-%d %H:%M:%S")), chat_list))

    console.print(table)

def show_chat_remove(chat:ChatModel) -> None:
    typer.echo("Removed:")
    typer.echo(f"Chat {chat.name} with id {chat.id}")

def show_chat_str_input() -> str:
    res:str = input("Speek your mind: ")
    print("\033[F\033[K", end="")
    return res