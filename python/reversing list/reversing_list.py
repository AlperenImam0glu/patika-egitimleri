def reverseList(_list):
    if (len(_list) > 1):
        lent = len(_list)-1
    else:
        lent = len(_list)
    for i in range(int(len(_list)/2)):
        temp = _list[i]
        _list[i] = _list[lent-i]
        _list[lent-i] = temp
    return _list


def checkList(_list):
    _list = reverseList(_list)
    for i in range(len(_list)):
        if isinstance(_list[i], list):
            _list[i] = reverseList(_list[i])
    return _list


def printAndCalculate(_list):
    print(f"list        = {_list}")
    _list = checkList(_list)
    print(f"sorted list = {_list}")
    print(" ")


list1 = [[1, 2], [3, 4], [5, 6, 7]]
list2 = [[1, 2], [3, 4], [5, 6, 7], [8], [11]]
list3 = [[1, 2], [3, 4], 5, 6, 7, [8], [11, 12, 13], 14, 15, [16]]

printAndCalculate(list1)
printAndCalculate(list2)
printAndCalculate(list3)
