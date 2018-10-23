# -*- coding: utf-8 -*-
"""
功能:本程序旨在实验出少女前线重装部队芯片强化的最优情况
作者:史学超
更新日期:2018.10.23
现在已经实现了一个简单的模型,需要的是不断额往芯片池中添加芯片
代码变得更简洁,生成的方案更多,也更加容易出现重复的地方
"""
# TODO(sxc): 添加图像化界面
# TODO(sxc): 芯片数据要能够附带属性
# TODO(sxc): 重复结果的删除和结果的评分

import copy


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size() - 1]

    # this is my add
    def show(self):
        i = 1
        for x in self.items:
            print('this is stack no ', i)
            show_map(x)
            i = i + 1

    def rest(self):
        tmp = ''
        for x in self.items:
            tmp = tmp + str(x)
        return tmp


map_stack = Stack()  # 用来记录安装芯片后的地图信息
chip_stack = Stack()  # 用来记录安装的芯片在芯片池中的起始序号
ChipList33 = [(0, 0), (0, 1), (0, 2),
              (1, 0), (1, 1), (1, 2)]
ChipList222 = [(0, 0), (0, 1),
               (1, 0), (1, 1),
               (2, 0), (2, 1)]
ChipList6 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
MapLList = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
ChipPoolLists = [ChipList33, ChipList222, ChipList6]
resultList = []


# 用于在屏幕上输出map的图像结果
def show_map(ml):
    _MapLList = ml
    _resStr = 'MapInfo:\n'
    _MapWidth = len(MapLList)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            if _MapLList[x][y] == -1:
                _resStr = _resStr + 'x' + '  '
            else:
                _resStr = _resStr + str(_MapLList[x][y]) + '  '
        _resStr = _resStr + '\n'
    print(_resStr)


# 传入的_chip是上一次插入的芯片序号
# 返回0的时候是按预设情况正常结束,返回1则异常结束
def install_chip(_map, _chip=-1):
    # 用于中断递归的条件
    if map_stack.empty() and _chip == (len(ChipPoolLists) - 1):
        print('install_chip is completed')
        return
    if _chip != (len(ChipPoolLists) - 1):
        chip_start = _chip + 1  # 记录本次芯片池中插入芯片的起始序号
        maplist = copy.deepcopy(_map)
        _MapWidth = len(maplist)
        for x in range(_MapWidth):
            for y in range(_MapWidth):
                # 这边得到的xy是可插入点坐标,下面的Z是芯片池中的序号
                if maplist[x][y] == 0:
                    for z in range(chip_start, len(ChipPoolLists)):
                        chiplist = ChipPoolLists[z]
                        if insertable(x, y, chiplist, maplist):
                            no = map_stack.size() + 1  # 插入位置的数值,用来区分插入的是哪一块芯片
                            maplist = inserted(x, y, chiplist, no, maplist)
                            chip_start = 0
                            # show_map(maplist)
                            map_stack.push(maplist)
                            chip_stack.push(z)
                            # print('==============================')
                            break
                else:
                    continue
        if isfulll(maplist):
            resultList.append(maplist)
            show_map(maplist)
            print("+++有一个方案已经完成+++")
    map_stack.pop()
    tempc1 = chip_stack.pop()
    if map_stack.empty():
        tempm1 = copy.deepcopy(MapLList)
    else:
        tempm1 = map_stack.top()
    install_chip(tempm1, tempc1)
    return


def insertable(x, y, _chiplist, _map):
    maplist = _map
    for g in _chiplist:
        xp, yp = g
        try:
            gno = maplist[x + xp][y + yp]
        except IndexError:
            return False
        finally:
            pass
        if gno != 0:
            return False
    return True


# xy表示插入起始点的坐标,_chiplist表示插入芯片的类型,
# _no表示插入的数值, _map表示被插入的map信息
# 返回插入后的map
def inserted(x, y, _chiplist, _no, _map):
    maplist = copy.deepcopy(_map)
    for g in _chiplist:
        xp, yp = g
        maplist[x + xp][y + yp] = _no
    # print(_chiplist, 'is inserted')
    return maplist


def rotate90(_chiplist, _time=0):
    list_ = []
    if _time == 0:
        list_ = _chiplist
        return list_
    else:
        for t in range(_time):
            list_ = []
            for item in _chiplist:
                x, y = item
                list_.append((-y, x))
        return list_


# 返回False为不满,代表未完全插入;返回True为满,已经完全插入.
def isfulll(_map):
    maplist = copy.deepcopy(_map)
    _MapWidth = len(maplist)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            if _map[x][y] == 0:
                return False
    return True


def writefile(_aimlist):
    with open('./resultList.txt', 'w') as f:
        for x in _aimlist:
            f.write(str(x) + '\n==========\n')
    print('已经成功写入文件到', 'resultList.txt')


if __name__ == "__main__":
    # map_stack.push(copy.deepcopy(MapLList))
    # install_chip(MapLList, -1)
    # writefile(resultList)
    print('总共有', len(resultList), '个结果')
    print('the process is end')
