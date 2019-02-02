from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt


class NumberValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            for i, c in enumerate(text):
                if not c.isdigit():
                    break
            raise ValidationError(message='This input contains non-numeric charachters', cursor_position=i)


number = int(prompt('Give a number: ', validator=NumberValidator(), validate_while_typing=True))
print('You said: {}'.format(number))
