from random import randint
from timeit import repeat
# # import statistics
# #
def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=1)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
# #
# # from random import randint
# # def quicksort(array):
# #     if len(array) < 2:
# #         return array
# #     less, equal, more = [], [], []
# #     pivot = statistics.median(array)
# #     [less.append(x) if x < pivot else more.append(x) if x > pivot else equal.append(x) for x in array]
# #     return quicksort(less) + equal + quicksort(more)
# #
# # def quicksort_2(array):
# #     if len(array) < 2:
# #         return array
# #     less, equal, more = [], [], []
# #     pivot = array[randint(0, len(array) - 1)]
# #     [less.append(x) if x < pivot else more.append(x) if x > pivot else equal.append(x) for x in array]
# #     return quicksort(less) + equal + quicksort(more)
# #
# # def binary_sort(array):
# #     length = len(array)
# #     b = []
# #     for i in range(length):
# #         if len(b) == 0:
# #             b.append(array[i])
# #         else:
# #             start = 0
# #             end = len(b) - 1
# #             middle = (start + end)//2
# #             while start <= end:
# #                 if end - start < 2:
# #                     if array[i] == b[middle]:
# #                         b.insert(array[i], middle + 1)
# #                     elif array[i] < b[middle]:
# #                         end = middle - 1
# #                     else:
# #                         start = middle + 1
# #                 else:
# #                     if array[i] >= b[0]:
# #                         b.append(array[i])
# #                         print(b, "greater")
# #                     else:
# #                         b.insert(0, array[i])
# #                         print(b, " less")
# #                 print("lol")
# #
# #             b.insert(0, array[end])
# #
# # ARRAY_LENGTH = 5
# #
# # if __name__ == "__main__":
# #     # Generate an array of `ARRAY_LENGTH` items consisting
# #     # of random integer values between 0 and 999
# #     array = [randint(1, 10) for i in range(ARRAY_LENGTH)]
# #
# #     # Call the function using the name of the sorting algorithm
# #     # and the array you just created
# #     # run_sorting_algorithm(algorithm="quicksort_2", array=array)
# #     run_sorting_algorithm(algorithm="binary_sort", array=array)
# #
# import time, sys
# force = list if sys.version_info[0] == 3 else (lambda X: X)
# class timer:
#     def __init__(self, func):
#         self.func = func
#         self.alltime = 0
#     def __call__(self, *args, **kargs):
#         start = time.perf_counter()
#         result = self.func(*args, **kargs)
#         elapsed = time.perf_counter() - start
#         self.alltime += elapsed
#         print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
#         return result
#
# @timer
# def listcomp(N):
#     return [x * 2 for x in range(N)]
#
# @timer
# def mapcall(N):
#     return map((lambda x: x * 2), range(N))
#
# @timer
# def forloop(N):
#     M = []
#     for i in range(N):
#         M.append(i * 2)
#
#     return M
# listcomp(500000)
# listcomp(1000000)
# listcomp(250000)
# print('allTime = %s' % listcomp.alltime)
# print('')
# mapcall(500000)
# mapcall(1000000)
# mapcall(250000)
# print('allTime = %s' % mapcall.alltime)
# forloop(50000000)
# forloop(1000000)
# forloop(250000)
# print('allTime = %s' % forloop.alltime)
# print('\n**map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
# print('\n**map/forloop = %s' % round(mapcall.alltime / forloop.alltime, 3))
# print('\n**comp/forloop = %s' % round(listcomp.alltime / forloop.alltime, 3))
#
# # def insertion_sort(array):
# #     sorted_array = []
# #     for element in array:
# #         if len(sorted_array) > 0:
# #             start = 0
# #             end = len(sorted_array) + 1
# #             mid = (len(sorted_array) + 1)//2 - 1
# #             while start <= mid < end:
# #                 if element > sorted_array[mid]:
# #                     start = mid + 1
# #                     mid = (mid + len(sorted_array))//2
# #                 elif element < sorted_array[mid]:
# #                     end = mid - 1
# #                     mid = (start + mid) // 2 + 1
# #             sorted_array.insert(mid, element)
# #         else:
# #             sorted_array.append(element)
# #     return list(reversed(sorted_array))
# #
from random import randint
toSort = []
for i in range(5):
    toSort.append(randint(1,1000))
# print(toSort)
# print(insertion_sort(toSort))

from random import randint

def binary_sort(arr, val, start, end):
    # we need to distinugish whether we
    # should insert before or after the
    # left boundary. imagine [0] is the last
    # step of the binary search and we need
    # to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_sort(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_sort(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_sort(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


# print("Sorted array:")
# print(insertion_sort(toSort))

def quicksort(arr):
    if len(arr) > 1:
        pivot = randint(0, len(arr)-1)
        less = []
        equal = []
        more = []
        for element in arr:
            if element < arr[pivot]:
                less.append(element)
            elif element > arr[pivot]:
                more.append(element)
            else:
                equal.append(element)
    else:
        return arr

    return quicksort(less) + equal + quicksort(more)

# print(run_sorting_algorithm(algorithm="quicksort", array=toSort))
# print(run_sorting_algorithm(algorithm="binary_sort", array=toSort))


def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def merge_sort(arr):
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    if len(left) == 1:
        if len(right) == 1:
            if left[0] < right[0]:
                return left + right
            else:
                return right + left
        else:
            return merge(left, merge_sort(right))
    elif len(right) == 1:
        return merge(merge_sort(left), right)
    else:
        return merge(merge_sort(left), merge_sort(right))

def merge(arr1, arr2):
    index1 = 0
    index2 = 0
    mergedList = []
    if arr1 and arr2:
        # while len(arr1) < len(arr2):
        #     arr1.append(0)
        # while len(arr2) < len(arr1):
        #     arr2.append(0)
        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] > arr2[index2]:
                mergedList.append(arr2[index2])
                index2 += 1
            elif arr2[index2] > arr1[index1]:
                mergedList.append(arr1[index1])
                index1 += 1
            else:
                mergedList.append(arr1[index1])
                mergedList.append(arr2[index2])
                index1 += 1
                index2 += 1
        if index1 == len(arr1):
            if index2 + 1 > len(arr2):
                return mergedList
            else:
                return mergedList + arr2[index2:]
        else:
            if index2 + 1 >= len(arr2):
                return mergedList + arr1[index1:]
            else:
                pass
    elif arr1:
        return arr1
    elif arr2:
        return arr2
#
#
# print(bubbleSort(toSort))
toSort = []
for i in range(50):
    for i in range(10):
        toSort.append(randint(1,1000))
    # print(toSort)
    # print(merge_sort(toSort))
    toSort = []
print(merge_sort([436, 961, 38, 533, 624, 589, 11, 77, 433, 689]))
# print(merge([1,2,4], [2,3,4]))