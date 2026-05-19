# coding:utf8
import abc
import json
import multiprocessing.pool
import warnings

import requests

from . import helpers


class BaseQuotation(metaclass=abc.ABCMeta):
    """行情获取基类"""

    max_num = 800  # 每次请求的最大股票数

    @property
    @abc.abstractmethod
    def stock_api(self) -> str:
        """
        行情 api 地址
        """
        pass

    def __init__(self):
        self._session = requests.session()
        stock_codes = self.load_stock_codes()
        self.stock_list = self.gen_stock_list(stock_codes)





    @property
    def all_market(self):
        """return quotation with stock_code prefix key"""
        pass

    def stocks(self, stock_codes, prefix=False):
        """deprecated, use real instead"""
        pass

    def real(self, stock_codes, prefix=False):
        """返回指定股票的实时行情
        :param stock_codes: 股票代码或股票代码列表，
                示例：'000001' / 'sh000001' / ['000001', '000002'] 
        :param prefix: 如果prefix为True，返回的行情字典键以sh/sz/bj市场标识开头
                    如果prefix为False，返回的行情将无法区分指数和股票代码，例如 sh000001 上证指数和 sz000001 平安银行
        :return: 行情字典，键为股票代码，值为实时行情。
        """
        pass

    def market_snapshot(self, prefix=False):
        """return all market quotation snapshot
        :param prefix: if prefix is True, return quotation dict's  stock_code
             key start with sh/sz market flag
        """
        pass



    def get_stock_data(self, stock_list, **kwargs):
        """获取并格式化股票信息"""
        pass

    def _fetch_stock_data(self, stock_list):
        """获取股票信息"""
        pass

    def format_response_data(self, rep_data, **kwargs):
        pass
