from dataclasses import dataclass
import models.resource_card
import models.card_collection


@dataclass
class Player:
    name:str
    cards: models.card_collection.Card_collection
