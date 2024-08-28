"""General UI components."""
import pygame.mouse
from pygame import Surface, Rect
from pygame.freetype import STYLE_DEFAULT
from pygame.event import post, Event

from settings import *


def center(corner: tuple[float, float],
           dimensions: Rect) \
        -> tuple[float, float]:
    return (corner[0] - dimensions.width / 2,
            corner[1] - dimensions.height / 2)


class Label:
    def __init__(self, text: str, position: tuple[float, float],
                 font: Font) -> None:
        """
        Constructor.

        :param text: label text.
        :param position: label (x, y) coordinates.
        :param font: font family of label text.
        """
        self.text = text
        self.position = position
        self.font = font

    def draw(self, surface: Surface) -> None:
        """
        Draws this label to the given surface.

        :param surface: pygame Surface to draw onto.
        """
        render = self.font.render(
            text=self.text,
            fgcolor=C_TEXT_DARK if get_dark_mode() else C_TEXT_LIGHT,
            bgcolor=None,
            style=STYLE_DEFAULT,
            rotation=0,
            size=self.font.size
        )

        if get_text_mode() == CORNER:
            surface.blit(render[0], (self.position[0], self.position[1] - render[1].height))
        elif get_text_mode() == CENTER:
            surface.blit(render[0],
                         center(self.position, render[1]))


class Button:
    def __init__(self, text: str, position: tuple[float, float],
                 font: Font, event_type: int = None,
                 dimensions: tuple[float, float] = None,
                 text_align: bool = LEFT) -> None:
        """
        Constructor.

        :param text: button text.
        :param position: button (x, y) coordinates.
        :param font: font family of button text.
        :param event_type: (optional) event type (ID number) to post when
                           this button is clicked.
        :param dimensions: (optional) button size.
        :param text_align: (optional) alignment of text within button. Ignored
                           if dimensions is set to None. May be LEFT, CENTER,
                           or RIGHT; other values may result in undefined
                           behavior.
        """
        self.text = text
        self.position = position
        self.font = font

        if dimensions is None:
            render = self.font.render(
                text=self.text,
                fgcolor=C_TEXT_DARK if get_dark_mode() else C_TEXT_LIGHT,
                bgcolor=None,
                style=STYLE_DEFAULT,
                rotation=0,
                size=self.font.size
            )
            bounds = render[1]
            self.dimensions = (bounds.width + 2 * BUTTON_PADDING,
                               self.font.size + 2 * BUTTON_PADDING)
            self.dimensionsFlag = False
        else:
            self.dimensions = dimensions
            self.dimensionsFlag = True

        self.text_align = text_align
        self.event_type = event_type

    def draw(self, surface: Surface) -> None:
        """
        Draws this label to the given surface.

        :param surface: pygame Surface to draw onto.
        """
        render = self.font.render(
            text=self.text,
            fgcolor=C_TEXT_DARK if get_dark_mode() else C_TEXT_LIGHT,
            bgcolor=None,
            style=STYLE_DEFAULT,
            rotation=0,
            size=self.font.size
        )
        if not self.dimensionsFlag:
            x_adjust = BUTTON_PADDING
        elif self.text_align == LEFT:
            x_adjust = BUTTON_PADDING
        elif self.text_align == CENTER:
            x_adjust = (self.dimensions[0] - render[1].width) / 2
        else:  # self.text_align == RIGHT
            x_adjust = self.dimensions[0] - render[1].width - BUTTON_PADDING
        y_adjust = (self.dimensions[1] - self.font.size) / 2 if self.dimensionsFlag else BUTTON_PADDING

        if get_button_mode() == CORNER:
            pygame.draw.rect(
                surface,
                self.get_color(),
                Rect(self.position[0], self.position[1],
                     self.dimensions[0], self.dimensions[1])
            )
            surface.blit(
                render[0],
                (self.position[0] + x_adjust,
                 self.position[1] + y_adjust)
            )
        elif get_button_mode() == CENTER:
            pygame.draw.rect(
                surface,
                self.get_color(),
                Rect(self.position[0] - self.dimensions[0] / 2,
                     self.position[1] - self.dimensions[1] / 2,
                     self.dimensions[0],
                     self.dimensions[1])
            )
            surface.blit(
                render[0],
                (self.position[0] - self.dimensions[0] / 2 + x_adjust,
                 self.position[1] - self.dimensions[1] / 2 + y_adjust,
                 self.dimensions[0],
                 self.dimensions[1])
            )

    def check_click(self) -> None:
        """
        Should be called on each frame; checks if this button is clicked,
        and if so, posts this button's event.
        """
        if self.event_type is None:
            return
        if self.is_pressed():
            post(Event(self.event_type))

    def is_hovered(self) -> bool:
        """
        Get whether the mouse is currently hovering above this button.
        Ignores the presence of occluding objects.

        :return: whether the mouse's coordinates are within the bounds of
                 this button.
        """
        if get_button_mode() == CORNER:
            return Rect(self.position[0], self.position[1],
                        self.dimensions[0], self.dimensions[1]) \
                .collidepoint(pygame.mouse.get_pos())
        elif get_button_mode() == CORNER:
            return Rect(self.position[0] - self.dimensions[0] / 2,
                        self.position[1] - self.dimensions[1] / 2,
                        self.dimensions[0],
                        self.dimensions[1]
                        ) \
                .collidepoint(pygame.mouse.get_pos())

    def is_pressed(self) -> bool:
        """
        Get whether the mouse is pressed on this button.
        Ignores the presence of occluding objects.

        :return: whether the mouse is inside this button and pressed (mouse 1).
        """
        return pygame.mouse.get_pressed()[0] and self.is_hovered()

    def get_color(self) -> tuple[int, int, int]:
        """
        Get the background color appropriate to the current theme and
        hover/pressed condition.

        :return: an int 3-tuple for the color's RGB.
        """
        if get_dark_mode():
            if self.is_pressed():
                return C_BUTTON_PRESSED_DARK
            if self.is_hovered():
                return C_BUTTON_HOVER_DARK
            return C_BUTTON_DARK
        else:
            if self.is_pressed():
                return C_BUTTON_PRESSED_LIGHT
            if self.is_hovered():
                return C_BUTTON_HOVER_LIGHT
            return C_BUTTON_LIGHT


class Transition:
    pass
