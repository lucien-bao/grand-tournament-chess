"""Screen where players choose armies before battle."""

from ui import *

components: list[Drawable] = []

#===============================================================================
# Setup
#===============================================================================


title = Label("Enter", (0.05, 0.194), F_TITLE)
components.append(title)
# TODO: subtitle

text_box_1 = TextBox((0.15, 0.45),
                     0.4,
                     F_BUTTON,
                     "Name")
components.append(text_box_1)
text_box_2 = TextBox((0.15, 0.65),
                     0.4,
                     F_BUTTON,
                     "Name")
components.append(text_box_2)


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
    for component in components:
        if isinstance(component, TextBox):
            component.check_click()


def send_key_down(key_down: Event) -> None:
    """
    Callback for key-down events. Passes them along to
    the text boxes.
    """
    for component in components:
        if isinstance(component, TextBox):
            component.check_type(key_down)
