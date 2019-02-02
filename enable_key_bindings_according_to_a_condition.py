import datetime
from prompt_toolkit import prompt
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.filters import Condition
from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()


@Condition
def is_active():
    """Only active key binding on the second half of each minute"""
    return datetime.datetime.now().second > 30


@bindings.add('c-t', filter=is_active)
def _(event):
    def print_hello():
        print('Hello World')

    run_in_terminal(print_hello)


prompt('> ', key_bindings=bindings)
