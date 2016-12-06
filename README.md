对贫困户2015年~2016年的信息，进行挖掘分析

# 模块介绍

data： 数据来源。定义访问数据库的schemal 和 获取数据的方法。

machinglearning： 各种机器学习的模型。 

stats： 数据统计。

# 安装

1) clone本工程，并进入到文件夹内，执行 `pip install -r requirements.txt` 安装依赖包.

2) 为了解决matplotlib中文乱码问题， 需要打开 `<PATH>/site-packages/matplotlib/mpl-data/matplotlibrc` 文件，
删除 `font.family` 和 `font.sans-serif` 两行前的 `#`，并在 `font.sans-serif` 后添加微软雅黑字体（Microsoft YaHei），代码如下：

    font.family         : sans-serif
    font.sans-serif     : Microsoft YaHei, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

3) 创建数据库

使用下面的语句创建数据库

    mysql> CREATE DATABASE `data_fupin` CHARACTER SET utf8;

并将 `./data/*.sql` 文件导入到数据库中

4) 更新配置文件local_settings

在 poormining 目录下,添加 local_settings.py 文件,修改对应的用户名密码，配置如下:

    # -*- coding: utf-8 -*-
    
    DATABASE = {
            'HOST': '127.0.0.1',
            'NAME': 'data_fupin',
            'USER': 'root',
            'PASSWORD': '123456',
            'OPTIONS': {
                'charset': 'utf8mb4',
            }
    }

# 执行

## 生成特征图

执行命令 `python stats/factor.py`, 会在 `stats/images/` 下面生成贫困户、已脱贫贫困户、已脱贫占总贫困户比的单因子影响图。

如果想添加跟多的因子，请修改 `stats/factor.py` 中 类`PinkunhuCharacter` 的 `run` 方法。

## 使用随机森林模型预测

## 使用逻辑回归预测

## 其它







