"""Menu screen."""
from math import sin, cos, pi

from pygame.locals import *

from ui import *

components: list[Button | Label] = []


#===============================================================================
# Setup
#===============================================================================
def setup() -> None:
    """
    Add all components.
    """
    title0 = Label("Grand", (0.05, 0.194), F_TITLE)
    title1 = Label("Tournament", (0.05, 0.296), F_TITLE)
    title2 = Label("Chess", (0.05, 0.398), F_TITLE)
    components.append(title0)
    components.append(title1)
    components.append(title2)

    play_button = Button("Play", (0.05, 0.463), F_BUTTON, GO_PLAY)
    tutorial_button = Button("Tutorial", (0.05, 0.555), F_BUTTON, GO_TUTORIAL)
    options_button = Button("Options", (0.05, 0.648), F_BUTTON, GO_OPTIONS)
    credits_button = Button("Credits", (0.05, 0.740), F_BUTTON, GO_CREDITS)
    quit_button = Button("Quit", (0.05, 0.833), F_BUTTON, QUIT)
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
    if len(components) == 0:
        setup()

    for component in components:
        component.draw(surface)

    res = settings.get_resolution()
    splash_center = res[0] * 13 / 20, res[1] / 2
    radius = res[1] / 3.5

    pygame.draw.rect(surface, (255, 255, 255), (*splash_center, 10, 10))

    # TODO: left off here. remake icons to be bigger
    for i in range(len(ICONS)):
        angle = i * (2 * pi / len(ICONS)) + 0.5  # radians
        x = radius * cos(angle)
        y = radius * sin(angle)

        icon = ICONS[i]
        surface.blit(icon, (splash_center[0] + x - icon.get_width() / 2,
                            splash_center[1] + y - icon.get_height() / 2))


def update() -> None:
    """
    Check for input and post events as needed.
    """
    for component in components:
        if isinstance(component, Button):
            component.check_click()
