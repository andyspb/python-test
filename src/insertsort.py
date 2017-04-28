'''
Created on Apr 23, 2017

@author: andy
'''
def insertion_sort(arr):
    for index in range(1,len(arr)):
        current = arr[index]
        pos = index

        while pos>0 and arr[pos-1]>current:
            arr[pos]=arr[pos-1]
            pos = pos-1

        arr[pos]=current


if __name__ == '__main__':
    arr = [54,26,93,17,77,31,44,55,20,0,34,23,22]
    print(arr)
    insertion_sort(arr)
    print(arr)
