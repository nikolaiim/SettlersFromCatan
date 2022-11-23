import models

class BoardActions:

    @staticmethod
    def generate_board(num_rows: int, num_cols: int) -> models.board:
        rows = list()
        for y in range(num_rows):
            row = list()
            for x in range(num_cols):
                tile = models.tile.Tile(models.resource_types, (x, y), False, models.dices.Dices.throw())
                row.append(tile)
            rows.append(row)

        return models.board.Board(rows, list())

    @staticmethod
    def place_construction(board: models.board.Board, construction: models.construction.Construction):
        pass
