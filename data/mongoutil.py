# -*- coding: utf-8 -*-
from data.db import *
from data.mongo import get_db
from sqlalchemy.sql import func
from sqlalchemy import inspect

def init_mongo_from_mysql():
    """
    用mysql中的数据初始化mongodb，格式如下：
    families：
        [
            {
                family_id: 123456,
                2014: {
                        bangfuren: {},
                        pinkunhu: {},
                        pinkunjiating: []
                      },

                2015: {
                        bangfuren: {},
                        pinkunhu: {},
                        pinkunjiating: []
                      },

                2016: {
                        bangfuren: {},
                        pinkunhu: {},
                        pinkunjiating: []
                      },

                features: {}
            },
        ......
        ]
    """
    pass


def init_table(table, year, kind):
    """
    初始化表
    :param table:
    :param year:
    :param kind:
    :return:
    """
    step = 100 # 一次取100条数据
    session = get_db_session()
    mongo = get_db()
    # 2016年数据
    mappings2016 = {}
    min_id, max_id = session.query(func.min(table.id), func.max(table.id)).one()
    if not min_id: return
    min_id -= 1
    min_id = 2543595
    while min_id < max_id:
        objs = session.query(table).filter(table.id > min_id).limit(step)
        for item in objs:
            min_id = item.id
            fid = item.sid
            data = {}
            for col in inspect(table).attrs:
                data[col.key] = getattr(item, col.key)

            print fid
            print '-------------------------'
            if kind in ['bangfuren', 'pinkunhu']:
                mongo.families.update(
                        {'family_id': fid},
                        {'$set':
                            {
                                '%s.%s' % (year, kind): data
                            }
                        },
                        upsert=True
                )
            elif kind in ['pinkunjiating']:
                mongo.families.update(
                        {'family_id': fid},
                        {'$push':
                            {
                                '%s.%s' % (year, kind): data
                            }
                        },
                        upsert=True
                )


        print 'min_id:%s' % min_id


if __name__ == '__main__':
    # init_table(Bangfuren2014, 2014, 'bangfuren')
    # init_table(Bangfuren2015, 2015, 'bangfuren')
    # init_table(Bangfuren2016, 2016, 'bangfuren')
    #
    # init_table(Pinkunhu2014, 2014, 'pinkunhu')
    # init_table(Pinkunhu2015, 2015, 'pinkunhu')
    # init_table(Pinkunhu2016, 2016, 'pinkunhu')

    # init_table(Pinkunjiating2014, 2014, 'pinkunjiating')
    init_table(Pinkunjiating2015, 2015, 'pinkunjiating')
    init_table(Pinkunjiating2016, 2016, 'pinkunjiating')

