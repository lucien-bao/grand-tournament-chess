"""Global constants."""

import pygame
from pygame.locals import USEREVENT
import pygame.freetype
from pygame.freetype import Font

#===============================================================================
# Graphics settings
#===============================================================================
FRAME_RATE = 60
APP_ICON_PATH = "../../res/pieces/fide/icon.png"


#===============================================================================
# Piece dictionary
#===============================================================================
class Piece:
    def __init__(self, code: int, symbol: str, name: str,
                 army: str, file: str) -> None:
        self.code = int(code)
        self.symbol = symbol
        self.name = name
        self.army = army
        self.file = file

        self.black = pygame.image.load(f"../../res/pieces/{army}/b{file}.png")
        self.white = pygame.image.load(f"../../res/pieces/{army}/w{file}.png")


with open("../pieces.csv") as csv:
    csv.readline()  # discard header line
    data: list[str] = csv.readlines()
    PIECES = [Piece(*line.strip().split(",")) for line in data]

PIECE_MAP = {piece.name.lower(): piece.code for piece in PIECES}

ICONS = [pygame.image.load(f"../../res/pieces/{folder}/icon.png")
         for folder in ["fide", "clob"]]

#===============================================================================
# Color presets
#===============================================================================
C_BACKGROUND_DARK = (30, 30, 30)
C_BACKGROUND_LIGHT = (210, 210, 210)

C_TEXT_DARK = (255, 255, 255)
C_TEXT_LIGHT = (0, 0, 0)
C_TEXT_PROMPT_DARK = (127, 127, 127)
C_TEXT_PROMPT_LIGHT = (127, 127, 127)

C_BUTTON_DARK = (60, 60, 60)
C_BUTTON_LIGHT = (160, 160, 160)
C_BUTTON_HOVER_DARK = (50, 50, 50)
C_BUTTON_HOVER_LIGHT = (140, 140, 140)
C_BUTTON_PRESSED_DARK = (40, 40, 40)
C_BUTTON_PRESSED_LIGHT = (100, 100, 100)

C_TEXT_BOX_DARK = (50, 50, 50)
C_TEXT_BOX_LIGHT = (200, 200, 200)
C_TEXT_BOX_ACTIVE_DARK = (80, 80, 80)
C_TEXT_BOX_ACTIVE_LIGHT = (170, 170, 170)

C_DARK_SQUARE = (80, 30, 80)
C_LIGHT_SQUARE = (180, 180, 180)

#===============================================================================
# Fonts
#===============================================================================
pygame.freetype.init()
F_TITLE = Font("../../res/font/PlusJakartaSans-Bold.ttf", 96)
F_BUTTON = Font("../../res/font/PlusJakartaSans-SemiBold.ttf", 48)
# TODO: subtitle font

#===============================================================================
# Events
#===============================================================================
GO_MENU = USEREVENT
GO_CHOOSE = USEREVENT + 1
GO_PLAY = USEREVENT + 2
GO_TUTORIAL = USEREVENT + 3
GO_OPTIONS = USEREVENT + 4
GO_CREDITS = USEREVENT + 5

#===============================================================================
# Screens
#===============================================================================
MENU = 0
CHOOSE = 1

#===============================================================================
# Miscellaneous
#===============================================================================
CORNER = 0  # for labels, aligns with the BOTTOM left, not top left
LEFT = 1
CENTER = 2
RIGHT = 3

BUTTON_PADDING_SCALAR = 0.02

CARET_BLINK_PERIOD = 90  # in frames
