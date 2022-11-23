import sys
sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")


from dataclasses import dataclass, field
import models.resource_types

@dataclass
class Tile:
    resource_type:models.resource_types.Resource_type
    coordinates:tuple[int,int] #x,y - column,row
    adjecent_tile_coordinates:list = field(init=False) 
    has_robber:bool
    prob_number:int
    def __str__(self):
        string_representation = f"Type: {self.resource_type}"
        string_representation += f"At coordinates: {self.coordinates}"
        string_representation += f"With prob number: {self.prob_number} "
        return string_representation
    #prob. number

    #def __post_init__(self):
    #    self.adjecent_tile_coordinates = self.get_adjecent_nodes(self.coordinates)