"""Screen where players choose armies before battle."""

from ui import *

components: list[Drawable] = []

#===============================================================================
# Setup
#===============================================================================

text_box_1 = TextBox((0.2, 0.3),
                     0.2,
                     F_BUTTON,
                     "player 1 name")
components.append(text_box_1)


#===============================================================================
# Callback
#===============================================================================
def display(surface: Surface) -> None:
    """
    Draw the menu screen.

    :param surface: the pygame Surface to draw to,
    """
    for component in components:
        component.draw(surface)


def update() -> None:
    """
    Check for input and post events as needed.
    """
    # TODO: check for keypress events (in main event loop?)
    for component in components:
        if isinstance(component, TextBox):
            component.check_click()
