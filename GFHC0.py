# -*- coding: utf-8 -*-
import copy


# define stack data structure be used to save info
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


map_stack = Stack()  # 用来记录安装芯片后的地图信息
chip_stack = Stack()  # 用来记录安装的芯片的顺序
ChipList33 = [(0, 0), (0, 1), (0, 2),
              (1, 0), (1, 1), (1, 2)]
ChipList6 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
MapLList = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
ChipPoolLists = [ChipList33, ChipList6]


# 用于在屏幕上输出map的图像结果
def show_map(ml):
    _MapLList = ml
    _resStr = 'MapInfo:\n'
    _MapWidth = len(MapLList)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            _resStr = _resStr + str(_MapLList[x][y]) + '  '
        _resStr = _resStr + '\n'
    print(_resStr)


def install_chip(_map):
    maplist = copy.deepcopy(_map)
    _MapWidth = len(maplist)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            # 这边的xy是可插入点坐标
            for chiplist in ChipPoolLists:
                if insertable(x, y, chiplist, maplist):
                    no = map_stack.size() + 1
                    inserted(x, y, chiplist, no)
                    show_map(MapLList)
                    maplist_push = copy.deepcopy(MapLList)
                    map_stack.push(maplist_push)
                    print('==============================')
                    break
                else:
                    pass

    print('install_chip is completed')
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
    print(_chiplist, 'is inserted')
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
    _MapWidth = len(MapLList)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            if _map[x][y] == 0:
                return False
    return True


if __name__ == "__main__":
    install_chip()
    map_stack.show()
    print('the process is end')
