from pygments.lexers.html import HtmlLexer
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.lexers import PygmentsLexer

text = prompt('Enter Html: ', lexer=PygmentsLexer(HtmlLexer))
print('You input: {}'.format(text))
