'''
Дана последовательность a1, a2, ..., an из n различных целых чисел. Для каждого числа ai найдите наименьшее такое j, что
j > i и aj > ai.

Пример входа: 1 3 2 4 5 
Пример выхода: 2 4 4 5 -1

Пример входа: 100 
Пример выхода: -1
'''
def func(arr):
  res=[-1]*len(arr)
  stack=[]
  for i in range(len(arr)):
    while len(stack)>0 and stack[-1][0]<arr[i]:
      j=stack.pop()
      res[j[1]]=i+1
    stack.append([arr[i],i])
  return res
print(func([1,3,1,0,2,4]))