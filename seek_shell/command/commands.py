from dataclasses import dataclass
from typing import Callable

from models.message_model import MessageModel


@dataclass
class DeleteMessage():
    message_id:int
    message_delete_funct:Callable[[int], MessageModel]
    def execute(self):
        self.message_delete_funct(self.message_id)
