"""Entry point of the program."""

import sys
from pygame.locals import *

from settings import *
import menu

#===============================================================================
# Setup
#===============================================================================
pygame.init()
pygame.display.set_caption("Grand Tournament Chess")

resolution: tuple[int, int] = RESOLUTIONS[0]
display: pygame.Surface = pygame.display.set_mode()
clock: pygame.time.Clock = pygame.time.Clock()

pygame.display.set_icon(
    pygame.image.load(APP_ICON_PATH)
    .convert_alpha()
)

screen = MENU


def handle_events() -> None:
    """
    Polls all events from the pygame event queue and handles
    dispatches.
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def draw() -> None:
    """
    Handles all display.
    """
    display.fill(C_BACKGROUND_DARK if get_dark_mode()
                 else C_BACKGROUND_LIGHT)
    # TODO: draw board + ui

    if screen == MENU:
        menu.display(display)

    pygame.display.update()


#===============================================================================
# Mainloop
#===============================================================================
while True:
    # specify amount of time between frames via frame rate
    clock.tick(FRAME_RATE)

    handle_events()
    draw()
