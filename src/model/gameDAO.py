#!/usr/bin/env python

__author__ = "nckt <galikuson@gmail.com>"

import dao
from datetime import datetime

class earthDAO(dao) :
    """
    Database accesor to save or load field.
    """

    def saveCurrent(self, earth) :
        """
        Save current field.

        @param Dictionary Return of earth.toDict()
        """
        self.db.current.update_one({}, earth, True)

    def record(self) :
        """
        Copy current to record.
        """
        current = self.db.current.find()
        current["logDateTime"] = datetime.now()

        self.db.record.insert_one(current)

    def getCurrent(self) :
        """
        Get current field.

        @return Dictionary Current field
        """
        return self.db.current.find()
