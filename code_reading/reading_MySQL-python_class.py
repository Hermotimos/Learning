"""
    This code was copied for learning purposes. All comments were added in the process of understanding.

    Source:
        https://github.com/nestordeharo/mysql-python-class/blob/master/mysql_python.py#L2
"""

#!/usr/bin/env python
# coding=utf-8

import MySQLdb, sys
from collections import OrderedDict


class MysqlPython(object):

    __instance   = None
    __host       = None
    __user       = None
    __password   = None
    __database   = None
    __session    = None
    __connection = None
    # class variables;
    # name mangling (__variable): variables are not overwritten when another variable 'instance', 'host' etc. occurs
    # due to name mangling these are actually named _MysqlPython__instance, _MysqlPython__host etc.

    def __new__(cls, *args, **kwargs):
        if not cls.__instance or not cls.__database:
            cls.__instance = super(MysqlPython, cls).__new__(cls, *args, **kwargs)
        return cls.__instance
        # __new__ creates new instance of class and implicitly passes it('cls') to __init__ (where 'cls' becomes 'self')
        # here overwritten ==> if __instance == None or __database == None, it recursively calls itself as superclass
        # todo why? does this only serve for sublasses to inherit (as __database is given value right next in __init__)

    def __init__(self, host='localhost', user='root', password='', database=''):
        self.__host     = host
        self.__user     = user
        self.__password = password
        self.__database = database

    def __open(self):
        # opens connection do db with cursor
        # name mangling applied to method to hide it from users of this class
        try:
            cnx = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
            self.__connection = cnx
            self.__session    = cnx.cursor()
        except MySQLdb.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            # %d for digit, %s for string extracted from e; but why is e iterable? is it error message as tuple/list?

    def __close(self):
        self.__session.close()          # closes cursor
        self.__connection.close()       # closes connection

    def select(self, table, where=None, *args, **kwargs):
        result = None
        query = 'SELECT '
        keys = args                         # *args is tuple => keys is tuple
        values = tuple(kwargs.values())     # **kwargs keys become tuple => values is tuple
        lngth = len(keys) - 1               # CHANGED variable l to lngth (was ambiguous PEP8)

        for i, key in enumerate(keys):      # this constructs what follows after SELECT i.e. columns or expressions
            query += "`"+key+"`"            # this loop adds to the query each one of *args (here as keys)
            if i < lngth:                   # in the format: `arg` (back-quotes call repr() on it => make it a str)
                query += ","                # is similar to: query += str(key) but calls __repr__() instead of __str__()
                                            # so it gives str: 'SELECT arg1,arg2,argN'
        query += 'FROM %s' % table

        if where:
            query += " WHERE %s" % where

        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]
        self.__close()

        return result

    def update(self, table, where=None, *args, **kwargs):
        query  = "UPDATE %s SET " % table
        keys   = kwargs.keys()
        values = tuple(kwargs.values()) + tuple(args)
        l = len(keys) - 1
        for i, key in enumerate(keys):
            query += "`"+key+"` = %s"
            if i < l:
                query += ","
        query += " WHERE %s" % where

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()

        update_rows = self.__session.rowcount
        self.__close()

        return update_rows

    def insert(self, table, *args, **kwargs):
        values = None
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) % tuple(keys) + ") VALUES (" + ",".join(["%s"]*len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()
        self.__close()
        return self.__session.lastrowid

    def delete(self, table, where=None, *args):
        query = "DELETE FROM %s" % table
        if where:
            query += ' WHERE %s' % where

        values = tuple(args)

        self.__open()
        self.__session.execute(query, values)
        self.__connection.commit()

        delete_rows = self.__session.rowcount
        self.__close()

        return delete_rows

    def select_advanced(self, sql, *args):
        od = OrderedDict(args)
        query  = sql
        values = tuple(od.values())
        self.__open()
        self.__session.execute(query, values)
        number_rows = self.__session.rowcount
        number_columns = len(self.__session.description)

        if number_rows >= 1 and number_columns > 1:
            result = [item for item in self.__session.fetchall()]
        else:
            result = [item[0] for item in self.__session.fetchall()]

        self.__close()
        return result


db = MysqlPython(password=input('Password:\n'), database='evaluations')
db.select()
