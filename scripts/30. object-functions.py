from Student_f import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 4.5, True)

print(student1.name)                            #   Jim
print(student2.gpa)                             #   4.5

print(student1.on_honor_roll())                 #   3.1         ==> False
print(student2.on_honor_roll())                 #   4.5         ==> True
