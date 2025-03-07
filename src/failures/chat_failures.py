from typing import Optional

from config.config import MAX_DESCRIPTION_LEN, MAX_NAME_LEN
from failures.failurebase import FailureBase


class NoChatsFoundFailure(FailureBase):
    def __init__(self):
        super().__init__("No chats found.")

class ChatCouldNotBeCreatedFailure(FailureBase):
    def __init__(self):
        super().__init__("Chat could not be created.")

class ChatCouldNotBeRemovedFailure(FailureBase):
    def __init__(self):
        super().__init__("Chat could not be removed.")

class ChatDescriptionTooLongFailure(FailureBase):
    def __init__(self):
        super().__init__(f"Description needs to be {MAX_DESCRIPTION_LEN} chars or less.")

class ChatNameTooLongFailure(FailureBase):
    def __init__(self):
        super().__init__(f"Name needs to be {MAX_NAME_LEN} chars or less.")

class ChatNotFoundFailure(FailureBase):
    def __init__(self, id:Optional[int] = None):
        if id:
            super().__init__(f"Chat with id {id} not found.")
        else:
            super().__init__(f"Chat not found.")