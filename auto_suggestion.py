from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory


session = PromptSession()

while True:
    text = session.prompt('> ', auto_suggest=AutoSuggestFromHistory())
    print('You said: {}'.format(text))

