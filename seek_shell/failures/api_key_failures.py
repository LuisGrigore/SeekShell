from failures.failurebase import FailureBase


class ApiKeyCouldNotBeSetFailure(FailureBase):
    def __init__(self):
        super().__init__("Api key could not be set.")


class ApiKeyCouldNotBeRemovedFailure(FailureBase):
    def __init__(self):
        super().__init__("Api key could not be removed.")