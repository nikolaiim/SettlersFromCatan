from dataclasses import dataclass
#from player import Player
import models.player
import models.board

@dataclass
class Game:
    players: list[models.player.Player]
    board: models.board.Board
