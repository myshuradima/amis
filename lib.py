import re
sdudent_name=input("student name")
def student_valid():
    sdudent_name = input("student name")
    if (re.match(r"^[A-Z]{2}\-\d{8}$",student_name)):
        return student_name
    else:
        return False
def company_valid():
    company = input("company")
    if (re.match(r"^[a-z]{0,10}\d*$",student_name)):
        return company
    else:
        return False
