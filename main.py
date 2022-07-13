# This is a sample Python script.
from math import floor
from random import randint


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def binary_search(array: [int], number: int) -> bool:
    index = floor(len(array) / 2)
    print(index, array[index])
    if array[index] == number:
        return True
    if index == 0:
        return False
    if array[index] > number:
        return binary_search(array[:index], number)
    if array[index] < number:
        return binary_search(array[index:], number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    results = {
        True: 0,
        False: 0,
    }
    for i in range(10000):
        stop = 100
        number = randint(0, stop)
        array = [randint(x, stop) for x in range(stop)]
        array.sort()
        # print(array)
        result = binary_search(array, number)
        results[result] += 1
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
