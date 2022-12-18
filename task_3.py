""" Реализуйте алгоритм перемешивания списка. """

from random import randrange

def shuffle_func (oldlist):
    newlist=[None for i in range(n)]
    for i in range(n):
        newlist[i]=oldlist.pop(randrange(0,len(a)))
    return newlist

n = int(input('Введите число элементов массива: '))
a = [(i+1) for i in range(n)]
print('Старый массив',a)
b=shuffle_func(a)
print('Новый массив ',b)