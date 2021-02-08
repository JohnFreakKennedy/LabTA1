import math
from random import randint
n = int(input("Введіть розмір масиву:"))
arr = []
arr2 = []
even = 0
for i in range(n):
    arr.append(randint(0, 100))
    arr2.append(arr[i])
    if arr[i] % 2 == 0:
        even = even+1
print(arr)
step = 0
temp = 0
for j in range(n):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        step = step+1
print(arr, step, sep="\n")
step = 0
for i in range(n):
    for j in range(n-1):
        if arr[j] % 2 == 1 and arr[j+1] % 2 == 0:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        if arr[j] % 2 == 1 and arr[j + 1] % 2 == 1:
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        step = step + 1
print(arr, step, sep="\n")
step = 0
step2 = 0
for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        if arr2[j] > arr2[j + 1]:
            temp = arr2[j]
            arr2[j] = arr2[j+1]
            arr2[j+1] = temp
        step2 = step2 + 1
print(arr, step, arr2, step2, sep="\n")