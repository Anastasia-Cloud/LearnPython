#сортировка слиянием
def connect(arr1,arr2):
  res=[]
  p1,p2=0,0
  while p1<len(arr1) and p2<len(arr2):
    if arr1[p1]<arr2[p2]:
      res.append(arr1[p1])
      p1+=1
    else:
      res.append(arr2[p2])
      p2+=1
  res+=arr1[p1:]+arr2[p2:]
  return res

def sort(arr):  #рекурсивная
  if len(arr)>1:
    l=len(arr)
    return connect(sort(arr[:l//2]),sort(arr[l//2:]))
  else:
    return arr
  
def otherSort(arr):  #нерекурсивная
  res=[[i] for i in arr]
  while len(res)>1:
    if len(res)%2!=0:
      res.append([])
    newRes=[]
    for i in range(0,len(res),2):
      newRes.append(connect(res[i],res[i+1]))
    res=newRes
  return res[0]

print(otherSort([2,3,4,1,2,77,6,55,9]))
