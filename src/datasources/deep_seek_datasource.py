from typing import Optional, List
import requests

from config.config import DEEP_SEEK_API_URL
from datasources import api_key_datasource, message_datasource
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


def send_chat(chat: ChatModel) -> Optional[str]:
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
        "content": "primero saludame como si fuera una celebrity y luego crea dos funciones en java que ordenen un array de formas distintas(usa markdown para formatear tu respuesta adecuadamente)"
      }
    ],

  })
    )
    return response.json()["choices"][0]["message"]["reasoning"]
