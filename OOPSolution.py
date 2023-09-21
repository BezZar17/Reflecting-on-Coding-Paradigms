# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".


# My attempt


class Podracers:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"

class AnakinsPod(Podracers):
  def __init__(self, max_speed, condition, price):
    super.__init__(self, max_speed, condition, price):
  def boost(self):
    self.max_speed = self.max_speed * 2

class SebulbasPod(Podracers):
  def __init__(self, max_speed, condition, price):
    super.__init__(max_speed, condition, price):
  
  def flame_jet(self,oppenent):
    oppenent.condition = "trashed"

# Solution
# class Podracer:
#   def __init__(self, max_speed, condition, price):
#     self.max_speed = max_speed
#     self.condition = condition
#     self.price = price
#   def repair(self):
#     self.condition = "repaired"
    
# class AnakinsPod(Podracer):
#   def __init__(self, max_speed, condition, price):
#     super.init(max_speed, condition, price):
  
#   def boost(self):
#     self.max_speed *= 2
    
# class SebulbasPod(Podracer):
#   def __init__(self, max_speed, condition, price):
#     super.init(max_speed, condition, price):
  
#   def flame_jet(self,other):
#     other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP?

# Inheritance is shown in this activity by having the Podracers class as an attribute for each new Class
    
# Polymorphism is shown when Anikans Pod and Sebulbas Pod share the data of the Podracers class

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

# Personally, I like writing it why this style of code becuase I seem to know it more, Still need to remeber a few things.

# How in particular did Object Oriented Programming assist in the solving of this problem?

# I honestly have new clue. I know what to do, I just don't know why we do it.