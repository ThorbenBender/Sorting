# TO-DO: Complete the selection_sort() function below
import random


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # j = i + 1

        currentNum = arr[i]

        # print('array', i)
        # print('currentNum', currentNum)

        # while j < len(arr) - 1 and currentNum < arr[j]:
        #     print('num in j is: ', arr[j])
        #     print('j in while', j)
        #     j += 1

        # print(currentNum)
        # print('is smaller currentNum', arr[j])
        # if (currentNum > arr[j]):
        #     smallerNum = arr[j]
        #     arr.remove(arr[j])
        #     arr.insert(i, smallerNum)
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


print(selection_sort(random.sample(range(200), 50)))
