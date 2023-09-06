class BalancedExpression:
  def __init__(self, expression):
    self.expression = expression
  
  def check(self):
    self.stack = []

    # Prepare stack of tags
    for i in self.expression:
      if i == "(" or i == ")" or i == "[" or i == "]" or i == "{" or i == "}":
        self.stack.append(i)
    print(self.stack)

    # Inital condition: if the last closing tag is an opening tag => return false
    if len(self.stack) == 0:
      return True
    if self.stack[-1] == "[" or self.stack[-1] == "{" or self.stack[-1] == "(" or len(self.stack) % 2 != 0: 
      return False
      
    # While stack is empty compare the current tag with the previous one and check for possible errors. 
    while len(self.stack)-1 > 0:
      current = self.stack.pop()

      if (self.stack[-1] == "(" or self.stack[-1] == "{") and  current == "]":
        print("Current:", current)
        print("-1:", self.stack[-1])
        return False
      
      if (self.stack[-1] == "(" or self.stack[-1] == "[") and  current == "}":
        print("Current:", current)
        print("-1:", self.stack[-1])
        return False
      
      if (self.stack[-1] == "[" or self.stack[-1] == "{") and  current == ")":
        print("Current:", current)
        print("-1:", self.stack[-1])
        return False
    return True
  
obj1 = BalancedExpression("(1+2)-3*[41+6]")
obj2 = BalancedExpression("(1+2)-3*[41+6}")
obj3 = BalancedExpression("(1+2)-3*[41+6")
obj4 = BalancedExpression("(1+2)-3*]41+6[")
obj5 = BalancedExpression("(1+[2-3]*4{41+6})")
obj6 = BalancedExpression(" ")

# print(obj1.check())
# print()
# print(obj2.check())
# print()
# print(obj3.check())
# print()
# print(obj4.check())
# print()
# print(obj5.check())
# print()
# print(obj6.check())