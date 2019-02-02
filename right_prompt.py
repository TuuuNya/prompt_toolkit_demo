from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

example_style = Style.from_dict({
    'rprompt': 'bg:#ff0066 #ffffff',
})


def get_rprompt():
    return '<rprompt>'


answer = prompt('> ', rprompt=get_rprompt, style=example_style)
