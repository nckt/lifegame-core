#!/usr/bin/env python

# !!! You should create config file as test/testConf.json !!!

__author__ = "nckt <galikuson@gmail.com>"

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src/model')

import unittest
import earthDAO
import earth

class earthDAOTest(unittest.TestCase) :
    def setUp(self) :
        self.dao = earthDAO.earthDAO("../../test/testConf.json")
        self.dao.connect()

    def tearDown(self) :
        self.dao.disconnect()

    def testSaveCurrent(self) :
        myEarth = earth.earth(1, 1, [[True, False], [False, True]])
        self.dao.saveCurrent

if __name__ == "__main__":
    unittest.main()
