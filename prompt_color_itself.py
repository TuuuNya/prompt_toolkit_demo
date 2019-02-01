from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

style = Style.from_dict({
    # User input ( default text )
    # '': '#ff0066',

    # Prompt
    'username': '#884444',
    'at': '#00aa00',
    'colon': '#0000aa',
    'pound': '#00aa00',
    'host': '#00ffff bg:#444400',
    'path': 'ansicyan underline',
})

message = [
    ('class:username', 'TuuuNya'),
    ('class:at', '@'),
    ('class:host', 'localhost'),
    ('class:colon', ':'),
    ('class:path', '~'),
    ('class:pound', '# '),
]

text = prompt(message, style=style)

