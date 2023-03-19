def flatten(_list):
    if _list == []:
        return _list
    if isinstance(_list[0], list):
        return flatten(_list[0]) + flatten(_list[1:])
    return _list[:1] + flatten(_list[1:])


def printAndCalculate(_list):
    print(f"list        = {_list}")
    _list = flatten(_list)
    print(f"sorted list = {_list}")
    print(" ")


list1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

printAndCalculate(list1)