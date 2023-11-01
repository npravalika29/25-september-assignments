class School:
    def __init__(self,name,location,num_students,num_teachers,facilities):
       self.name = name
       self.location = location
       self.students = num_students
       self.faculty = num_teachers
       self.facilities = facilities
School1 = School("KTR High School","city A ", 1000,50,4.5)
School2 = School("XYZ Elementary school","city B",400,20,2.0)
print(School1.name)  
print(School1.students)
print(School1.location)
print(School1.faculty)
print(School1.facilities)

print(School2.name)
print(School2.students)
print(School2.location)  
print(School2.faculty)
print(School2.facilities)
