import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    if len(self.storage) > 0:
      self._bubble_up(len(self.storage)-1)

  def delete(self):
    value = self.storage[0]

    self.storage[0] = self.storage[len(self.storage)-1]
    self.storage.pop(len(self.storage)-1)
    if len(self.storage) > 0:
      self._sift_down(0)
    return value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index == 1 or index == 2:
      parentIndex = 0
    else:
      parentIndex = math.floor((index-1)/2) 
    parent = self.storage[parentIndex]
    child = self.storage[index]
    if child > parent:
      self.storage[index] = parent
      self.storage[parentIndex] = child
      if(parentIndex != 0):
        self._bubble_up(parentIndex)

  def _sift_down(self, index):
    children = []
    childrenIndices = [2*(index+1)-1,2*(index+1)]
    parent = self.storage[index]

    if childrenIndices[0] > self.get_size()-1:
      pass
    else:
      if childrenIndices[1] > self.get_size()-1:
        childrenIndices.pop(1)
      for childIndex in childrenIndices:
        children.append(self.storage[childIndex])
      if len(children) > 1:
        if children[0] < children[1]:
          children.reverse()
          childrenIndices.reverse()
      if children[0] > parent:
        self.storage[index] = children[0]
        self.storage[childrenIndices[0]] = parent
        self._sift_down(childrenIndices[0])
