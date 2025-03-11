from groq import Groq, Stream
from groq.types.chat import ChatCompletionChunk

from datasources import api_key_datasource
from models.chat_model import ChatModel


def send_chat_stream(chat: ChatModel) -> Stream[ChatCompletionChunk]:
    client = Groq(api_key=api_key_datasource.get_current_key().key)

    stream:Stream[ChatCompletionChunk] = client.chat.completions.create(

        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": "\n".join([mssg.content for mssg in chat.messages]),
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=True,
    )
    return stream

