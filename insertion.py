import random
import time
import matplotlib.pyplot as plt
def insertion(arr):
    n=len(arr)
    for i in range (1,n):
        v=arr[i]
        j=i-1
        while j>=0 and arr[j]>v:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=v
n_list=[5000,6000,7000,8000]
sort_time=[]
for n in n_list:
    arr=[random.randint(1,1000)for _ in range(n)]
    s_t=time.time()
    insertion(arr)
    e_t=time.time()
    sort_time.append(e_t-s_t)
print("Input Size:",n_list)
print("Sorting Size:",sort_time)
plt.plot(n_list,sort_time)
plt.show()