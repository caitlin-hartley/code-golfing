# DESCRIPTION:
# In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:

# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# Rock crushes Scissors
# Task:
# Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".

# Inputs
# Values will be given as one of "rock", "paper", "scissors", "lizard", "spock".

def rpsls(pl1, pl2):
    if pl1 == pl2:
        return ("Draw!")
    elif (pl1 == "rock" and (pl2 == "lizard" or pl2=="scissors")) or \
    (pl1 == "scissors" and (pl2 == "paper" or pl2 == "lizard")) or \
    (pl1 == "lizard" and (pl2 == "spock" or pl2 == "paper")) or \
    (pl1 == "spock" and (pl2 == "scissors" or pl2 == "rock")) or \
    (pl1 == "paper" and (pl2 == "rock" or pl2 == "spock")):
        return ("Player 1 Won!")
    else:
        return("Player 2 Won!")

import codewars_test as test


@test.describe('rock paper scissors lizard spock')
def test():
    @test.it('Player 1 Won!')
    def _():
        test.assert_equals(rpsls('rock', 'lizard'), 'Player 1 Won!')
        test.assert_equals(rpsls('paper', 'rock'), 'Player 1 Won!')