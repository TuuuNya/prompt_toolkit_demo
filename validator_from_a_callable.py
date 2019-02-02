from prompt_toolkit.validation import Validator
from prompt_toolkit import prompt


def is_number(text):
    return text.isdigit()


validator = Validator.from_callable(
    is_number,
    error_message='This input contains non-numeric characters',
    move_cursor_to_end=True
)

number = int(prompt('Give a number: ', validator=validator))
print('You said: {}'.format(number))
