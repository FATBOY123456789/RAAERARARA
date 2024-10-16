class Vehicle:
    def __init__(self,school_name,speed,mileage):
        self.school_name=school_name
        self.speed=speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
schoolbus=Bus('School Volvo',123,20)
print('The school that owns this bus is',schoolbus.school_name,'the speed of this bus is',schoolbus.speed,'and the mileage is',schoolbus.mileage)