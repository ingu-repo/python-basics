#
# Python Class 
# - No private controller, so every class variable/method are public accessible
# - Inside of class, need to use self to access variable/method
#
class Person:
    name = ""
    _last_name = ""
    _first_name = ""
    age = 0

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
        
    def validation_check(self):
        if (self._first_name == "" or self._last_name == "" or self.age == 0):
            raise Exception("person information is not enough")
        
    def class_method_name():
        print ("self is missing")

person = Person()
person._first_name = "Mike"
person._last_name = "Sonoma"
person.age = 23
person.check_health(90)

# causing error because the method has no self param
# but code itself has no compilation error, only run time error when the method called
person.class_method_name()  



