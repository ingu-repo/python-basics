# ----------------------------------------------------------
# Class
# 
# Private Access 
# - No private controller in Python, so every class variable/method is public accessible
# - Inside of class, need to use self to access variable/method
#
# Call Parent class method
# - super().METHOD(PARAMS)
# - PARENT_CLASS_NAME.METHOD(self, PARAMS)
#
# Variables in method
# - self.VARIRABLE  : instance variable
# - VARIABLE        : local variable
#
# ----------------------------------------------------------
class Person:
    # name = ""
    # _last_name = ""
    # _first_name = ""
    # age = 0
    def setLastName(self, lastname):
        self._last_name = lastname

    def setFirstName(self, firstname):
        self._first_name = firstname

    def getName(self):
        return self._first_name + " " + self._last_name
    
    def check_health(self, weight):
        self.build_person()
        if (weight < 60):
            print (f"Hello {self.name}, you are good")
        elif (weight < 80):
            print (f"Hello {self.name}, you need to be careful")
        else:
            print (f"Hello {self.name}, you need health check")

    def build_person(self):
        self.validation_check()
        self.name = f"{self._first_name} {self._last_name}"
        name = "oh my dummy name"
        
    def validation_check(self):
        if (self._first_name == "" or self._last_name == "" or self.age == 0):
            raise Exception("person information is not enough")
        
person = Person()
person._first_name = "Mike"
person._last_name = "Sonoma"
person.age = 23
person.check_health(90)

class Employee(Person):
    def getName(self):
        return super().getName()

    def setFirstName(self, firstname):
        # Person.setFirstName(firstname)    # ERROR
        Person.setFirstName(self, firstname)

    def setLastName(self, lastname):
        super().setLastName(lastname)       # OK
    
employee = Employee()
employee.setFirstName("Pole")
employee.setLastName("Traffans")
print ("Name: ", employee.getName())



