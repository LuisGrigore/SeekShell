from returns.result import Result, Failure, Success

from datasources import api_key_datasource
from failures.api_key_failures import ApiKeyCouldNotBeSetFailure, ApiKeyCouldNotBeRemovedFailure
from models.api_key_model import ApiKeyModel


def set_current_api_key(key:str, alias:str) -> Result[ApiKeyModel,ApiKeyCouldNotBeSetFailure]:
    new_key:ApiKeyModel = ApiKeyModel(key=key, alias=alias)
    current_key = api_key_datasource.set_current_api_key(new_key)
    if current_key:
        return Success(current_key)
    return Failure(ApiKeyCouldNotBeSetFailure())

def remove_current_api_key() -> Result[ApiKeyModel,ApiKeyCouldNotBeRemovedFailure]:
    removed_key:ApiKeyModel = api_key_datasource.remove_current_api_key()
    if removed_key:
        return Success(removed_key)
    return Failure(ApiKeyCouldNotBeRemovedFailure())