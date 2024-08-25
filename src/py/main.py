"""Entry point of the program."""

import sys
import pygame
from pygame.locals import *

from constants import *

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


def handle_events() -> None:
    """
    Polls all events from the pygame event queue and handles
    dispatches.

    Parameters
    ---
    (no parameters)

    Returns
    ---
    None
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def draw() -> None:
    """
    Handles all display.

    Parameters
    ---
    (no parameters)

    Returns
    ---
    None
    """
    display.fill(C_BACKGROUND_DARK)
    # TODO: draw board + ui

    # DEBUG: testing display :)
    display.blit(PIECES[11].white, (10, 10))

    pygame.display.update()


#===============================================================================
# Mainloop
#===============================================================================
while True:
    # specify amount of time between frames via frame rate
    clock.tick(FRAME_RATE)

    handle_events()
    draw()
