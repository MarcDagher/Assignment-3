class Node:
  def __init__(self, brand, color, plate_number, next = None):
    self.brand = brand
    self.color = color
    self.plate_number = plate_number
    self.next = next
  
  # Methods of the LinkedList class: addTail - addHead - deleteTail - deleteHead - printList - search
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
  
  def addTail(self,brand, color, plate_number):
    new_node = Node(brand, color, plate_number)
    self.brand = brand
    self.color = color
    self.plate_number = plate_number

    if self.size == 0:
      self.tail = new_node   
      self.head = new_node
      self.size += 1

    else:
      self.tail.next = new_node
      self.tail = new_node
      self.size += 1

  def addHead(self,brand, color, plate_number):
    new_node = Node(brand, color, plate_number)
    self.brand = brand
    self.color = color
    self.plate_number = plate_number

    if self.size == 0:
      self.head = new_node
      self.tail = new_node
      self.size += 1
    else:
      new_node.next = self.head
      self.head = new_node
      self.size += 1
  
  def deleteTail(self):
    if self.size == 0:
      return None
    
    else: 
      current = self.head
      for i in range(self.size - 2):
        current = current.next
      
      current.next = None
      self.tail = current
      self.size -= 1

  def deleteHead(self):
    if self.size == 0:
      return None
    
    else:
      self.head = self.head.next
      self.size -= 1
  
  def printList(self):
    if self.size == 0:
      return None
    current = self.head
    while current != None:
      print(current.brand, current.color, current.plate_number)
      current = current.next
  
  def search(self, brand, color, plate_number):
    if self.size == 0:
      return False
    else:
      current = self.head
      while current != None:
        if current.brand == brand and current.color == color and  current.plate_number == plate_number:
          return True
        current = current.next
      return False

# enqueue - dequeue - size - isEmpty - front 
class Queue:
  def __init__(self):
    self.LL = LinkedList()
    
  def enqueue(self, brand, color, plate_number):
    self.LL.addHead(brand, color, plate_number)

  def dequeue(self):
    print("{} {} {} removed from queue.".format(self.LL.tail.brand, self.LL.tail.color, self.LL.tail.plate_number))
    self.LL.deleteTail()
    print()

  def size(self):
    return self.LL.size

  def isEmpty(self):
    if self.LL.size == 0:
      return True
    else: return False
  
  def front(self):
    if self.LL.size == 0:
      return "None" 
    else:
      tail = self.LL.tail
      print(tail.brand, tail.color, tail.plate_number)
      print()

# LinkedList => addTail - addHead - deleteTail - deleteHead - printList - search
# Queue => enqueue - dequeue - size - isEmpty - front 

class CarWash:
  def __init__(self):
    self.queue = Queue()
    self.menu()

  def menu(self):
    self.command = input('''
                    1. To insert a car to the queue
                    2. To remove the car from the queue
                    Choose 1 or 2: ''')
    while self.command != "1" and self.command != "2":
      self.command = input('''
                    1. To insert a car to the queue
                    2. To remove the car from the queue
                    Choose 1 or 2: ''')
    return self.action()
  
  def action(self):

    if self.command == "1":
      brand = input("Insert brand: ")
      color = input("Insert color: ")

      plate_number = input("Insert plate_number: ")
      while plate_number.isdigit() == False:
        plate_number = input("Plate Number must be a number! Insert a valid plate number: ") 

      self.queue.enqueue(brand, color, plate_number)
      print()
      print("Car added to queue.")
      print("Queue size = {}".format(self.queue.size()))
      print()
      
    
    elif self.command == "2": 
      self.queue.dequeue()
      print("Next in line: ", self.queue.front())
      print("Queue size = {}".format(self.queue.size()))
      print()

    if self.queue.isEmpty():
      print("All the cars have been washed.")
      return
    
    self.menu()

obj = CarWash()