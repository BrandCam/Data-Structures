class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    curr_node = self
    while(True):
        if(value > curr_node.value):
          if curr_node.right != None:
            curr_node = curr_node.right
          else:
            curr_node.right = BinarySearchTree(value)
            break
        else:
          if curr_node.left != None:
            curr_node = curr_node.left
          else:
            curr_node.left = BinarySearchTree(value)
            break

  def contains(self, target):
    curr_node = self
    value = self.value
    while(True):
      if(target==curr_node.value):
        return True
      else:
        if(target > curr_node.value):
          if curr_node.right != None:
            curr_node = curr_node.right
          else:
            return False
        else:
          if curr_node.left != None:
            curr_node = curr_node.left
          else:
            return False

  def get_max(self):
    curr_node = self
    while(True):
      if curr_node.right != None:
        curr_node=curr_node.right
      else:
        return curr_node.value

  def for_each(self, cb):
    cb(self.value)
    if self.right != None:
      self.right.for_each(cb)
    if self.left != None:
      self.left.for_each(cb)