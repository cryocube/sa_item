#!/usr/bin/env python3
# Shadow Accord Item for creating Magic Item Loadouts
#
# Original Author: Kyle Ricks
# Organization: Shadow Accord - NW LARPers
#
# Imports
#
import sys
import sqlite3
#
#
##############################################
# Classes and Functions                      #
##############################################
class DB_Functions:
    """Functions to be called from the Menu."""

    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
#
#
class Type_Menu:
    def __init__(self, db):
            self.db = db
    def prompt(self):
        selection = input("Please select what type of Item use you would like.\n\t[1] worn\n\t[2] carried\n\t[3] armor\n\t[4] weapon\n\n")
        return selection
    def selector(self, selection):
        if selection == '1':
            item_type_id = 1
            return item_type_id
        elif selection == '2':
            item_type_id = 2
            return item_type_id
        elif selection == '3':
            item_type_id = 3
            return item_type_id
        elif selection == '4':
            item_type_id = 4
            return item_type_id
        else:
            print("You have not selected a valid option.  Please select again.")
            sel = Type_Menu(db).prompt()
            self.selector(sel)

##############################################
# Actual Program                             #
##############################################
if __name__ == "__main__":
    db = DB_Functions('item_properties.db3')
# Database Connection
# https://docs.python.org/3.5/library/sqlite3.html
    sel = Type_Menu(db).prompt()
    Type_Menu(db).selector(sel)
