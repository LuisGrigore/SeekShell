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
                "content": "You are a helpful assistant. Make sure to end all your messages with a new line. You will format your response in markdown format, use ir to be as legible and clear as possible, remember that you can use colors and make your text bold if needed. You will use emojis and any other visual aid on hand to be as clear as posible."
            },
            {
                "role": "user",
                "content": "\n".join([mssg.content for mssg in chat.messages]),
            }
        ],
        model="deepseek-r1-distill-llama-70b",
        temperature=0.5,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=True,
    )
    return stream

