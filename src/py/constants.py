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


with open("pieces.csv") as csv:
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
C_BUTTON_DARK = (60, 60, 60)
C_BUTTON_LIGHT = (160, 160, 160)
C_BUTTON_HOVER_DARK = (50, 50, 50)
C_BUTTON_HOVER_LIGHT = (140, 140, 140)
C_BUTTON_PRESSED_DARK = (40, 40, 40)
C_BUTTON_PRESSED_LIGHT = (100, 100, 100)

C_DARK_SQUARE = (80, 30, 80)
C_LIGHT_SQUARE = (180, 180, 180)

#===============================================================================
# Fonts
#===============================================================================
pygame.freetype.init()
F_TITLE = Font("../../res/font/Roboto-Medium.ttf", 96)
F_BUTTON = Font("../../res/font/Roboto-Medium.ttf", 48)

#===============================================================================
# Events
#===============================================================================
GO_MENU = USEREVENT
GO_PLAY = USEREVENT + 1
GO_TUTORIAL = USEREVENT + 2
GO_OPTIONS = USEREVENT + 3
GO_CREDITS = USEREVENT + 4

#===============================================================================
# Screens
#===============================================================================
MENU = 0

#===============================================================================
# Miscellaneous
#===============================================================================
CORNER = 0  # for labels, aligns with the BOTTOM left, not top left
LEFT = 1
CENTER = 2
RIGHT = 3

BUTTON_PADDING_SCALAR = 0.02
