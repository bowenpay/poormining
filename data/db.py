# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Float
from settings import DATABASE


DB_SESSION = None
Base = declarative_base()


def get_db_session():
    """
    获取数据库连接
    """
    global DB_SESSION
    if not DB_SESSION:
        # 初始化数据库连接:
        engine = create_engine('mysql+mysqlconnector://%s:%s@%s:%s/%s' % (
            DATABASE.get('USER'), DATABASE.get('PASSWORD'), DATABASE.get('HOST'),
            DATABASE.get('PORT', 3306), DATABASE.get('NAME'))
        )
        # 创建DBSession类型:
        DB_SESSION = sessionmaker(bind=engine)()
    return DB_SESSION


####################################################################
###### 数据库表 start

class PinkunhuBase(object):
    """ 贫困户表的父类 """
    sid = Column(String(50 ))
    id = Column(String(20), primary_key=True)
    # 住址
    province = Column(String(100))
    city = Column(String(100))
    county = Column(String(100))
    town = Column(String(100))
    village = Column(String(100))
    group = Column(String(100))
    # 基本情况
    name = Column(String(100))
    card_number = Column(String(100))
    call_number = Column(String(100))

    member_count = Column(Integer())
    bank_name = Column(String(100))
    bank_number = Column(String(100))
    standard = Column(String(100))
    reason = Column(String(100))
    other_reason = Column(String(100))
    is_back_poor = Column(String(100))
    poor_status = Column(String(100))
    # 生产生活条件
    arable_land = Column(Float())
    wood_land = Column(Float())
    living_space = Column(Float())
    is_danger_house = Column(String(50 ))
    is_debt = Column(String(50 ))
    debt_total = Column(Float())
    year_total_income = Column(Float())
    person_year_total_income = Column(Float())
    subsidy_total = Column(Float())
    xin_nong_he_total = Column(Float())
    xin_yang_lao_total = Column(Float())
    # 帮扶计划
    help_plan = Column(Text())
    # 五查无看
    tv = Column(String(50 ))
    washing_machine = Column(String(50))
    fridge = Column(String(50))

    ny_is_poor = Column(Integer()) # 下一年是否贫困, 1表示是，0表示否
    ny_total_income = Column(Float()) # 下一年年收入
    ny_person_income = Column(Float()) # 下一年人均年收入


class BangfurenBase(object):
    """ 帮扶人表的父类 """
    sid = Column(String(50 ))
    id = Column(String(20), primary_key=True)
    # 住址
    province = Column(String(100))
    city = Column(String(100))
    county = Column(String(100))
    town = Column(String(100))
    village = Column(String(100))
    group = Column(String(100))
    # 基本情况
    bangfu_name = Column(String(100))
    company = Column(String(200))
    company_name = Column(String(100))
    company_address = Column(String(100))
    relation = Column(String(100))
    call_number = Column(String(100))
    sex = Column(String(100))


class PinkunjiatingBase(object):
    """ 贫困家庭表的父类 """
    sid = Column(String(50 ))
    id = Column(String(20), primary_key=True)
    # 住址
    province = Column(String(100))
    city = Column(String(100))
    county = Column(String(100))
    town = Column(String(100))
    village = Column(String(100))
    group = Column(String(100))
    # 基本情况
    name = Column(String(100 ))
    card_number = Column(String(100))
    member_name = Column(String(100 ))
    member_card_number = Column(String(100))
    sex = Column(String(100))
    relation = Column(String(100))
    nation = Column(String(100))
    education = Column(String(100))
    edu_status = Column(String(100))
    health = Column(String(100))
    work_ability = Column(String(100))
    work_status = Column(String(100))
    work_time = Column(String(100))
    xin_nong_he = Column(String(100))
    xin_yang_lao = Column(String(100))
    dabing_yiliao = Column(String(100))
    fuchi_fangshi = Column(String(100))
    change_type = Column(String(100))
    change_reason = Column(String(100))
    age = Column(Integer())


class Bangfuren2014(BangfurenBase, Base):
    """ 2014年帮扶人表 """
    __tablename__ = 'yunnan_all_bangfuren_2014'


class Bangfuren2015(BangfurenBase, Base):
    """ 2015年帮扶人表 """
    __tablename__ = 'yunnan_all_bangfuren_2015'


class Bangfuren2016(BangfurenBase, Base):
    """ 2016年帮扶人表 """
    __tablename__ = 'yunnan_all_bangfuren_2016'


class Pinkunhu2014(PinkunhuBase, Base):
    """ 2014年贫困户表 """
    __tablename__ = 'yunnan_all_pinkunhu_2014'


class Pinkunhu2015(PinkunhuBase, Base):
    """ 2015年贫困户表 """
    __tablename__ = 'yunnan_all_pinkunhu_2015'


class Pinkunhu2016(PinkunhuBase, Base):
    """ 2016年贫困户表 """
    __tablename__ = 'yunnan_all_pinkunhu_2016'


class Pinkunjiating2014(PinkunjiatingBase, Base):
    """ 2014年贫困家庭表 """
    __tablename__ = 'yunnan_all_pinkunjiating_2014'


class Pinkunjiating2015(PinkunjiatingBase, Base):
    """ 2015年贫困家庭表 """
    __tablename__ = 'yunnan_all_pinkunjiating_2015'


class Pinkunjiating2016(PinkunjiatingBase, Base):
    """ 2016年贫困家庭表 """
    __tablename__ = 'yunnan_all_pinkunjiating_2016'

###### 数据库表 end
####################################################################




