class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name =  last_name
        self.birth_year = birth_year
        self.student_id = self.name[0] + self.last_name + str(self.birth_year)
        # calculate the student_id here
chuj = Student(input() , input()  , input())
# stri = "jan"
# print (stri[1])
print (chuj.student_id)
