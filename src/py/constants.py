"""Global constants."""

import pygame

#===============================================================================
# Graphics settings
#===============================================================================
FRAME_RATE = 60
RESOLUTIONS = (
    (1920, 1200),
    (1920, 1080),
    (1600, 1000),
    (1600, 900),
    (1280, 720),
    (800, 600),
)
APP_ICON_PATH = "../../res/pieces/fide/icon.png"

#===============================================================================
# Piece dictionary
#===============================================================================
class Piece:
    def __init__(self, id: int, symbol: str, name: str,
                 army: str, file: str) -> None:
        self.id = id
        self.symbol = symbol
        self.name = name
        self.army = army
        self.file = file

        self.black = pygame.image.load(f"../../res/pieces/{army}/b{file}.png")
        self.white = pygame.image.load(f"../../res/pieces/{army}/w{file}.png")

PIECES: list[Piece] = None
with open("pieces.csv") as csv:
    csv.readline() # discard header line
    data: list[str] = csv.readlines()
    PIECES = [Piece(*line.strip().split(",")) for line in data]

#===============================================================================
# Color presets
#===============================================================================
C_BACKGROUND_DARK = (50, 50, 50)
C_BACKGROUND_LIGHT = (210, 210, 210)
C_TEXT_DARK = (200, 200, 200)
C_TEXT_LIGHT = (50, 50, 50)

C_DARK_SQUARE = (80, 30, 80)
C_LIGHT_SQUARE = (180, 180, 180)

#===============================================================================
# Events
#===============================================================================
# TODO