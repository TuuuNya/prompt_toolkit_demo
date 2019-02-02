from prompt_toolkit import prompt
import getpass

prompt('What is your name: ', default='${}'.format(getpass.getuser()))
