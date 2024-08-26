"""Menu screen."""

from ui import *
from settings import *

button = Button("button",
                (100, 100),
                F_BODY)


def display(surface: Surface) -> None:
    """
    Draw the menu screen.

    :param surface: the pygame Surface to draw to,
    """
    set_button_mode(CORNER)
    button.draw(surface)
    set_button_mode(CENTER)
    button.draw(surface)
