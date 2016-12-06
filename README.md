对贫困户的信息，进行挖掘分析

# 模块介绍

```
--.
  ├── data/               数据来源。定义访问数据库的schemal 和 获取数据的方法。
  ├── machinelearning/    各种机器学习的模型。
  │   ├── __init__.py
  │   ├── randomforest
  │   ├── logistic
  │   └── svm
  └── stats/              数据统计
```


# 安装

##### 1）安装python环境 

检查python的版本，是否为2.7.x，如果不是，安装2.7.6。


##### 2）安装依赖包, clone代码

安装Mysql-python依赖
    
    $ yum install python-devel mysql-devel gcc

clone代码,安装依赖python库

    $ git clone https://github.com/bowenpay/poormining.git
    $ cd poormining
    $ pip install -r requirements.txt

##### 3) 解决 `matplotlib` 中文乱码问题

打开 `<PATH>/site-packages/matplotlib/mpl-data/matplotlibrc` 文件，
删除 `font.family` 和 `font.sans-serif` 两行前的 `#`，并在 `font.sans-serif` 后添加微软雅黑字体（Microsoft YaHei），代码如下：

    font.family         : sans-serif
    font.sans-serif     : Microsoft YaHei, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif

##### 4) 创建数据库

使用下面的语句创建数据库

    mysql> CREATE DATABASE `data_fupin` CHARACTER SET utf8;

并将 `./data/*.sql` 文件导入到数据库中

##### 5) 更新配置文件local_settings

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

如果想添加跟多的因子，请修改 `stats/factor.py` 中 类`PinkunhuCharacter` 的 `run` 方法。 如下所示

```python
class PinkunhuCharacter(object):
    """ 贫困户特征
    """
    def run(self):
        for col in ['member_count', 'is_debt']:   # 在list中添加想要的因子
            self.stat_col_percent(col)
```

## 使用随机森林模型预测

## 使用逻辑回归预测

## 其它







