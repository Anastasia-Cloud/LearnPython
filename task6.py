'''
Даны последовательность A1, ... An, состоящая из n целых чисел, и число S. Найдите количество пар элементов, 
сумма которых = S.
Пример входа 1 2 3 4 5, 6
Пример выхода 2

Пример входа 1 1 1 1 1, 2
Пример выхода 10

Пример входа 1 2 1 2 1 2, 3
Пример выхода 9

1 1 1 2 2 2 
3
'''
from task4 import sort

def findPairs(arr,s):#числа не повторяются
  sort(arr)
  l=0
  r=len(arr)-1
  count=0
  while l<r:
    if arr[l]+arr[r]<s:
      l+=1
    elif arr[l]+arr[r]==s:
      l+=1
      r-=1
      count+=1
    else:
      r-=1
  return count

def findPairs2(arr,s):#числа могут повторяться
  return
print(findPairs([1, 2, 3, 4, 5], 6))
