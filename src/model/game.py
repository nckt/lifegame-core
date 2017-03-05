#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import random

class game :
    """
    Life game field.
    """
    def __init__(self, generation = 1, step = 1, field = []) :
        """
        Constructor.

        @param int  generation
        @param int  step
        @param list field
        """

        self.generation = generation
        self.step       = step
        self.field      = field

    def initField(self, width, height) :
        """
        Create field randomly from size parameter.

        @param int field width.
        @param int field height.
        """

        for y in range(height) :
            self.field.append([])

            for x in range(width) :
                self.field[y].append( bool( random.getrandbits(1) ) )

    def getAroundLifeCount(self, argX, argY) :
        """
        Count living around received coordinate.

        @param  int x coordinate.
        @param  int y coordinate.
        @return int Count.
        """

        count = 0

        for y in range(argY - 1, argY + 2) :
            for x in range(argX - 1, argX + 2):
                if y == argY and x == argX :
                    continue

                if self.__isLiving(x, y) :
                    count += 1

        return count

    def nextTurn(self) :
        """
        Progress turn.
        """

        nextField = []
        height = len(self.field)
        width = len(self.field[0])

        for y in range(0, height) :
            nextField.append([])

            for x in range(0, width) :
                if self.__isLiving(x, y) :
                    # Living pattern
                    if self.getAroundLifeCount(x, y) == 2 or self.getAroundLifeCount(x, y) == 3 :
                        nextField[y].append(True)
                    else :
                        nextField[y].append(False)
                else :
                    # Dead pattern
                    if self.getAroundLifeCount(x, y) == 3 :
                        nextField[y].append(True)
                    else :
                        nextField[y].append(False)

        self.field = nextField
        self.step += 1

    def __isLiving(self, x, y) :
        """
        If received coordinate life is living, returns true.

        @param  int  x coordinate.
        @param  int  y coordinate.
        @return bool Is living?
        """

        # invalid parameter.
        if y < 0 or x < 0 or len(self.field) <= y or len(self.field[y]) <= x :
            return False

        return self.field[y][x]
