lst=[3,56,7,3523,124,53,234]
def func1(a,i=0):
    if(i*3>len(a)):
        return
    else:
        print(a[i*3])
        func1(a,i+1)
func1(lst)
a=int(input("1"))
b=int(input("2"))
k=0
while(a<b):
    if(a%2==1):
        k=k+1
    a=a+1
print(k)
str=input("str")
s=""
for ele in str.split():
    s=s+" "+ele.title()
print(s[1:])
dataset=dict()
n="+"
while(n=="+"):
    strdat=input().split()
    if(strdat[0] in dataset.keys()):
        dataset[strdat[0]].append(strdat[1:])
    else:
        dataset[strdat[0]]=strdat[1:]
    n=input()
print(dataset)
Ages={"Bob":45,
      "Boba":20,
      "Biba":28,
      "Ben":67,
      "Gnom":37}
a=[]
for ele in Ages.values():
    a.append(ele)
a.sort()
print(a)
x=-1
while x>-4:
    for key,ele in Ages.items():
        if ele==a[x]:
            print(key)
    x=x-1