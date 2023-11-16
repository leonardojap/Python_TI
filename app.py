class DataCapture:
  def __init__(self):
    self.data = []


  def add(self, value):
    self.data.append(value)

  def build_stats(self):
    return self
    
  def less(self, value):
    counter = 0
    for i in self.data:
      if i < value:
        counter += 1
    return counter

  def greater(self, value):
    counter = 0
    for i in self.data:
      if i > value:
        counter += 1
    return counter

  def between(self, value1, value2):
    counter = 0
    for i in self.data:
      if i >= value1 and i <= value2:
        counter += 1
    return counter
  

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()

print(stats.less(4))
print(stats.greater(4))
print(stats.between(3, 6))
