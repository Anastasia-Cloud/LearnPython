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
    print('item added!')
  
  def heapify(self,index):
    pass

  def buildHeap(self,arr):
    pass
  
  def getMax(self):
    pass

  def heapSort(self,arr):
    pass

myHeap=Heap()
myHeap.add(99)
myHeap.add(77)
myHeap.add(6)
myHeap.add(34)
myHeap.add(1)
