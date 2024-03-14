class vehicle:
    def __init__(self,manufactor,model,year,type):
        self.manufactor = manufactor
        self.model = model
        self.year = year
        self.type = type
        self.started = False
    def __str__(self):
        return f"{self.manufactor},{self.model},{self.year},{self.type}"
        
    def moves(self):
        print(f" starts {self.manufactor}")
        self.started = True
        print(f"{self.manufactor} is starting")
        
    def not_moves(self):
        print(f" stops {self.manufactor}")
        self.started = False
        print(f"{self.manufactor} is stopped")
        
    def starts(self):
        return self.started
        
class cars(vehicle):
    def __init__(self,manufactor,model,year,type,no_of_doors):
      self.no_of_doors= no_of_doors
      super().__init__(manufactor,model,year,type)
      
    def horn_sound(self):
        
        print("hanking")
        
class Tractor(vehicle):
    def __init__(self, manufactor, model, year, type, trailer_locked, fuel_level):
        super().__init__(manufactor, model, year, type)
        self.trailer_locked = trailer_locked
        self.fuel_level = fuel_level

    @classmethod
    def vehicle_type(cls):
        print("Tractor")

    def start(self):
        if self.trailer_locked and self.fuel_level > 0:
            print(f" starts {self.manufactor}")
            self.started = True
            print(f"{self.manufactor} is starting")
        else:
            if not self.trailer_locked:
                print(f"{self.manufactor} cannot start because trailer is not locked")
            else:
                print(f"{self.manufactor} cannot start because fuel level is 0")

    def stop(self):
        print(f" stops {self.manufactor}")
        self.started = False
        print(f"{self.manufactor} is stopped")


class JohnDeereTractor(Tractor):
    @classmethod
    def vehicle_type(cls):
        print("John Deere Tractor")


# Example usage
johndeere = JohnDeereTractor("John Deere", "Model X", 2023, "Tractor", True, 75)
johndeere.start()
johndeere.vehicle_type()

        





        
        
        
        