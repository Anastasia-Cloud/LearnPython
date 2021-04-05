'''
На плоскости дано n отрезков. Определите, есть ли среди
них два пересекающихся.
Выведите NO, если никакие два отрезка не пересекаются. Иначе
в первой строке выведите YES, а во второй –– номера любых двух
пересекающихся отрезков. Отрезки нумеруются с единицы.

Пример входа
3
0 0 2 2
0 1 0 2
0 2 2 0
Пример выхода
YES
1 3

https://e-maxx.ru/algo/intersecting_segments

'''
def findIndex(arr,data):
  l=0
  r=len(arr)
  while l<=r:
    print(data,l,r)
    k=(r+l)//2
    if data<arr[k]:
      r=k-1
    elif data>k:
      l=k+1
    else:
      return k+1 
  return k
arr=[1,3,5,7,8,9]
print(findIndex(arr,4))
'''
arr=[]
otr={}
n=int(input())
for i in range(n):
  x1,y1,x2,y2=[int(j) for j in input().split()]
  arr.append((x1,0,y1,i+1))
  arr.append((x2,1,y2,i+1))
  otr[i+1]=(x1,y1,x2,y2)
res=[]
arr=sorted(arr)
for i in arr:
  pass
#print(arr)
'''
