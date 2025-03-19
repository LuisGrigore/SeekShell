from app import console
from models.message_model import MessageModel, SenderTypes
from rich.syntax import Syntax
from rich.panel import Panel
import re

def _get_metadata_str(mssg:MessageModel):
    switch = {
        SenderTypes.USR: f"[bold magenta]({mssg.id})<You>[/bold magenta]",
        SenderTypes.BOT: f"[bold blue]({mssg.id})<SeekShell>[bold blue]"
    }
    return switch.get(mssg.sender_type)

def show_message(mssg:MessageModel) -> None:
    console.print(f"{_get_metadata_str(mssg)}: {mssg.content}")

def show_message_md(mssg: MessageModel) -> None:
    console.print(f"{_get_metadata_str(mssg)}:")
    MarkdownPrinter.print_markdown_response(mssg.content)


class MarkdownPrinter:
    def __init__(self):
        self.console = console
        self.inside_code_block = False
        self.code_lines = []
        self.language = "text"

    def print_markdown_line(self, line: str):
        line = line.rstrip()
        if line.startswith("```"):
            if self.inside_code_block:
                syntax = Syntax("\n".join(self.code_lines), self.language, theme="monokai", line_numbers=True)
                panel = Panel(syntax, title=self.language.capitalize(), border_style="white", padding=(1, 2), expand=True)
                self.console.print(panel)

                self.inside_code_block = False
                self.code_lines = []
            else:
                self.inside_code_block = True
                self.language = line[3:].strip() or "text"
        elif self.inside_code_block:
            self.code_lines.append(line)
        else:
            self.console.print(line)

    @staticmethod
    def print_markdown_response(markdown_text: str):
        code_blocks = re.findall(r'```(.*?)\n(.*?)```', markdown_text, re.DOTALL)

        plain_text = re.sub(r'```(.*?)\n(.*?)```', '', markdown_text, flags=re.DOTALL)
        console.print(plain_text)  # Texto normal

        for lang, code in code_blocks:
            language = lang.strip() if lang else "text"  # Si no hay lenguaje, usar 'text'
            syntax = Syntax(code.strip(), language)
            panel = Panel(syntax, title=language.capitalize(), border_style="white", padding=(1, 2), expand=True)
            console.print(panel)