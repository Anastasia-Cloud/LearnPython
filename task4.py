import random
#быстрая сортировка
def quickSort(arr,l,r):
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
    quickSort(arr,l,j-1)
    quickSort(arr,j+1,r)
  else:
    return

def sort(arr):  
  quickSort(arr,0,len(arr)-1)

#a=[2,3,4,1,2,77,6,55,9]
#sort(a)
#print(a)