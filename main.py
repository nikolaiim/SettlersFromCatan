import models.game
import models.board
import models.player
import models.dices
import models.resource_card
import models.resource_types

import board_helpers





def main():
    num_rows = 2
    num_cols = 2

    board = board_helpers.generate_board(num_rows,num_cols)
    players = [models.player.Player("Nikolai",[])]
    game = models.game.Game(players,board)

    # start first-round-routine:
    ##select random player to start, all can set out two towns and two roads, as well as pick the resources

    while True: #loop over turns

        for player in game.players:

            #if player has knight in player.cards:
            ##player wants to play knight?

            dice_results = models.dices.Dices.throw()

            #if 7: start robber-routine

            #if not 7: start resource-distribution-routine:
            #loop over map to see what resources the players have "won" -> make function in/that work on ganme.board to see what resources dice_results give to whom

            #give players the resources -> update game.players

            #


            #calculate what constructions/dev-card player can buy

            #if player wants to buy construction:
            ##start shopping-routine:
            ###find possible locations
            ###player choose
            ###update game.board.constructions and player.cards

            ##count points and evaluate longes road and most knights



if __name__ == "__main__":
    main()