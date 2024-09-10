"""Entry point of the program."""

import sys

import pygame.display
from pygame.locals import *

from settings import *
import menu

#===============================================================================
# Setup
#===============================================================================
pygame.init()
pygame.display.set_caption("Grand Tournament Chess")

display: pygame.Surface = pygame.display.set_mode()
clock: pygame.time.Clock = pygame.time.Clock()

pygame.display.set_icon(
    pygame.image.load(APP_ICON_PATH)
    .convert_alpha()
)

screen = MENU
screens = [menu]
set_dark_mode(True)
set_text_mode(CORNER)
set_button_mode(CORNER)
set_resolution(pygame.display.get_window_size())


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

    screens[screen].display(display)
    screens[screen].update()

    pygame.display.update()


#===============================================================================
# Mainloop
#===============================================================================
while True:
    # specify amount of time between frames via frame rate
    clock.tick(FRAME_RATE)

    handle_events()
    draw()
