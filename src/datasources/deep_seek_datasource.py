from typing import Optional, List
import requests
from rich.panel import Panel

from config.config import DEEP_SEEK_API_URL
from datasources import api_key_datasource
from models.chat_model import ChatModel
import json
from models.message_model import SenderTypes, MessageModel


def _map_sneder_type(sender_type:SenderTypes) -> Optional[str]:
    match sender_type:
        case SenderTypes.USR:
            return "user"
        case SenderTypes.BOT:
            return "assistant"
    return None

def _serialize_messages(mssgs:List[MessageModel]) -> str:
    a = "[{role:user,content:"
    b = "}]"
    return f"{a}{mssgs[0].content}{b}"

def _serialize_chat(chat:ChatModel) -> str:
    return json.dumps({
        "model": "deepseek/deepseek-r1-zero:free",
        "messages": _serialize_messages(chat.messages)
    })



from rich.console import Console
from rich.syntax import Syntax
import re

# Crear una instancia de la consola para imprimir
console = Console()

# Definir una función para imprimir el contenido en markdown
def print_markdown_response(markdown_text: str):
    """
    Imprime una respuesta en markdown de la manera más legible posible.
    También maneja los bloques de código y los resalta según el lenguaje,
    dentro de un panel con borde y esquinas redondeadas.
    """

    # Buscar bloques de código en el texto markdown
    code_blocks = re.findall(r'```(.*?)\n(.*?)```', markdown_text, re.DOTALL)

    # Imprimir texto normal
    plain_text = re.sub(r'```(.*?)\n(.*?)```', '', markdown_text, flags=re.DOTALL)
    console.print(plain_text)  # Texto normal

    # Imprimir los bloques de código con borde redondeado
    for lang, code in code_blocks:
        language = lang.strip() if lang else "text"  # Si no hay lenguaje, usar 'text'

        # Creamos el bloque de código con syntax para resaltar los colores según el lenguaje
        syntax = Syntax(code.strip(), language)

        # Creamos el panel con borde y esquinas redondeadas, sin limitar el ancho
        panel = Panel(syntax, title=language.capitalize(), border_style="white", padding=(1, 2), expand=True)

        # Imprimir el panel con el código resaltado
        console.print(panel)



def send_chat(chat: ChatModel) -> MessageModel:
    print(_serialize_chat(chat))
    response = requests.post(
        url=DEEP_SEEK_API_URL,
        headers={
            "Authorization": f"Bearer {api_key_datasource.get_current_key().key}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
    "model": "deepseek/deepseek-r1-zero:free",
    "messages": [
      {
        "role": "user",
        "content": "crea dos funciones en java que ordenen un array de formas distintas(usa markdown para formatear tu respuesta adecuadamente)"
      }
    ],

  })
    )
    print_markdown_response(response.json()["choices"][0]["message"]["reasoning"])
