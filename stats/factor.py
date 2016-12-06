# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'yijingping'
from data.db import get_db_session, Pinkunhu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


def autolabel(ax, rects):
    """ 给柱状图的每一个柱加上label
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')


class PinkunhuCharacter(object):
    """ 贫困户特征
    """
    def run(self):
        for col in ['washing_machine', 'tv', 'fridge']:
            self.stat_col_percent(col)

    def plot_col_name(self, data, title):
        fig = plt.figure()
        fig.patch.set_facecolor('white')
        ax1 = fig.add_subplot(1, 1, 1)
        labels = [item[0] for item in data]
        values = [item[1] for item in data]
        index = np.arange(len(labels))
        bar_width = 0.4
        opacity = 0.4
        rects = plt.bar(index, values, bar_width, alpha=opacity, color='b', label=title)
        autolabel(ax1, rects)
        plt.xticks(index + bar_width / 2, labels, rotation=-45)
        plt.legend()
        # 显示
        # plt.show()
        # 存储到images文件夹
        fpath = os.path.join(os.path.dirname(__file__), 'images', '%s.png' % title)
        plt.savefig(fpath)


    def count_to_percent(self, cnt_dict):
        total = sum(cnt_dict.values())
        res = []
        for k, v in cnt_dict.iteritems():
            v2 = float('%.2f' % (v * 100.0 / total))
            res.append((k, v2))
        res = sorted(res, key=lambda x:-x[1])
        return res

    def stat_col_percent(self, col):
        top_num = 10
        session = get_db_session()
        objs = session.query(getattr(Pinkunhu, col)).filter(Pinkunhu.poor_status != '已脱贫')
        res0 = {}
        for item in objs:
            k = (getattr(item, col) or '')[:2]
            cnt = res0.get(k, 0)
            res0[k] = cnt + 1

        self.plot_col_name(self.count_to_percent(res0)[:20], title='%s-未脱贫' % col)

        objs = session.query(getattr(Pinkunhu, col))
        res1 = {}
        for item in objs:
            k = (getattr(item, col) or '')[:2]
            cnt = res1.get(k, 0)
            res1[k] = cnt + 1

        self.plot_col_name(self.count_to_percent(res1)[:20], title='%s-全部' % col)

        objs2 = session.query(getattr(Pinkunhu, col)).filter(Pinkunhu.poor_status=='已脱贫')
        res2 = {}
        for item in objs2:
            k = (getattr(item, col) or '')[:2]
            cnt = res2.get(k, 0)
            res2[k] = cnt + 1

        self.plot_col_name(self.count_to_percent(res2)[:20], title='%s-已脱贫' % col)

        res = []
        for k, v in res1.iteritems():
            print k
            res.append((k, res2.get(k, 0) * 100.0 / v))

        res = sorted(res, key=lambda x: -x[1])
        result = []
        for item in res:
            if res2.get(item[0]) > 200:
                result.append(('%s (%s户)' % (item[0], res2.get(item[0])), item[1]))

        self.plot_col_name(result[:top_num], title='%s-百分比' % col)


if __name__ == '__main__':
    t = PinkunhuCharacter()
    t.run()
