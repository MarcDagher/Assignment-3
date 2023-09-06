class Node:
  def __init__(self, info, next=None):
    self.info=info
    self.next=next

class LinkedList:
  def __init__(self):
    self.head=None 
    self.tail=None 
    self.size=0 

  def addToHead(self,info): 
    n=Node(info) 

    if self.size==0: 
      self.head=n
      self.tail=n
      self.size+=1
      
    else: 
      n.next=self.head  
      self.head=n 
      self.size+=1
  
  def addToTail(self, info): 
    n = Node(info)

    if self.size == 0: 
      self.head = n
      self.tail = n
      self.size += 1
    else:
      self.tail.next = n 
      self.tail = n 
      self.size += 1
    
  def search(self, key):  
    if self.size == 0:
      return False
    else:
      current = self.head 
      while current != None: 
        if current.info == key:
          return True
        
        current = current.next 
    return False
  
  def deleteHead(self): 
    if self.size == 0:
      return None
    elif self.size == 1:
      temporary_head = self.head.info 
      self.head = None
      self.tail = None
      self.size = 0
      return temporary_head 
    else: 
      temporary_head = self.head.info
      self.head = self.head.next 
      self.size -=1
      return temporary_head
  
  def deleteTail(self):
    if self.size == 0:
      return None
    elif self.size == 1:
      temp = self.tail.info
      self.head = None
      self.tail = None
      self.size = 0
      return temp

    temp = self.tail.info 
    current = self.head 
    for i in range(self.size - 2): 
      current = current.next 

    self.tail = current 
    self.tail.next = None 
    self.size -=1
    return temp 
  
  def print(self):
    if self.size == 0: return None

    current = self.head
    count = 1
    while current != None:
      print("Node {}: ".format(count), current.info)
      count += 1
      current = current.next


class Stack:
  def __init__(self):
    self.stack = LinkedList()
    self.phrase = input("Insert String: ")
    new_phrase = ""
    for i in self.phrase:
      if i == "*":
        new_phrase += self.Pop()
      else:
        self.Push(i) 
    while self.stack.size > 0:
      new_phrase += self.Pop()
    
    print(new_phrase)
  def Push(self, item):
    self.stack.addToTail(item)
  
  def Pop(self):
    return self.stack.deleteTail()

obj = Stack()