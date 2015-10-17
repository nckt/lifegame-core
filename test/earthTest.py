#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/model')

import unittest
import earth
import logging

class earthTest(unittest.TestCase) :

    def testInitEarth(self) :
        myEarth = earth.earth()

        myEarth.initField(3, 2)

        # Check field was created randomly with manpower (damn!)
        logging.basicConfig()
        log = logging.getLogger("LOG")
        log.warning(myEarth.field)

        self.assertEqual(
            [ len(myEarth.field[0]), len(myEarth.field) ],
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
        myEarth = earth.earth(1, 1, field)

        self.assertEqual(
            [myEarth.getAroundLifeCount(0, 0), myEarth.getAroundLifeCount(2, 2)],
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

        myEarth = earth.earth(1, 1, field)
        myEarth.nextTurn()

        self.assertEqual(
            myEarth.step,
            2
        )
        self.assertEqual(
            myEarth.field,
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

        myEarth = earth.earth(1, 1, field)
        myEarth.nextTurn()

        self.assertEqual(
            myEarth.step,
            2
        )
        self.assertEqual(
            myEarth.field,
            nextTurnField
        )

if __name__ == "__main__":
    unittest.main()
