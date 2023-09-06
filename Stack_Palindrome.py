class Palindrome_Stack:
  def __init__(self, word):
    self.word = word

  def compare(self):
    self.stack = []

    for i in self.word:
      self.stack.append(i)

    for i in self.stack:
      if self.stack.pop() != i: 
        return False
      
    return True

check = Palindrome_Stack("helloolleh")
print(check.compare()) 