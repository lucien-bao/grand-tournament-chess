"""Global settings."""

from constants import *

_dark_mode: bool = True
_text_mode: int = CORNER
_button_mode: int = CORNER
_resolution: tuple[int, int] = RESOLUTIONS[0]


def get_dark_mode() -> bool:
    """
    Get the current dark mode setting.

    :return: the current dark mode setting.
    """
    return _dark_mode


def set_dark_mode(value: bool) -> None:
    """
    Change the current dark mode setting.

    :param value: the desired dark mode setting.
    """
    global _dark_mode
    _dark_mode = value


def get_text_mode() -> int:
    """
    Get the current text mode setting.

    :return: the current text mode setting.
    """
    return _text_mode


def set_text_mode(value: int) -> None:
    """
    Change the current text mode setting.
    Values other than the defined CORNER and CENTER constants
    may lead to undefined behavior.

    :param value: the desired text mode setting.
    """
    global _text_mode
    _text_mode = value


def get_button_mode() -> int:
    """
    Get the current button mode setting.

    :return: the current button mode setting.
    """
    return _button_mode


def set_button_mode(value: int) -> None:
    """
    Change the current button mode setting.
    Values other than the defined CORNER and CENTER constants
    may lead to undefined behavior.

    :param value: the desired button mode setting.
    """
    global _button_mode
    _button_mode = value


def get_resolution() -> tuple[int, int]:
    """
    Get the current resolution.

    :return: the current resolution.
    """
    return _resolution


def set_resolution(value: tuple[int, int]) -> None:
    """
    Change the current resolution.

    :param value: the desired resolution.
    """
    global _resolution
    _resolution = value
