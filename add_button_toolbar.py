from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML


def bottom_toolbar():
    return HTML('This a <b><style bg="ansired">Toolbar</style></b>')


text = prompt('> ', bottom_toolbar=bottom_toolbar)
print('You said: {}'.format(text))
