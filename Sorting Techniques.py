import timeit
import time

def calculateRunTime(function, *args):
    startTime = time.time()
    for x in range(10**3):
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
                list[x],list[x+1]=list[x+1],list[x]
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
        list[x],list[temp_lowest_location]=list[temp_lowest_location],list[x]
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
counter = 0
def merge_sort(input_list):
    if len(input_list) == 1:
        return [input_list, 1]
    else:
        middle = len(input_list) // 2
        left_data = merge_sort(input_list[:middle])
        left = left_data[0]
        right_data = merge_sort(input_list[middle:len(input_list)])
        right = right_data[0]
        result = [0 for x in range(len(input_list))]
        counter = left_data[1] + right_data[1]
        l_counter = 0
        r_counter = 0
        for m_counter in range(len(input_list)):
            if l_counter == len(left):
                result[m_counter] = right[r_counter]
                r_counter += 1
            elif r_counter == len(right):
                result[m_counter] = left[l_counter]
                l_counter += 1
            elif left[l_counter] < right[r_counter]:
                result[m_counter] = left[l_counter]
                l_counter += 1
            else:
                result[m_counter] = right[r_counter]
                r_counter += 1
        return [result, counter]

print('Bubble Sort List: ' + str(bubble_sort(list)))
print('Time: {}\n'.format(calculateRunTime(bubble_sort, list)))

print('Selection Sort List: ' + str(selection_sort(list)))
print('Time: {}\n'.format(calculateRunTime(selection_sort, list)))

print('Insertion Sort List: ' + str(insertion_sort(list)))
print('Time: {}\n'.format(calculateRunTime(insertion_sort, list)))

print('Merge Sort List: ' + str(merge_sort(list)))
#print('Time: {}\n'.format(calculateRunTime(merge_sort, list)))
