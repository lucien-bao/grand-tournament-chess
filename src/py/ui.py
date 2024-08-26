"""General UI components."""
import pygame.mouse
from pygame import Surface, Rect
from pygame.freetype import STYLE_DEFAULT

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
            surface.blit(render[0], self.position)
        elif get_text_mode() == CENTER:
            surface.blit(render[0],
                         center(self.position, render[1]))


class Button:
    def __init__(self, text: str, position: tuple[float, float],
                 font: Font, dimensions: tuple[float, float] = None,
                 text_align: bool = LEFT) -> None:
        """
        Constructor.

        :param text: button text.
        :param position: button (x, y) coordinates.
        :param font: font family of button text.
        :param dimensions: button size (optional).
        :param text_align: alignment of text within button. Ignored if
                           dimensions is set to None.
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
                               bounds.height + 2 * BUTTON_PADDING)
        else:
            self.dimensions = dimensions

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

        if get_button_mode() == CORNER:
            pygame.draw.rect(
                surface,
                self.get_color(),
                Rect(self.position[0], self.position[1],
                     self.dimensions[0], self.dimensions[1])
            )
            surface.blit(
                render[0],
                (self.position[0] + BUTTON_PADDING,
                 self.position[1] + BUTTON_PADDING)
            )
        elif get_button_mode() == CENTER:
            pygame.draw.rect(
                surface,
                self.get_color(),
                Rect(self.position[0] - self.dimensions[0] / 2,
                     self.position[1] - self.dimensions[1] / 2,
                     self.dimensions[0],
                     self.dimensions[1]
                     )
            )
            surface.blit(
                render[0],
                (self.position[0] - self.dimensions[0] / 2 + BUTTON_PADDING,
                 self.position[1] - self.dimensions[1] / 2 + BUTTON_PADDING,
                 self.dimensions[0],
                 self.dimensions[1])
            )

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
