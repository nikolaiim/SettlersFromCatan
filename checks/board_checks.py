import models


class BoardChecks:

    @staticmethod
    def get_adjecent_tiles(tile_coordinates: tuple[int, int]) -> list[tuple[int,int]]:
        """"Input a node coordinate and get coordinates of all 6 adjecent tiles."""
        adjecent_tile_coordinates = list()
        col = tile_coordinates[0]
        row = tile_coordinates[1]

        if tile_coordinates[0] % 2 == 1:  # row is odd
            adjecent_tile_coordinates.append((col - 1, row - 1))
            adjecent_tile_coordinates.append((col, row - 1))

            adjecent_tile_coordinates.append((col - 1, row))
            adjecent_tile_coordinates.append((col + 1, row))

            adjecent_tile_coordinates.append((col - 1, row + 1))
            adjecent_tile_coordinates.append((col, row + 1))

            return adjecent_tile_coordinates

        if tile_coordinates[0] % 2 == 0:  # row is even
            adjecent_tile_coordinates.append((col, row - 1))
            adjecent_tile_coordinates.append((col + 1, row - 1))

            adjecent_tile_coordinates.append((col - 1, row))
            adjecent_tile_coordinates.append((col + 1, row))

            adjecent_tile_coordinates.append((col, row + 1))
            adjecent_tile_coordinates.append((col + 1, row + 1))

            return adjecent_tile_coordinates

    @staticmethod
    def coordinates_to_tile(board: models.Board, coordinates:tuple[int,int]) -> models.Tile:
        for tile in board.tiles:
            if tile.coordinates == coordinates:
                return tile
        return None



    @staticmethod
    def is_placement_valid(board: models.Board, placement: list[tuple[int, int]], player:models.Player, is_first_round:bool=False) -> bool:
        for construction in board.constructions:
            if placement.sort() == construction.location.sort():
                return False  # already a construction on location

        if BoardChecks.location_is_town_or_city(placement):
            if BoardChecks.is_construction_too_close(board,placement):
                return False #existing town or city is too close to placement

        #for rounds that are not first round, the player needs to have a road connected to whatever its building


        #does player have a road close enough?
    ##does player have a construction close enough? allways neighbouring road

    @staticmethod
    def does_player_have_connecting_road_to_coordinate(board:models.Board, player: models.Player, placement: list[tuple[int,int]],is_first_round):
        if not is_first_round:
            if BoardChecks.location_is_town_or_city(placement):
                pass
            elif: ##add check if is road
                tile1_neighbours = BoardChecks.coordinates_to_tile(placement[0]).adjecent_tile_coordinates
                tile2_neighbours = BoardChecks.coordinates_to_tile(placement[1]).adjecent_tile_coordinates

                tile3_neighbours, tile4_neighbours = intersection(tile1_neighbours,tile2_neighbours)

        # is road,


    @staticmethod
    def is_construction_too_close(board: models.board.Board, placement: list[tuple[int, int]]) -> bool:
        """Checks if there is a construction too close to placement. Works for towns, as len(placement)==3"""

        first_direction = [placement[0], placement[1]]
        second_direction = [placement[0], placement[2]]
        third_direction = [placement[1], placement[2]]

        for construction in board.constructions:
            if first_direction[0] in construction.location and first_direction[1] in construction.location:
                return True
            if second_direction[0] in construction.location and second_direction[1] in construction.location:
                return True
            if third_direction[0] in construction.location and third_direction[1] in construction.location:
                return True
        return False

    @staticmethod
    def location_is_town_or_city(location:list[tuple[int,int]]) -> bool:
        if len(location) == 3:
            return True
        elif len(location == 2):
            return False
        raise ValueError


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3