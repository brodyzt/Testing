import timeit
import time

def calculateRunTime(function, *args):
    startTime = time.time()
    for x in range(10**5):
        result = function(*args)
    return time.time() - startTime

list = []

def timeFunction(function, list):
    return timeit.timeit(function(list))

file = open('List','r')
for line in file:
    list.append(int(line))

def bubble_sort(list):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for x in range(len(list) - 1):
            if(list[x] > list[x+1]):
                temp = list[x]
                list[x] = list[x+1]
                list[x+1] = temp
                is_sorted = False
    return list

def selection_sort(list):
    for x in range(0, len(list) - 1):
        temp_lowest = list[x]
        temp_lowest_location = x
        for y in range(x + 1, len(list)):
            if list[y] < temp_lowest:
                temp_lowest = list[y]
                temp_lowest_location = y
        temp = list[x]
        list[x] = list[temp_lowest_location]
        list[temp_lowest_location] = temp
    return list

def insertion_sort(list): # fix this
    temp_list = []
    list_length = len(list)
    for x in range(list_length):
        min = list[0]
        min_loc = 0
        for y in range(1, len(list)):
            if list[y] < list[min_loc]:
                min = list[y]
                min_loc = y
        temp_list.append(list[min_loc])
        list.pop(min_loc)
    return temp_list


print('Bubble Sort List: ' + str(bubble_sort(list)))
print('Time: {}\n'.format(calculateRunTime(bubble_sort, list)))

print('Selection Sort List: ' + str(selection_sort(list)))
print('Time: {}\n'.format(calculateRunTime(selection_sort, list)))

print('Insertion Sort List: ' + str(insertion_sort(list)))
print('Time: {}\n'.format(calculateRunTime(insertion_sort, list)))
