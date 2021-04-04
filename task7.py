'''
Дано множество отрезков с целыми концами на прямой. Найти точку, которая является общей для максимального количества отрезков, и вывести это максимальное количество.
'''
arr=[(0,4),(0,2),(1,3),(5,6)]
res=[]
for i in range(len(arr)):
  x,y=arr[i]
  res.append((x,0))
  res.append((y,1))
res=sorted(res)
maxCount=0
count=0
for i in res:
  #print(i)
  if i[1]==0:
    count+=1
    maxCount=max(count,maxCount)
  else:
    count-=1
  #print(count,maxCount)
print(maxCount)