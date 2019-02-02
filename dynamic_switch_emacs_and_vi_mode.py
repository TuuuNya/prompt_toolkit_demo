from prompt_toolkit import prompt
from prompt_toolkit.application.current import get_app
from prompt_toolkit.filters import Condition
from prompt_toolkit.enums import EditingMode
from prompt_toolkit.key_binding import KeyBindings


def run():
    bindings = KeyBindings()

    @bindings.add('f4')
    def _(event):
        """ Toggle between Emacs and Vi mode. """
        app = event.app

        if app.editing_mode == EditingMode.VI:
            app.editing_mode = EditingMode.EMACS
        else:
            app.editing_mode = EditingMode.VI

    # add a toolbar at the bottom to display the current input mode
    def bottom_toolbar():
        """ Display the current input mode """
        text = 'Vi' if get_app().editing_mode == EditingMode.VI else 'Emacs'
        return [
            ('class:toolbar', ' [F4] {}'.format(text))
        ]

    prompt('> ', key_bindings=bindings, bottom_toolbar=bottom_toolbar)


run()
