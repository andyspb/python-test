'''
Created on 22 04 2017

@author: andy
'''

def quickSort(arr):
    quickSortHelper(arr,0,len(arr)-1)
   
def quickSortHelper(arr,start,end):
    if start<end:
        splitpoint = partition(arr,start,end)
        quickSortHelper(arr,start,splitpoint-1)
        quickSortHelper(arr,splitpoint+1,end)

def partition(arr,start,end):
    pivot = arr[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1

        while arr[right] >= pivot and right >= left:
            right = right -1

        if right < left:
            done = True
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    temp = arr[start]
    arr[start] = arr[right]
    arr[right] = temp
    return right   


if __name__ == '__main__':
    arr = [54,26,93,17,77,31,44,55,20]
    print(arr)    
    quickSort(arr)
    print(arr)    
