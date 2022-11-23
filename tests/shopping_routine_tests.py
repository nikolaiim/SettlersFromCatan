import unittest
import sys

sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")

import models
import routines
from  resource_helpers import get_resource_cards

class Shopping_routine_tests(unittest.TestCase):

    def test_roadresources_can_afford_only_road(self):
        player1 = models.Player("This is a name",models.Card_collection(get_resource_cards(1,0,0,0,1)))
        helper = routines.Shopping_helper()

        items = helper.what_can_player_afford(player1.cards)
        self.assertEqual(items,[models.constructions.Road()])
        
    def test_tworoadresources_can_afford_only_road(self):
        player1 = models.Player("This is a name",models.Card_collection(get_resource_cards(2,0,0,0,2)))
        helper = routines.Shopping_helper()

        items = helper.what_can_player_afford(player1.cards)
        self.assertEqual(items,[models.constructions.Road()])
        
    def test_cityresources_can_afford_only_city(self):
        player1 = models.Player("This is a name",models.Card_collection(get_resource_cards(0,3,0,2,0)))
        helper = routines.Shopping_helper()

        items = helper.what_can_player_afford(player1.cards)
        self.assertEqual(items,[models.constructions.City()])

    def test_devcardresources_can_afford_only_devcard(self):
        player1 = models.Player("This is a name",models.Card_collection(get_resource_cards(0,1,1,1,0)))
        helper = routines.Shopping_helper()

        items = helper.what_can_player_afford(player1.cards)
        self.assertEqual(items,[models.development_card.Development_card()])


if __name__ == '__main__':
    unittest.main()