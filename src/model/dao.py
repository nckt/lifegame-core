#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import pymongo
import json

class dao :
    """
    Database accesor.
    """

    def __init__(self, configPath = "../../config/config.json") :
        """
        Constructor.

        @param String Config file path.
        """
        self.dbName
        self.host
        self.user
        self.password
        self.mongoClient
        self.db

        self.configPath = configPath
        self.__loadConfig()

    def __loadConfig(self) :
        """
        Load config file.
        """
        fh = open(configPath, "r")

        config = json.load(fh)

        self.dbName = config["db"]["db"]
        self.host = config["db"]["host"]
        self.user = config["db"]["user"]
        self.password = config["db"]["password"]

        fh.close()

    def connect(self) :
        """
        Connect to database.
        """
        connectString = "mongodb://%s:%s@%s" % (self.user, self.password, self.host)
        self.mongoClient = MongoClient(connectString)
        self.db = self.mongoClient[self.dbName]

    def disconnect(self) :
        """
        Disconnect to database.
        """
        self.mongoClient.close()
