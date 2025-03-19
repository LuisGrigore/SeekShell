from failures.failurebase import FailureBase

class MessageCouldNotBeCreatedFailure(FailureBase):
    def __init__(self):
        super().__init__("Message could not be created.")