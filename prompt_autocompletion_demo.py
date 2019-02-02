from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

web_pocket_completer = WordCompleter([
    'use', 'set RHOST', 'run', 'exploit'
], ignore_case=True)

session = PromptSession(completer=web_pocket_completer)

while True:
    session.prompt('WebPocket> ')
