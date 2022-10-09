class Vehicle():
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle
    
  def drive(self, speed):
    self.mode = 'driving'
    self.speed = speed
  
class Car(Vehicle):
  def __init__(self, enginetype):
    super().__init__("Car")
    self.wheels = 4
    self.doors = 4 
    self.enginetype = enginetype 
    
  def drive(self, speed):
    self.speed = speed
    print("Driving my", self.enginetype, "car at", self.speed)

    
class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Motorcycle")
    if(hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
    self.doors = 0
    self.enginetype = enginetype
  def drive(self, speed):
    self.speed = speed
    print("Driving my", self.enginetype, "motorcycle at", self.speed)
    
v1 = Vehicle(Motorcycle)
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(v1.bodystyle)
print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)
car1.drive(30)
mc1.drive(35)

