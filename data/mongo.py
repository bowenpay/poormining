# -*- coding: utf-8 -*-
from pymongo import MongoClient
from settings import MONGODB

DB = None


def get_db():
    """
    获取mongodb的client连接
    :return:
    """
    global DB
    if not DB:
        client = MongoClient(MONGODB.get('HOST', '127.0.0.1'), MONGODB.get('PORT', 27017))
        DB = client[MONGODB.get('NAME')]
        user, password = MONGODB.get('USER', ''), MONGODB.get('PASSWORD', '')
        if user or password:
            DB.authenticate(user, password)

    return DB

if __name__ == '__main__':
    db = get_db()
    for item in db.families.find():
        print item



