from app import console
from models.message_model import MessageModel, SenderTypes
from rich.syntax import Syntax
from rich.panel import Panel
import re



def _get_metadata_str(mssg:MessageModel):
    switch = {
        SenderTypes.USR: f"[bold magenta]({mssg.id})<You>[/bold magenta]",
        SenderTypes.BOT: f"[bold blue]({mssg.id})<SeekShell>[bold blue]"
    }
    return switch.get(mssg.sender_type)

def show_message(mssg:MessageModel) -> None:
    console.print(f"{_get_metadata_str(mssg)}: {mssg.content}")

def show_message_md(mssg: MessageModel) -> None:
    console.print(f"{_get_metadata_str(mssg)}:")
    _print_markdown_response(mssg.content)

def _print_markdown_response(markdown_text: str):
    code_blocks = re.findall(r'```(.*?)\n(.*?)```', markdown_text, re.DOTALL)

    plain_text = re.sub(r'```(.*?)\n(.*?)```', '', markdown_text, flags=re.DOTALL)
    console.print(plain_text)  # Texto normal

    for lang, code in code_blocks:
        language = lang.strip() if lang else "text"  # Si no hay lenguaje, usar 'text'

        # Creamos el bloque de código con syntax para resaltar los colores según el lenguaje
        syntax = Syntax(code.strip(), language)

        # Creamos el panel con borde y esquinas redondeadas, sin limitar el ancho
        panel = Panel(syntax, title=language.capitalize(), border_style="white", padding=(1, 2), expand=True)

        # Imprimir el panel con el código resaltado
        console.print(panel)