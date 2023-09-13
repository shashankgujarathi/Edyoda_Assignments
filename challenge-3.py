class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
    
    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber
    
student_obj = Student()

student_obj.setName('Shashank')
student_obj.setRollNumber('0411')

print(student_obj.getName())
print(student_obj.getRollNumber())