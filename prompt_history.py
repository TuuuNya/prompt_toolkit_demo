from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory

session = PromptSession(history=FileHistory('./prompt_history.log'))

while True:
    session.prompt()
