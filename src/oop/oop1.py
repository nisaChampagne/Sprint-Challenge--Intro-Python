# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle(): #parent class
    pass
class FlightVehicle(Vehicle):#child class with base class Vehicle
    pass
class GroundVehicle(Vehicle):#child class with base class vehicle
    pass
class Starship(FlightVehicle):#child class with base class flightvehicle
    pass
class Airplane(FlightVehicle):#child class with base class flightvehicle
    pass
class Car(GroundVehicle):#child class with base class groundvehicle
    pass
class Motorcycle(GroundVehicle):#child class with base class groundvehicle
    pass