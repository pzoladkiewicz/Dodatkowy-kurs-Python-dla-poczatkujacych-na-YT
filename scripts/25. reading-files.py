employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "r")            # r, w, a, r+

print(employee_file.readable())
print(employee_file.read())

employee_file.close()

###########################################

employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "r")           

print(employee_file.readline())
print(employee_file.readline())

employee_file.close()

###########################################

employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "r")           

print(employee_file.readlines())             # put lines in list

employee_file.close()

###########################################

employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "r")            

print(employee_file.readlines()[1])             # print 

employee_file.close()

###########################################

employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "r")            
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
