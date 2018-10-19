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


rec_stack = Stack()  # 用来记录安装的芯片的顺序
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


def show_map(ml):
    _MapLList = ml
    _resStr = 'MapInfo:\n'
    _MapWidth = len(MapLList)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            _resStr = _resStr + str(_MapLList[x][y]) + '  '
        _resStr = _resStr + '\n'
    print(_resStr)


def install_chip():
    _MapWidth = len(MapLList)
    for x in range(_MapWidth):
        for y in range(_MapWidth):
            for chiplist in ChipPoolLists:
                if insertable(x, y, chiplist):
                    no = rec_stack.size() + 1
                    inserted(x, y, chiplist, no)
                    show_map(MapLList)
                    maplist_push = copy.deepcopy(MapLList)
                    rec_stack.push(maplist_push)
                    print('==============================')
                    break
                else:
                    pass

    print('install_chip is completed')
    return


def insertable(x, y, _chiplist):
    for g in _chiplist:
        xp, yp = g
        try:
            gno = MapLList[x + xp][y + yp]
        except IndexError:
            return False
        finally:
            pass
        if gno != 0:
            return False
    return True


def inserted(x, y, _chiplist, _no):
    for g in _chiplist:
        xp, yp = g
        MapLList[x + xp][y + yp] = _no
    print(_chiplist, 'is inserted')


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


if __name__ == "__main__":
    install_chip()
    rec_stack.show()
    print('the process is end')
