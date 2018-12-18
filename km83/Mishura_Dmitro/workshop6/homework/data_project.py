import re
import plotly
import plotly.graph_objs as go
from plotly import tools

def get_num(line):
    result=re.split(r",", line, maxsplit=1)
    result1=re.findall(r"\d+", result[0])
    return result1, result[1]
def get_country(line):
    result=re.split(r",",line, maxsplit=1)
    result1=re.findall(r"([A-Z][a-z]+|[A-Z]+)", result[0])
    return result1, result[1]
def get_description(line):
    if(line[0]=="\""):
        result=re.split(r"\"", line, maxsplit=2)
        return result[1], result[2]
    else:
        result = re.split(r",", line, maxsplit=1)
        return result[0], result[1]
def get_designation(line):
    result=re.split(",", line, maxsplit=2)
    return result[1], result[2]
def get_points(line):
    result=re.split(",", line, maxsplit=1)
    result1=re.findall(r"\d{1,2}", result[0])
    return result1, result[1]
def get_price(line):
    result=re.split(r",", line, maxsplit=1)
    result1=re.findall(r"\d{1,2}\.\d", result[0])
    return result1, result[1]
def get_province(line):
    result=re.split(r",", line, maxsplit=1)
    return result[0], result[1]
def get_title(line):
    result=line.split(",")
    return result[5]
def amount_of_vines(dic):
    s=0
    dict1=dict()
    for key, val in dic.items():
        for ele in val.values():
            s=s+len(ele)
        dict1[key]=s
        s=0
    return dict1
def first_graph(dic):
    countries=[]
    amount=[]
    for key, val in dic.items():
        countries.append(key)
        amount.append(val)
    diagram1=go.Bar(
        x=countries,
        y=amount
    )
    #plotly.offline.plot([diagram], filename="firstgraph.html")
    return diagram1
def sum_points(dic):
    dict2=dict()
    s=0
    for key, val in dic.items():
        for elem in val.values():
            for eleme in elem.values():
                if not eleme["points"]:
                    s=s+0
                else:
                    s=s+float(eleme["points"][0])
        dict2[key]=s
        s=0
    return dict2
def graph2(dic):
    countries=[]
    sum_points=[]
    for key, val in dic.items():
        countries.append(key)
        sum_points.append(val)
    diagram = go.Pie(labels=countries, values=sum_points)
    #plotly.offline.plot([diagram], filename="secondgraph.html")
    diagram2 = go.Bar(
        x=countries,
        y=sum_points
    )
    return diagram2
def max_price(dic):
    dict3 = dict()
    s = 0
    for key, val in dic.items():
        for key1, elem in val.items():
            for eleme in elem.values():
                if not eleme["price"]:
                    s = s + 0
                else:
                    if s<float(eleme["price"][0]):
                        s=float(eleme["price"][0])
            dict3[key1] = s
        s = 0
    return dict3
def graph3(dic):
    provinces = []
    big_price = []
    for key, val in dic.items():
        provinces.append(key)
        big_price.append(val)
    diagram3 = go.Bar(
        x=provinces,
        y=big_price
        )
    #plotly.offline.plot([diagram], filename="thirdgraph.html")
    return diagram3
def all_togeather(diagram1, diagram2, diagram3):
    fig = tools.make_subplots(rows=1, cols=3)
    fig.append_trace(diagram1, 1, 1)
    fig.append_trace(diagram2, 1, 2)
    fig.append_trace(diagram3, 1, 3)
    plotly.offline.plot(fig, filename='myplotly1.html')
try:
    current_line=0
    with open("data/data.csv") as file:
        header=file.readline().rstrip()
        dataset=dict()
        header_nice= [ colum.strip().upper() for colum in header.split(",")]
        #product_index= header_nice.index("COUNTRY")
        for line in file:
            line1=line.split(",")
            number, rest = get_num(line)
            #print(number[0])
            country, rest = get_country(rest)
            #print(country[0])
            description, rest = get_description(rest)
            #print(description)
            designation, rest = get_designation(rest)
            #print(designation)
            points, rest = get_points(rest)
            #print(points)
            price, rest = get_price(rest)
            #print(price)
            province, rest = get_province(rest)
            #print(province)
            title=get_title(rest)
            #print(title)
            #print(line1[product_index])
            if country[0] not in dataset:
                dataset[country[0]]=dict()
            if province not in dataset[country[0]]:
                dataset[country[0]][province]=dict()
            if title not in dataset[country[0]][province]:
                dataset[country[0]][province][title]={"points":points,
                                                      "price":price}
        #for key,ele in dataset.items():
        #print(amount_of_vines(dataset))
        print(dataset)
        dictionar=sum_points(dataset)
        d2=graph2(dictionar)
        diction=amount_of_vines(dataset)
        d1=first_graph(diction)
        dicti=max_price(dataset)
        d3=graph3(dicti)
        all_togeather(d1, d2, d3)
        print(dicti)
except IOErrors as io_errors:
    print("error", io_error.strerror)

