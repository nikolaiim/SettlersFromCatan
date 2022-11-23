import sys
sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")

from dataclasses import dataclass
from abc import ABC
import models.resource_card


class Buyable_item(ABC):
    price:list[models.resource_card.Resource_card] = None

    def __init__(self) -> None:
        super().__init__()