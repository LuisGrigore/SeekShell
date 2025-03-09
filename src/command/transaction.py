from dataclasses import dataclass
from typing import Protocol


@dataclass
class Transaction(Protocol):
    def execute(self):
        ...
    def undo(self):
        ...
    def redo(self):
        ...