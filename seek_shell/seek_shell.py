from app import app
from db import Base, engine



if __name__ == '__main__':
    #Setsup db
    from models import api_key_model, message_model, chat_model
    Base.metadata.create_all(engine)
    #Starts app
    from controllers import api_key_controller, manage_chats_controller, chat_controller
    app()
