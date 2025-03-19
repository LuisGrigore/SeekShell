from app import app
from manage_result import manage_result
from services import api_key_service
from views.api_key_view import show_remove_key, show_set_key
from views.failure_view import show_fail


@app.command(name="set-api-key", help="Sets the api key to be used in all http requests.")
def set_current_api_key(key:str, alias:str) -> None:
    manage_result(api_key_service.set_current_api_key(key, alias), show_set_key, show_fail)

@app.command(name="remove-api-key", help="Removes current api key.")
def remove_current_api_key() -> None:
    manage_result(api_key_service.remove_current_api_key(), show_remove_key, show_fail)
