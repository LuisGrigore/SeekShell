import typer
from models.api_key_model import ApiKeyModel


def show_key(key:ApiKeyModel) -> None:
    if not key:
        typer.echo("No key specified.")
        return
    typer.echo(f'key with alias "{key.alias}"="{key.key}"')

def show_set_key(key:ApiKeyModel) -> None:
    if not key:
        typer.echo("No key specified.")
        return
    typer.echo("Set:")
    show_key(key)

def show_remove_key(key:ApiKeyModel) -> None:
    if not key:
        typer.echo("No key specified.")
        return
    typer.echo("Removed:")
    show_key(key)