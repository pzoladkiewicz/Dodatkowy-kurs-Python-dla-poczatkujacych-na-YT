employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "r")            # r, w, a, r+
print(employee_file.read())
employee_file.close()

###########################################

# append - add at the end of the file

employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "a")            
employee_file.write("\nToby - Human Resources")
employee_file.close()

###########################################

# overwrite the file

employee_file =  open(r"C:\GiraffeAcademy\employees.txt", "w")            
employee_file.write("\nToby - Human Resources")
employee_file.close()


# or create new if not exists

employee_file =  open(r"C:\GiraffeAcademy\employees_2.txt", "w")            
employee_file.write("\nToby - Human Resources")
employee_file.close()
