import models.resource_card
import models.card_collection

def get_resource_cards(num_wood:int,num_stone:int,num_wool:int,num_wheat:int,num_brick:int)->list[models.resource_card.Resource_card]:
    resource_cards = []
    resource_cards.extend([models.resource_card.Resource_card(models.resource_types.Resource_type.Wood) for n in range(num_wood)])
    resource_cards.extend([models.resource_card.Resource_card(models.resource_types.Resource_type.Stone) for n in range(num_stone)])
    resource_cards.extend([models.resource_card.Resource_card(models.resource_types.Resource_type.Wool) for n in range(num_wool)])
    resource_cards.extend([models.resource_card.Resource_card(models.resource_types.Resource_type.Wheat) for n in range(num_wheat)])
    resource_cards.extend([models.resource_card.Resource_card(models.resource_types.Resource_type.Brick) for n in range(num_brick)])
    return resource_cards

