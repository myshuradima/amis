import os.path
import plotly
import plotly.graph_objs  as go
from reg_lib import*
file = open("/home/dima/amis/amis/example/Tereshchenko_Igor/workshop5/source/data/orders.csv")
info = file.read()
lines = info.splitlines()
print(len(lines))
data = dict()
keys=lines[0].split(",")
values=lines[1].split(",")
values1=lines[2].split(",")
bigdata=[]
dict1={}
n=1
while n<len(lines):
    values=lines[n].split(",")
    for index in range(len(keys)):
        data[keys[index]] = values[index]
    bigdata.append(data)
    data=dict()
    n=n+1
#print(data[keys[0]])
for ele in bigdata:
    if ele["client"] in dict1.keys():
        dict1[ele["client"]].append(ele)
    else:
        dict1[ele["client"]]=[ele]
arr1=[]
for ele in dict1.values():
    arr=[]
    for elem in ele:
        arr.append(elem[" product"])
        arr1.append(arr)
    print(arr)
result =list(set(arr1[0]) & set(arr1[1]))
def wanted(arra):
    intersect=set(arra[0]).intersection(arra[1])
    for ele in arra:
        a=set(intersect).intersection(ele)
    print(a)
wanted(arr1)
def graph(diction):
    a=[]
    b=[]
    for elem in diction.values():
        for element in elem:
            if element[" product"] == " apple":
                a.append(element[" price"])
                b.append(element[" date"])
    diagram=go.Bar(x=b,
                     y=a
                       )
    plotly.offline.plot([diagram], filename = "applesprice.html")
#graph(dict1)
def money(diction):
    s=0
    a=[]
    b=[]
    for name, all in diction.items():
        a.append(name)
        for ele in all:
            s=s+float(ele[" price"])
        b.append(s)
        s=0
    diagram=go.Pie(
        values=b,
        labels=a
        )
    plotly.offline.plot([diagram], filename="money.html")
#money(dict1)
def new_data(dict):
    ele={"client":get_client()," date":get_date()," product":get_product()," quantity":get_quantity()," price":get_price()}
    if ele["client"] in dict.keys():
        dict[ele["client"]].append(ele)
    else:
        dict[ele["client"]]=[ele]
def most_expensive(dictionary):
    prod=[]
    price=[]
    for ele in dictionary.values():
        for elem in ele:
            prod.append(elem[" product"])
            price.append(float(elem[" price"]))
    index1=price.index(max(price))
    print(prod[index1])
#most_expensive(dict1)
new_data(dict1)
def most_wanted(dictionary):
    dict3=dict()
    ammount=[]
    for ele in dictionary.values():
        for elem in ele:
            if elem[" product"] in dict3.keys():
                a=dict3[elem[" product"]]
                a=a+1
                dict3[elem[" product"]]=a
            else:
                dict3[elem[" product"]]=1
    for ele in dict3.values():
        ammount.append(ele)
    a=max(ammount)
    b=min(ammount)
    for key,ele in dict3.items():
        if(ele==a):
            print("max-",key)
        elif(ele==b):
            print("min-",key)
    print(dict3)
#most_wanted(dict1)
print(dict1)
#print(bigdata[0]["client"])
#print (set(arr1[0]).intersection(arr1[1]))
file.close()
