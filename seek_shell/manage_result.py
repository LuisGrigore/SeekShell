from typing import TypeVar, Union, Callable, Optional

from returns.result import Result, Success, Failure

from views.failure_view import show_fail

R = TypeVar('R')
F = TypeVar('F')
SR = TypeVar('SR')
FR = TypeVar('FR')

ResultType = Union[SR, FR]

def manage_result(result:Result[R,F], on_success:Optional[Callable[[R],SR]] = None, on_fail:Callable[[F], FR] = show_fail) -> ResultType:
    match result:
        case Success(sr):
            if on_success:
                return on_success(sr)
            return None
        case Failure(fr):
            return on_fail(fr)
    return None