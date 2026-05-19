# coding:utf8
"""
# pylint: disable=line-too-long
url = "http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_dayqfq&param=hk00001,day,,,660,qfq&r=0.7773272375526847"

url 参数改动
股票代码 :hk00001
日k线天数：660

更改为需要获取的股票代码和天数例如：

# pylint: disable=line-too-long
url = "http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_dayqfq&param=hk00700,day,,,350,qfq&r=0.7773272375526847"

"""
import json
import re

from . import basequotation


class DayKline(basequotation.BaseQuotation):
    """腾讯免费行情获取"""

    max_num = 1





if __name__ == "__main__":
    pass
