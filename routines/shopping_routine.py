import sys

sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")

import models



# inputs:
# board - check if some location is available
# player.cards - gotta for for whatever is bought


def shopping_routine(board: models.board.Board, player: models.player.Player):
    helper = Shopping_helper()
    while True:
        # change resouces for other (4:1, 3:1, ...)
        player_can_afford = helper.what_can_player_afford(player.cards)
        # ask player what to buy

    # if construction: place on map


class Shopping_helper:
    buyable_items: list[models.buyable_item.Buyable_item] = [models.constructions.Road(),
                                                             models.constructions.Town(),
                                                             models.constructions.City(),
                                                             models.development_card.Development_card()
                                                             ]

    def what_can_player_afford(self, cards: models.card_collection.Card_collection) -> list[
        models.buyable_item.Buyable_item]:
        items_player_can_afford = []
        for item in self.buyable_items[:]:
            if self.can_player_afford_item(cards, item):
                items_player_can_afford.append(item)
        return items_player_can_afford

    @staticmethod
    def can_player_afford_item(cards: models.card_collection.Card_collection,
                               item: models.buyable_item.Buyable_item) -> bool:
        temp_cards = cards.cards[:]  # will try to remove  cards from temp_cards
        price_of_item = item.price

        for card in price_of_item[:]:
            if card in temp_cards:
                temp_cards.remove(card)  # if fails remove
            else:
                return False

        return True


a = Shopping_helper("oho",77)

# select item -> pay -> update map. loop back


# buy_item(item:models.buyable_item,player)->buyable_item:
# should remove necessary cards from deck
# should create construction object with correct owner
# should placement be set?


# if player buy construction:

# find_possible_placements(contruciont:models.construction)->legal placements

# place on map(board:Board)
