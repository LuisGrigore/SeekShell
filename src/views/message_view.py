from app import console
from models.message_model import MessageModel, SenderTypes


def _get_sender_type_str(sender_type:SenderTypes):
    switch = {
        SenderTypes.USR: "You",
        SenderTypes.BOT: "SeekShell",
    }
    return switch.get(sender_type)

def show_message(mssg:MessageModel) -> None:
    console.print(f"[bold magenta]{_get_sender_type_str(mssg.sender_type)}:[/bold magenta] {mssg.content}")