"""Menu screen."""
from pygame.locals import *

from ui import *
from settings import *

#===============================================================================
# Setup
#===============================================================================
components: list[Button | Label] = []

title0 = Label("Grand", (100, 200), F_TITLE)
title1 = Label("Tournament", (100, 300), F_TITLE)
title2 = Label("Chess", (100, 400), F_TITLE)
components.append(title0)
components.append(title1)
components.append(title2)

play_button = Button("Play", (100, 500), F_BUTTON)  # TODO
tutorial_button = Button("Tutorial", (100, 600), F_BUTTON)
options_button = Button("Options", (100, 700), F_BUTTON)
credits_button = Button("Credits", (100, 800), F_BUTTON)
quit_button = Button("Quit", (100, 900), F_BUTTON, QUIT)
components.append(play_button)
components.append(tutorial_button)
components.append(options_button)
components.append(credits_button)
components.append(quit_button)


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
        if isinstance(component, Button):
            component.check_click()
