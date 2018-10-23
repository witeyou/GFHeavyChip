# -*- coding: utf-8 -*-
"""
功能:本程序旨在存储并能够被其他程序读取芯片仓库的芯片的所有信息
作者:史学超
更新日期:2018.10.23
"""

import json

chips_info = {
    '001': {
        'color': 'red',  # 颜色
        'used': False,  # 是否被使用
        'position': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)],  # 位置信息
        'rotate': 0,  # 是否被旋转
        'hurt': 10,  # 伤害值
        'armor': 10,  # 破防值
        'precision': 10,  # 精度值
        'filling': 10  # 装填值
    },
    '002': {
        'color': 'blue',
        'used': True,
        'position': [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)],
        'rotate': 0,
        'hurt': 10,
        'armor': 10,
        'precision': 10,
        'filling': 10
    }
}


def writejs():
    with open('./data.json', 'w') as f:
        json.dump(chips_info, f)


def readjs():
    with open('./data.json', 'r') as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    writejs()
    print('the process chipsinfo is end')
