"""
Тут написати умову до завдання
"""
def get_elem(a):
    if len(a)==1:
        if(a[0]%2!=0):
            print(a[0])
        else:
            return
    else:
        if (a[0] % 2 != 0):
            print(a[0])
            get_elem(a[1:])
        else:
            get_elem(a[1:])
list=[1,2,3,4,5,6,7,8,9]
get_elem(list)

#TODO