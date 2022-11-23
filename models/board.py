import sys

sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")

import models.tile
import models.construction
import models.resource_types


class Board:
    tiles: list[models.tile.Tile]
    constructions: list[models.construction.Construction]

    def __init__(self, tiles: list[models.tile.Tile], constructions: list[models.construction.Construction]):
        self.tiles = tiles
        self.constructions = constructions

    def __str__(self):
        for row in self.tiles:
            for tile in row:
                print(tile)

