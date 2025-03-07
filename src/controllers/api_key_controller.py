from returns.result import Result, Success, Failure, Callable

from app import app
from failures.api_key_failures import ApiKeyCouldNotBeSetFailure, ApiKeyCouldNotBeRemovedFailure
from failures.failurebase import FailureBase
from models.api_key_model import ApiKeyModel
from services import api_key_service
from views.api_key_view import show_remove_key, show_set_key
from views.failure_view import show_fail

def _manage_result(result:Result[ApiKeyModel,FailureBase], on_success:Callable[[ApiKeyModel],None], on_fail:Callable[[FailureBase],None]) -> None:
    match result:
        case Success(api_key):
            on_success(api_key)
        case Failure(error):
            on_fail(error)

@app.command(name="set-api-key", help="Sets the api key to be used in all http requests.")
def set_current_api_key(key:str, alias:str) -> None:
    result: Result[ApiKeyModel, ApiKeyCouldNotBeSetFailure] = api_key_service.set_current_api_key(key, alias)
    _manage_result(result, show_set_key, show_fail)

@app.command(name="remove-api-key", help="Removes current api key.")
def remove_current_api_key() -> None:
    result:Result[ApiKeyModel, ApiKeyCouldNotBeRemovedFailure] = api_key_service.remove_current_api_key()
    _manage_result(result, show_remove_key, show_fail)
