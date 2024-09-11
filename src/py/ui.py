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


class Drawable:
    """
    A UI component that can be drawn to the screen.
    """

    def draw(self, surface: Surface) -> None:
        pass


class Label(Drawable):
    """
    Component that simply renders a line of text.
    """

    def __init__(self, text: str, position: tuple[float, float],
                 font: Font) -> None:
        """
        Constructor.

        :param text: label text.
        :param position: label (x, y) relative position.
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
        x, y = (self.position[0] * get_resolution()[0],
                self.position[1] * get_resolution()[1])

        render = self.font.render(
            text=self.text,
            fgcolor=C_TEXT_DARK if get_dark_mode() else C_TEXT_LIGHT,
            bgcolor=None,
            style=STYLE_DEFAULT,
            rotation=0,
            size=self.font.size
        )

        if get_text_mode() == CORNER:
            surface.blit(render[0], (x, y - render[1].height))
        elif get_text_mode() == CENTER:
            surface.blit(render[0],
                         center((x, y), render[1]))


def get_padding() -> float:
    """
    Get the absolute padding amount.

    :return: the padding amount.
    """
    return 15 + (get_resolution()[0] - 1536) * BUTTON_PADDING_SCALAR


class Button(Drawable):
    """
    Component that renders a button to the screen and detects
    some mouse events.
    """

    def __init__(self, text: str, position: tuple[float, float],
                 font: Font, event_type: int = None,
                 dimensions: tuple[float, float] = None,
                 text_align: bool = LEFT) -> None:
        """
        Constructor.

        :param text: button text.
        :param position: button (x, y) relative position.
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

        if dimensions is not None:
            self.dimensions = dimensions
            self.dimensions_flag = True
        else:
            self.dimensions = None
            self.dimensions_flag = False

        self.text_align = text_align
        self.event_type = event_type

    def draw(self, surface: Surface) -> None:
        """
        Draws this button to the given surface.

        :param surface: pygame Surface to draw onto.
        """
        x, y = self.get_coordinates()

        render = self.font.render(
            text=self.text,
            fgcolor=C_TEXT_DARK if get_dark_mode() else C_TEXT_LIGHT,
            bgcolor=None,
            style=STYLE_DEFAULT,
            rotation=0,
            size=self.font.size
        )
        bounds = render[1]
        if not self.dimensions_flag:
            self.dimensions = (bounds.width + 2 * get_padding(),
                               self.font.size + 2 * get_padding())

        if self.text_align == CENTER:
            x_adjust = (self.dimensions[0] - render[1].width) / 2
        elif self.text_align == LEFT:
            x_adjust = get_padding()
        else:  # self.text_align == RIGHT
            x_adjust = self.dimensions[0] - render[1].width - get_padding()
        y_adjust = (self.dimensions[1] - self.font.size) / 2

        if get_button_mode() == CORNER:
            pygame.draw.rect(
                surface,
                self.get_color(),
                Rect(x, y,
                     self.dimensions[0], self.dimensions[1])
            )
            surface.blit(
                render[0],
                (x + x_adjust,
                 y + y_adjust)
            )
        elif get_button_mode() == CENTER:
            pygame.draw.rect(
                surface,
                self.get_color(),
                Rect(x - self.dimensions[0] / 2,
                     y - self.dimensions[1] / 2,
                     self.dimensions[0],
                     self.dimensions[1])
            )
            surface.blit(
                render[0],
                (x - self.dimensions[0] / 2 + x_adjust,
                 y - self.dimensions[1] / 2 + y_adjust,
                 self.dimensions[0],
                 self.dimensions[1])
            )

    def get_coordinates(self) -> tuple[float, float]:
        """
        Get the absolute coordinates of this button.

        :return: a pair of (x, y) coordinates.
        """
        return (self.position[0] * get_resolution()[0],
                self.position[1] * get_resolution()[1])

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
        x, y = self.get_coordinates()

        if get_button_mode() == CORNER:
            return Rect(x, y,
                        self.dimensions[0], self.dimensions[1]) \
                .collidepoint(pygame.mouse.get_pos())
        elif get_button_mode() == CENTER:
            return Rect(x - self.dimensions[0] / 2,
                        y - self.dimensions[1] / 2,
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


class TextBox(Drawable):
    """
    An interactable area for inputting one line of text.
    """

    def __init__(self, position: tuple[float, float],
                 width: float, font: Font, prompt: str = None) -> None:
        """
        Constructor.

        :param position: text box relative (x, y) position.
        :param width: text box relative width.
        :param font: font family of entered text and prompted text
                     (if prompt is specified).
        :param prompt: (optional) text to show when text box is empty.
        """
        self.position = position
        self.width = width
        self.font = font
        if prompt is None:
            self.prompt = ""
        else:
            self.prompt = prompt
        self.text = ""
        self.selected = False
        self.caret_frame_count = 0

    def draw(self, surface: Surface) -> None:
        """
        Draw this text box to the given surface.

        :param surface: the surface to draw to.
        """
        x, y = self.get_coordinates()
        w, h = self.get_width(), self.font.size + 2 * get_padding()

        # TODO: "caret" simulation
        text_to_render = self.text if len(self.text) > 0 else self.prompt
        if get_dark_mode():
            text_color = C_TEXT_DARK if len(self.text) > 0\
                else C_TEXT_PROMPT_DARK
            box_color = C_TEXT_BOX_ACTIVE_DARK if self.selected\
                else C_TEXT_BOX_DARK
        else:
            text_color = C_TEXT_LIGHT if len(self.text) > 0\
                else C_TEXT_PROMPT_LIGHT
            box_color = C_TEXT_BOX_ACTIVE_LIGHT if self.selected\
                else C_TEXT_BOX_ACTIVE_LIGHT
        render = self.font.render(
            text=text_to_render,
            fgcolor=text_color,
            bgcolor=None,
            style=STYLE_DEFAULT,
            rotation=0,
            size=self.font.size
        )

        if get_button_mode() == CORNER:
            pygame.draw.rect(
                surface,
                box_color,
                Rect(x, y, w, h)
            )
            surface.blit(
                render[0],
                (x + get_padding(),
                 y + get_padding())
            )
        elif get_button_mode() == CENTER:
            pygame.draw.rect(
                surface,
                box_color,
                Rect(x - w / 2, y - h / 2, w, h)
            )
            surface.blit(
                render[0],
                (x - w / 2 + get_padding(),
                 y - h / 2 + get_padding())
            )

    def get_coordinates(self) -> tuple[float, float]:
        """
        Get the absolute coordinates of this text box.

        :return: a pair of (x, y) coordinates.
        """
        return (self.position[0] * get_resolution()[0],
                self.position[1] * get_resolution()[1])

    def get_width(self) -> float:
        """
        Get the absolute width of this text box.

        :return: width in pixels.
        """
        return self.width * get_resolution()[0]

    def check_click(self) -> None:
        """
        Should be called on each frame; checks if this text box is clicked,
        and if so, selects this text box as active. If the mouse is clicked
        outside the text box, unselects this text box.
        """
        if pygame.mouse.get_pressed()[0]:
            if self.is_hovered():
                self.selected = True
                self.caret_frame_count = 0
                # TODO: use caret frame count to animate caret
            else:
                self.selected = False

    def check_type(self, key_down: Event) -> None:
        """
        Should be called on each key down event; checks if this text box
        is active, and if so, updates the text state.

        :param key_down: pygame key down event.
        """
        if not self.selected:
            return

        if key_down.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += key_down.unicode

    def is_hovered(self) -> bool:
        """
        Get whether the mouse is currently hovering above this button.
        Ignores the presence of occluding objects.

        :return: whether the mouse's coordinates are within the bounds of
                 this button.
        """
        x, y = self.get_coordinates()
        w, h = self.get_width(), self.font.size + 2 * get_padding()

        if get_button_mode() == CORNER:
            return Rect(x, y, w, h).collidepoint(pygame.mouse.get_pos())
        elif get_button_mode() == CENTER:
            return Rect(x - w / 2, y - h / 2, w, h) \
                .collidepoint(pygame.mouse.get_pos())


class Transition:
    pass
