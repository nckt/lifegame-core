#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

class earth :
"""
Life game field.
"""
    def __init__(self, generation, step, width, height) :
        """
        Constructor. Create field randomly from size parameter.

        @param self
        @param int generation
        @param int step
        @param int width  Field width.
        @param int height Field height.
        """

        self.generation = generation
        self.step       = step
        self.field      = []

        # Create field randomly.
        for y in range(height) :
            self.field.append([])

            for x in range(width) :
                self.field[y].append( bool( random.getrandbits(1) ) )

    def __init__(self, generation, step, field) :
        """
        Constructor. Create field from parameter.

        @param self
        @param int  generation
        @param int  step
        @param list field
        """

        self.generation = generation
        self.step       = step
        self.field      = field

    def getAroundLifeCount(argX, argY) :
        """
        Count living around received coordinate.

        @param  int x coordinate.
        @param  int y coordinate.
        @return int Count.
        """

        count = 0

        for y in range(argY - 1, 3) :
            for x in range(argX - 1, 3):
                if y == argY and x == argX :
                    continue

                if __isLiving(x, y) :
                    count++

        return count

    def __isLiving(x, y) :
        """
        If received coordinate life is living, returns true.

        @param  int  x coordinate.
        @param  int  y coordinate.
        @return bool Is living?
        """

        # invalid parameter.
        if y < 0 or x < 0 or len(self.field) < y or len(self.field[y]) < x :
            return false

        return self.field[y][x]
