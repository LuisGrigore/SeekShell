from app import console
from models.message_model import MessageModel, SenderTypes


def _get_metadata_str(mssg:MessageModel):
    switch = {
        SenderTypes.USR: f"[bold magenta]({mssg.id})<You>[/bold magenta]",
        SenderTypes.BOT: f"[bold blue]({mssg.id})<SeekShell>[bold blue]"
    }
    return switch.get(mssg.sender_type)

def show_message(mssg:MessageModel) -> None:
    console.print(f"{_get_metadata_str(mssg)}: {mssg.content}")