import random

def bubble_sort(arr):
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print("Sorted Array:",arr)

def selection_sort(arr):
    n=len(arr)
    for i in range (n):
        min_index=i
        for  j in range (i+1,n):
            if arr[j]>arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

n=5000
arr=[random.randint(1,1000)for _ in range(n)]
selection_sort(arr)
print(arr)
bubble_sort(arr)
print(arr)