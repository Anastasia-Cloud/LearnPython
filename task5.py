#порядковые статистики: Random-Select
import random

def randomSelect(arr,k,l,r):
  if l<r:
    p=random.randint(l,r)
    arr[p],arr[r]=arr[r],arr[p]
    i,j=l,l
    while i<r:
      if arr[i]<=arr[r]:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=1
      else:
        i+=1
    arr[j],arr[r]=arr[r],arr[j]
    if k<j:
      return randomSelect(arr,k,l,j-1)
    else:
      return randomSelect(arr,k,j,r)
  elif l==r:
    return arr[r]
  else:
    return

print(randomSelect([2,1,4,5,3,8],3,0,5))
