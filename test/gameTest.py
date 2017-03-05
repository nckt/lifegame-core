#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/model')

import unittest
import game
import logging

class gameTest(unittest.TestCase) :

    def testInitField(self) :
        myGame = game.game()

        myGame.initField(3, 2)

        # Check field was created randomly with manpower (damn!)
        logging.basicConfig()
        log = logging.getLogger("LOG")
        log.warning(myGame.field)

        self.assertEqual(
            [ len(myGame.field[0]), len(myGame.field) ],
            [3, 2]
        )

    def testGetAroundLifeCount(self) :
        # ★ ○ ×
        # × ○ ×
        # × ○ ★
        #
        # ★...test target, ○...living cell, ×...dead cell
        # expects -> 2, 2

        field = [
            [False, True,  False],
            [False, True,  False],
            [False, True,  False]
        ]
        myGame = game.game(1, 1, field)

        self.assertEqual(
            [myGame.getAroundLifeCount(0, 0), myGame.getAroundLifeCount(2, 2)],
            [2, 2]
        )

    def testDeadCellsNextTurn(self) :
        # If 3 living cells exist around dead cell, birth living cell.
        # Otherwise, dead.
        #
        # [before]
        # × × ○
        # ○ × ○
        # × ○ ×
        #
        # [after]
        # × ○ ×
        # × × ○
        # × ○ ×

        field = [
            [False, False, True],
            [True,  False, True],
            [False, True,  False]
        ]

        nextTurnField = [
            [False, True,  False],
            [False, False, True],
            [False, True,  False]
        ]

        myGame = game.game(1, 1, field)
        myGame.nextTurn()

        self.assertEqual(
            myGame.step,
            2
        )
        self.assertEqual(
            myGame.field,
            nextTurnField
        )

    def testLivingCellsNextTurn(self) :
        # If 2 or 3 living cells exist around living cell, the cell survive.
        # Otherwise, dead.
        #
        # [before]
        # ○ × ○
        # × ○ ○
        # × ○ ×
        #
        # [after]
        # × × ○
        # ○ × ○
        # × ○ ○

        field = [
            [True,  False, True],
            [False, True,  True],
            [False, True,  False]
        ]

        nextTurnField = [
            [False, False, True],
            [True,  False, True],
            [False, True,  True]
        ]

        myGame = game.game(1, 1, field)
        myGame.nextTurn()

        self.assertEqual(
            myGame.step,
            2
        )
        self.assertEqual(
            myGame.field,
            nextTurnField
        )

if __name__ == "__main__":
    unittest.main()
