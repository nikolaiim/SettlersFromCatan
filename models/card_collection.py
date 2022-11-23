import sys
sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")


from dataclasses import dataclass
import models.resource_card
import resource_helpers

@dataclass
class Card_collection:
    cards: list[models.resource_card.Resource_card]

    def add_cards(self,num_wood:int,num_stone:int,num_wool:int,num_wheat:int,num_brick:int):
        self.cards.extend(resource_helpers.get_resource_cards(num_wood,num_stone,num_wool,num_wheat,num_brick))

    def remove_cards(self,cards: list[models.resource_card.Resource_card]):
        temp_cards = self.cards

        for card in temp_cards:
            self.cards.remove(card)
        
        self.cards = temp_cards
