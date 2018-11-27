from data import dataset

#   Написати функцію, що додає студента з певним квитком та навичкою
#   Викликати функцію


def addStudentSkill(student, company, skill):
    #TODO
    if student in dataset:
        for ele in dataset[student]["companies"]:
            if company in ele:
                ele[company].add(skill)
            else:
                dataset[student]["companies"].append({company:{skill}})
    else:
        name=input("name\n")
        surname=input("surname\n")
        age=int(input("age\n"))
        dataset[student]={
        "personal_data":{
            "name":name,
            "surname":surname,
            "age":age
        },
        "companies":[{company:{skill}}],
    }



print("Task 1")

#Додати нового студента та вміння у новій компанії
addStudentSkill("KB-15151515","mersedes","driving")

#Додати існуючому студенту нове вміння у новій компанії
addStudentSkill("KB-12121212","oshchad","runing")

#Додати існуючому студенту нове вміння в існуючій компанії
addStudentSkill("KB-12121212","privat24","coding")

print(dataset)


print("\n\n")