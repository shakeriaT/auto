class Car:
  def __init__(self, make, model):
      self.make = make
      self.model = model

# create a list of cars
cars = []
# add some cars to the list
allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def find_car(make, model):
  for car in cars:
      if car.make == make and car.model == model:
          return car
  return None

def add_car(make, model):
  car = find_car(make, model)
  if car is None:
      car = Car(make, model)
      cars.append(car)
  print(cars.make, cars.model)