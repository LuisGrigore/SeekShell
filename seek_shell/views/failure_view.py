from app import console
from failures.failurebase import FailureBase


def show_fail(fail:FailureBase) -> None:
    console.print(fail.message)