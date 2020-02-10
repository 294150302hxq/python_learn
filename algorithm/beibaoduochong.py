#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/21
    @desc:
"""

#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
    @author:huang xiaoqin
    @time: 2020/1/21
    @desc:
"""


def ks(i,c):
    result = 0
    if (i == 0) | (c == 0):
        # 初识化
        result = 0
    elif ws[i]>c:
        # 装不下
        result = ks(i-1, c)
    else:
        # 装得下，要考虑是不是最优
        # 取k个物品i，取其中使得总价值最大的k
        k = 0
        while (k*ws[i] <= c) & (k < ns[i]):
            tmp = ks(i-1, c-k*ws[i])+k*vs[i]
            k += 1
            if tmp > result:
                result = tmp
    return result


vs = [0,2,3,4]
ws = [0,3,4,5]
ns = [0,4,3,2]

result = ks(3,15)
print(result)
