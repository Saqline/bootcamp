class Person:
    def introduce(self):
        print("I am a person.")

class Student(Person):
    def introduce(self):
        print("I am a student.")

# Example usage
person = Person()
student = Student()

person.introduce()  
student.introduce() 
