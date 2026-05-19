# coding:utf8
import re
from datetime import datetime
from typing import Optional

from . import basequotation


class Tencent(basequotation.BaseQuotation):
    """腾讯免费行情获取"""

    grep_stock_code = re.compile(r"(?<=_)\w+")
    max_num = 60



    def _safe_acquire_float(self, stock: list, idx: int) -> Optional[float]:
        """
        There are some securities that only have 50 fields. See example below:
        ['\nv_sh518801="1',
        '国泰申赎',
        '518801',
        '2.229',
        ......
         '', '0.000', '2.452', '2.006', '"']
        """
        pass

