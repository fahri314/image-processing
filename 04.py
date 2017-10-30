def createList(size):
    list = []
    for i in range(size):
        list.append(i)
    return list


def listIncrement(l, n):
    list = []
    for i in range(len(l)):
        list.append(l[i] + n)
    return list


%timeit list = listIncrement(createList(1000), 50)
