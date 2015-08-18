#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/model')

import unittest
import earth
import logging

class testEarth(unittest.TestCase) :

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
        # ★...test target, ○...living cell, ×...dead cesll
        # expects -> 2, 2

        field = [
            [False, True,  False],
            [False, True,  False],
            [False, True,  False]
        ]
        myEarth = earth.earth(0, 0, field)

        self.assertEqual(
            [myEarth.getAroundLifeCount(0, 0), myEarth.getAroundLifeCount(2, 2)],
            [2, 2]
        )

if __name__ == "__main__":
    unittest.main()
