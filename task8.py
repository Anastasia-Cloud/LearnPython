#бинарный поиск
def find(arr,k,l,r):
  while l<=r:
    #print(l,r)
    m=(l+r)//2
    if k<arr[m]:
      r=m-1
    elif k==arr[m]:
      return m
    else:
      l=m+1
  return 'item not found...'

def findItem(arr,k):
  return find(arr,k,0,len(arr)-1)

print(findItem([1, 3, 5, 7, 9, 10, 11 ,13],8))