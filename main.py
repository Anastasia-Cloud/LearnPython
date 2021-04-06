#Двоичная куча

class Heap:
  def __init__(self):
    self.heapList=[]

  def add(self,data):
    self.heapList.append(data)
    index=len(self.heapList)-1
    parent=(index-1)//2
    while index>0 and data>self.heapList[parent]:
      self.heapList[index],self.heapList[parent]=self.heapList[parent],self.heapList[index]
      index=parent
      parent=(index-1)//2
    print('item added: ',self.heapList)
  
  def findMax(self,i1,i2):
    if i2>=len(self.heapList):
      return i1
    if i1>=len(self.heapList):
      return i2
    if self.heapList[i1]>self.heapList[i2]:
      return i1
    else:
      return i2

  def heapify(self,index):
    if index>((len(self.heapList)-2)//2):
      print('result: ',self.heapList)
      return
    left=2*index+1
    right=2*index+2
    maxCh=self.findMax(left,right)
    while self.heapList[maxCh]>self.heapList[index]:
      self.heapList[index],self.heapList[maxCh]=self.heapList[maxCh],self.heapList[index]
      index=maxCh
      if index>((len(self.heapList)-2)//2):
        print('result: ',self.heapList)
        return
      left=2*index+1
      right=2*index+2
      maxCh=self.findMax(left,right)
    print('result: ',self.heapList)
    

  def buildHeap(self,arr):
    self.heapList=arr[:]
    for i in range((len(self.heapList)-2)//2,-1,-1):
      self.heapify(i)
    print('build result: ',self.heapList)
  
  def getMax(self):
    if len(self.heapList)<=0:
      return None
    result=self.heapList[0]
    self.heapList[0]=self.heapList[-1]
    self.heapList.pop()
    self.heapify(0)
    return result

  def heapSort(self,arr):
    pass

myHeap=Heap()
myHeap.add(1)
myHeap.add(2)
myHeap.add(3)
myHeap.add(4)
myHeap.add(5)
myHeap.add(6)
myHeap.buildHeap([1,2,3,4,0,6])
print(myHeap.getMax())
print(myHeap.getMax())
print(myHeap.getMax())
print(myHeap.getMax())
print(myHeap.getMax())
print(myHeap.getMax())
print(myHeap.getMax())
