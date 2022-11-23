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

        if not BoardChecks.does_player_have_connecting_road_to_coordinate(board,player,placement,is_first_round=is_first_round):
            return False #player doesn't have a road connecting to placement

        return True




        #does player have a road close enough?
    ##does player have a construction close enough? allways neighbouring road

    @staticmethod
    def does_player_have_connecting_road_to_coordinate(board:models.Board, player: models.Player, placement: list[tuple[int,int]],is_first_round) -> bool:
        if not is_first_round:
            if BoardChecks.location_is_town_or_city(placement):
                for construction in board.constructions:
                    if isinstance(construction, models.constructions.Road) and construction.owner == player:
                        tile1_coordinates = placement[0]
                        tile2_coordinates = placement[1]
                        tile3_coordinates = placement[2]
                        construction_coordinates = construction.location.sort()
                        if (construction_coordinates == [tile1_coordinates,tile2_coordinates].sort()
                                or construction_coordinates == [tile1_coordinates,tile3_coordinates].sort()
                                or construction_coordinates == [tile2_coordinates,tile3_coordinates].sort()):
                            return True


            else: #is road
                tile1_coordinates = placement[0]
                tile2_coordinates = placement[1]

                tile1_neighbours = BoardChecks.coordinates_to_tile(tile1_coordinates).adjecent_tile_coordinates
                tile2_neighbours = BoardChecks.coordinates_to_tile(tile2_coordinates).adjecent_tile_coordinates

                tile3_coordinates, tile4_coordinates = intersection(tile1_neighbours,tile2_neighbours)

                for construction in board.constructions:
                    if isinstance(construction,models.constructions.Road) and construction.owner == player:
                        construction_coordinates = construction.location.sort()
                        if (construction_coordinates == [tile1_coordinates, tile3_coordinates].sort()
                                or construction_coordinates == [tile1_coordinates, tile4_coordinates].sort()
                                or construction_coordinates == [tile2_coordinates, tile3_coordinates].sort()
                                or construction_coordinates == [tile2_coordinates, tile4_coordinates].sort()):
                            return True
        False





                ##check if there is road between (tile 1 and tuke 3 or 4) OR (tile 2 and 3 or 4)

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