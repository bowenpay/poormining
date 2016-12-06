# -*- coding: utf-8 -*-
from data.db import get_db_session, ZhenxiongPinkunhu2015, Pinkunhu
from sklearn.ensemble import RandomForestClassifier
import trees
import treePlotter


class RandomForestModel(object):
    """使用随机森林模型"""

    def run(self):
        # 获取数据
        data, labels = self.fetch_data()
        # 构建决策树
        my_tree = trees.createTree(data, labels)
        print my_tree
        # 绘制决策树
        # TODO 因为节点过多，暂时不绘制
        # treePlotter.createPlot(my_tree)
        # 保存决策树
        # trees.storeTree(my_tree, 'tree.txt')
        # my_tree = trees.grabTree('tree.txt')
        # 用决策树进行预测
        self.predict(my_tree)

    def fetch_data(self):
        """ 获取数据 """
        session = get_db_session()
        objs = session.query(ZhenxiongPinkunhu2015).limit(20)
        labels = [
           # 'province', 'city', 'county', 'town', 'village', 'group',
            'last_name', 'has_bank', 'has_phone',
            'member_count', 'standard', 'reason', 'other_reason',
        ]
        data = []
        for item in objs:
            data.append([
               # item.province, item.city, item.county, item.town, item.village, item.group,
                item.name[:1], '有银行卡' if item.bank_name else '无银行卡', '有电话' if item.call_number else '无电话',
                item.member_count, item.standard, item.reason, item.other_reason,
                item.poor_status
            ])
        return data, labels

    def fetch_test_data(self):
        """ 获取测试数据 """
        session = get_db_session()
        objs = session.query(Pinkunhu).filter(Pinkunhu.county == '陆良县').limit(1000)
        # objs = session.query(ZhenxiongPinkunhu2015).limit(1000)
        lables = [
           #  'province', 'city', 'county', 'town', 'village', 'group',
            'last_name', 'has_bank', 'has_phone',
            'member_count', 'standard', 'reason', 'other_reason',
        ]
        data = []
        for item in objs:
            data.append([
               #  item.province, item.city, item.county, item.town, item.village, item.group,
                item.name[:1], '有银行卡' if item.bank_name else '无银行卡', '有电话' if item.call_number else '无电话',
                item.member_count, item.standard, item.reason, item.other_reason,
                item.poor_status
            ])
        return data, lables

    def predict(self, my_tree):
        total, hit = 0, 0
        test_data, labels = self.fetch_test_data()
        for row in test_data:
            res = trees.classify(my_tree, labels, row[:-1])
            if res == row[-1]:
                hit += 1
            total += 1

        print 'Total: %d, Hit: %d, Precision: %.2f' % (total, hit, 100.0*hit/total)


if __name__ == '__main__':
    m = RandomForestModel()
    m.run()

