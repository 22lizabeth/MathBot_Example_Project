import operator

class MathBot:
  
  def __init__(self):
    self.numbers = []
    self.operators = []
    self.numberOrder = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    self.operatorDict = {"+": operator.add, "-": operator.sub, "/": operator.div, "*": operator.mul}
    
  def isOperator(self, operator):
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
      return True
    else:
      return False
  
  def solveProblem(self, operator1, operator2):
    i = 0
    while(len(self.operators) > 0 and i < len(self.operators)):
      if self.operators[i] == operator1 or self.operators[i] == operator2:
        tempAnswer = self.operatorDict[self.operators[i]](float(self.numbers[i]), float(self.numbers[i+1]))
        self.numbers[i] = str(tempAnswer)
        self.numbers.pop(i+1)
        self.operators.pop(i)
      else:
        i += 1
  
  def doMathProblem(self):
    
    error = False
    self.numbers = []
    self.operators = []
    
    numNumbers = input("\nHow many numbers are in your math problem?\n")
    numNumbers = int(numNumbers)
    
    if numNumbers <= 10:
      
      print("\nPlease read the problem from left to right.")
      for i in range(numNumbers):
        nextNum = input("\nWhat is the " + self.numberOrder[i] + " number?")
        while(not nextNum.isnumeric()):
          nextNum = input("Please enter a valid number: ")
        self.numbers.append(nextNum)
        
      print("\nThank you for all those juicy numbers.\n")
      
      numOperators = numNumbers - 1
      
      if numOperators > 0:
        print("I will now ask for each operator from left to right." \
        + "Operators are things like addition, subtraction, division, etc." \
        + "For division, type '/', for multiplication, type '*'\n")
        for i in range(numOperators):
          if i == 0:
            nextOperator = input("What is the first operator?")
          else:
            nextOperator = input("\nWhat is the next operator?")
          
          while(not self.isOperator(nextOperator)):
            nextOperator = input("Please enter a valid operator (+,-,*, or /): ")
          
          if(nextOperator == "/" and self.numbers[len(self.operators)+1] == "0"):
            error = True
            break
          
          self.operators.append(nextOperator)
        
      if(not error):
        print("\nGreat, I will now do math! Standby...")
            
        self.solveProblem("*","/")
        self.solveProblem("+","-")
        print("\nThe answer to your math problem is: " + self.numbers[0])
      else:
        print("\nCannot divide by zero. Problem unsolvable." \
        + "\nMy sincerest apologies.")
        
        
Bob = MathBot()
print("Hello and welcome to the greatest math bot on the planet!\n")
userName = input("Who am I speaking with today?")
print("\nWelcome " + userName + "!")
print("\nSo that I can best assist you, please be accurate in your answers to my questions today.")

while(True):
  Bob.doMathProblem()
  userAnswer = input("\nDo you have another problem I can help with?")
  if(userAnswer.lower() == "yeah" or userAnswer.lower() == "yes" 
  or userAnswer.lower() == "yup" or userAnswer.lower() == "obviously"
  or userAnswer.lower() == "yuss"):
    continue
  else:
    break

print("\nThank you for letting me assist you today! \nHave a great day " + userName + "!")
