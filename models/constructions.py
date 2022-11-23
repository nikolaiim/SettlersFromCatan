import sys
sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")


from dataclasses import dataclass, field
from typing import Optional
from resource_helpers import get_resource_cards
import models.player
import models.buyable_item
import models.construction

@dataclass
class Town(models.buyable_item.Buyable_item,models.construction.Construction):
    price: list[models.resource_card.Resource_card] 
    def check_valid_location(location: list, Board) -> bool:
        #three tiles are given:
        if len(location) != 3:
            return False

        #all tiles are adjecent
        #if not (location[0] in get_adjecent_tiles(location[1]) and location[0] in get_adjecent_tiles(location[2]) and location[1] in get_adjecent_tiles(location[2])):
        #    return False

        #location is not occupied

    def __init__(self, owner = None, location = None  ) -> None:
        super().__init__()
        self.price = get_resource_cards(1,0,1,1,1)
        self.owner = owner
        self.location = location

@dataclass
class City(models.buyable_item.Buyable_item,models.construction.Construction):
    price: list[models.resource_card.Resource_card]
    def check_valid_location(location: list, Board) -> bool:
        pass
    def __init__(self, owner = None, location = None  ):
        super().__init__()
        self.price = get_resource_cards(0,3,0,2,0)
        self.owner = owner
        self.location = location

@dataclass
class Road(models.buyable_item.Buyable_item,models.construction.Construction):
    price: list[models.resource_card.Resource_card] 

    def check_valid_location(location: list, Board) -> bool:
        pass

    def __init__(self, owner = None, location = None  ):
        super().__init__()
        self.price = get_resource_cards(1,0,0,0,1)
        self.owner = owner
        self.location = location