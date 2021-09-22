
class Student:

  # Initializer to define attributes of Student class
  # Values for name, major, gpa, is_on_probation are getting
  # passed into the __init__ function
  def __init__(self, name, major, gpa, is_on_probation):
    # name of the student object is gonna be the name given to the constructor
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation
  
  def sayStudentName(self):
    print(self.name)
