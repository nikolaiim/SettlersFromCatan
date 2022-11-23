from resource_helpers import get_resource_cards
from dataclasses import dataclass
import models.resource_card


@dataclass
class Development_card(models.buyable_item.Buyable_item):
    price: list[models.resource_card.Resource_card]

    def __init__(self):
        self.price = get_resource_cards(0, 1, 1, 1, 0)

    def play_card(self):
        pass


@dataclass
class Knight(Development_card):

    def play_card(self):
        print("Playing knight")
