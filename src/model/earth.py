#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import random

class earth :
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
        # debug #
        print("======")
        # debug #
        count = 0

        for y in range(argY - 1, argY + 2) :
            for x in range(argX - 1, argX + 2):
                # debug #
                print([x,y])
                # debug #
                if y == argY and x == argX :
                    # debug #
                    print("skip!")
                    # debug #
                    continue

                if self.__isLiving(x, y) :
                    # debug #
                    print("living. count++")
                    # debug #
                    count += 1

                # debug #
                print("-----")
                # debug #
        return count

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
