# -*- coding: utf-8 -*-
__author__ = 'yijingping'
from data.db import get_db_session, Pinkunhu2015
from matplotlib import pyplot as plt
import numpy as np


def myplot(x, y, nb=32, xsize=500, ysize=500):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=nb)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent


def chart_person_year_total_income():
    # 获取数据
    session = get_db_session()
    objs = session.query(Pinkunhu2015.person_year_total_income, Pinkunhu2015.ny_person_income).filter(
            Pinkunhu2015.county == 'A县',
            Pinkunhu2015.ny_person_income >= -1, Pinkunhu2015.ny_person_income < 7000,
            Pinkunhu2015.person_year_total_income > 0, Pinkunhu2015.person_year_total_income < 7000,
    ).all()
    X, Y = [], []
    for item in objs:
        X.append(item.person_year_total_income)
        Y.append(item.ny_person_income if item.ny_person_income != -1 else -1000)
    # 绘图
    fig = plt.figure(1, figsize=(10, 10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    # 画点图
    ax1.plot(X, Y, 'k.', markersize=2)

    # 画热力图
    heatmap_16, extent_16 = myplot(X, Y, nb=16)
    heatmap_32, extent_32 = myplot(X, Y, nb=32)
    heatmap_64, extent_64 = myplot(X, Y, nb=64)

    ax2.imshow(heatmap_16, extent=extent_16, origin='lower', aspect='auto')
    ax2.set_title("Smoothing over 16 neighbors")

    ax3.imshow(heatmap_32, extent=extent_32, origin='lower', aspect='auto')
    ax3.set_title("Smoothing over 32 neighbors")

    #Make the heatmap using a smoothing over 64 neighbors
    ax4.imshow(heatmap_64, extent=extent_64, origin='lower', aspect='auto')
    ax4.set_title("Smoothing over 64 neighbors")

    plt.show()


def chart_year_total_income():
    # 获取数据
    session = get_db_session()
    objs = session.query(Pinkunhu2015.year_total_income, Pinkunhu2015.ny_total_income).filter(
            Pinkunhu2015.county == 'A县',
            Pinkunhu2015.year_total_income >= -1, Pinkunhu2015.year_total_income < 70000,
            Pinkunhu2015.ny_total_income > -1, Pinkunhu2015.ny_total_income < 70000
    ).all()
    X, Y = [], []
    for item in objs:
        X.append(item.year_total_income)
        Y.append(item.ny_total_income if item.ny_total_income != -1 else -500)
    # 绘图
    fig = plt.figure(1, figsize=(10, 10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    # 画点图
    ax1.plot(X, Y, 'k.', markersize=2)

    # 画热力图
    heatmap_16, extent_16 = myplot(X, Y, nb=16)
    heatmap_32, extent_32 = myplot(X, Y, nb=32)
    heatmap_64, extent_64 = myplot(X, Y, nb=64)

    ax2.imshow(heatmap_16, extent=extent_16, origin='lower', aspect='auto')
    ax2.set_title("Smoothing over 16 neighbors")

    ax3.imshow(heatmap_32, extent=extent_32, origin='lower', aspect='auto')
    ax3.set_title("Smoothing over 32 neighbors")

    #Make the heatmap using a smoothing over 64 neighbors
    ax4.imshow(heatmap_64, extent=extent_64, origin='lower', aspect='auto')
    ax4.set_title("Smoothing over 64 neighbors")

    plt.show()


if __name__ == '__main__':
    chart_year_total_income()
