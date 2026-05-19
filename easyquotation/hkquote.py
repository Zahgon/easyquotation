# coding:utf8
"""
url = "http://sqt.gtimg.cn/utf8/q=r_hk00981"

url 参数改动
股票代码 q=r_hk00981
"""


import re

from . import basequotation


class HKQuote(basequotation.BaseQuotation):
    """腾讯免费行情获取"""



