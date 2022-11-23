
import models.player
import models.buyable_item
import models.resource_card
import resource_helpers
from dataclasses import dataclass
from typing import Optional
from abc import ABC,abstractmethod


@dataclass
class Construction(ABC):
    location:Optional[list] #location defined as between two tiles for Roads and between three for Town&City
    owner: Optional[models.player.Player]

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def check_valid_location(location:list, Board)-> bool:
        pass

