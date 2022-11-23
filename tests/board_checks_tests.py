import unittest
import sys

sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")

import models
from actions import board_actions
from checks import board_checks


class Shopping_routine_tests(unittest.TestCase):
    board = models.board.Board(board_actions.BoardActions.generate_board(10, 10),[models.constructions.City(None,[(2,1),(3,1),(3,2)])])
    def test_town_too_close_detected1(self):
        construction_placement=[(3,1),(3,2),(4,2)]
        res = board_checks.BoardChecks.is_construction_too_close(self.board,construction_placement)
        self.assertTrue(res)

    def test_town_too_close_detected2(self):
        construction_placement=[(2,1),(2,2),(3,2)]
        res = board_checks.BoardChecks.is_construction_too_close(self.board,construction_placement)
        self.assertTrue(res)

    def test_town_too_close_detected3(self):
        construction_placement=[(2,1),(3,1),(3,1)]
        res = board_checks.BoardChecks.is_construction_too_close(self.board,construction_placement)
        self.assertTrue(res)

    def test_not_town_too_close_detected(self):
        construction_placement=[(2,2),(1,3),(2,3)]
        res = board_checks.BoardChecks.is_construction_too_close(self.board,construction_placement)
        self.assertFalse(res)

    def test_does_player_have_connecting_road_to_coordinate(self):
        construction_placement=[(2,2),(1,3),(2,3)]
        player = models.Player("name",models.Card_collection([]))

        board_checks.BoardChecks.does_player_have_connecting_road_to_coordinate(self.board,player,construction_placement,is_first_round=True)




if __name__ == '__main__':
    unittest.main()
