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

执行命令 

    $ PYTHONPATH=. python stats/factor.py

会在 `stats/images/` 下面生成贫困户、已脱贫贫困户、已脱贫占总贫困户比的单因子影响图。

如果想添加跟多的因子，请修改 `stats/factor.py` 中 类`PinkunhuCharacter` 的 `run` 方法。 如下所示

```python
class PinkunhuCharacter(object):
    """ 贫困户特征
    """
    def run(self):
        for col in ['member_count', 'is_debt']:   # 在list中添加想要的因子
            self.stat_col_percent(col)
```

## 使用随机森林模型预测是否脱贫

执行命令

    $ PYTHONPATH=. python machinelearning/randomforest/model.py


会打印出

    Total: 48378, Hit: 47494, Precision: 98.17%

表示对48378个数据进行检测， 命中47494个， 命中率是 98.17%.

## 使用线性回归模型预测下一年人均年收入

在使用前，先做一个定义：

    误差率 = | (真实值 - 预测值) / 真实值 |

如果预测值在允许的误差范围内，即

    |真实值| * (1 - 误差率) <= |预测值| <= |真实值| * (1 + 误差率)

就算预测准确。

下面，开始执行命令

    $ PYTHONPATH=. python machinelearning/linearregression/model.py

会打印出

    Deviation: 0%, Total: 40820, Hit: 0, Precision: 0.00%
    Deviation: 10%, Total: 40820, Hit: 24418, Precision: 59.82%
    Deviation: 20%, Total: 40820, Hit: 32935, Precision: 80.68%
    Deviation: 30%, Total: 40820, Hit: 36211, Precision: 88.71%
    Deviation: 40%, Total: 40820, Hit: 37367, Precision: 91.54%
    Deviation: 50%, Total: 40820, Hit: 38041, Precision: 93.19%
    Deviation: 60%, Total: 40820, Hit: 38502, Precision: 94.32%
    Deviation: 70%, Total: 40820, Hit: 38816, Precision: 95.09%
    Deviation: 80%, Total: 40820, Hit: 39071, Precision: 95.72%
    Deviation: 90%, Total: 40820, Hit: 39282, Precision: 96.23%
    Deviation: 100%, Total: 40820, Hit: 39432, Precision: 96.60%

表示的意思是：
    
    误差率小于等于0%时，对40820个数据进行检测， 命中0个， 命中率是 0.00%
    误差率小于等于10%时，对40820个数据进行检测， 命中24418个， 命中率是 59.82%
    误差率小于等于20%时，对40820个数据进行检测， 命中32935个， 命中率是 80.68%
    误差率小于等于30%时，对40820个数据进行检测， 命中36211个， 命中率是 88.71%
    误差率小于等于40%时，对40820个数据进行检测， 命中37367个， 命中率是 91.54%
    误差率小于等于50%时，对40820个数据进行检测， 命中38041个， 命中率是 93.19%
    误差率小于等于60%时，对40820个数据进行检测， 命中38502个， 命中率是 94.32%
    误差率小于等于70%时，对40820个数据进行检测， 命中38816个， 命中率是 95.09%
    误差率小于等于80%时，对40820个数据进行检测， 命中39071个， 命中率是 95.72%
    误差率小于等于90%时，对40820个数据进行检测， 命中39282个， 命中率是 96.23%
    误差率小于等于100%时，对40820个数据进行检测， 命中39432个， 命中率是 96.60%

同时会将结果绘制出来，如下所示：

![](assets/images/linearregression.jpg?raw=true)


## 其它







