import os
from pages.models import Name

def filedata():
    ct = 0
    lst = os.listdir(os.path.join(os.curdir,'name'))
    for i in lst:
        year = int(i[3:7])
        print(year)
        path = os.path.join('name',i)
        results = process_data(path,year)
        if results % 10000 == 0:
            print(results)
    return results



def process_data(path,year):
    with open(path,'rt') as f:
        lines = f.readlines()
        for line in lines:
            a = get_elements(line,year)
    return a




def get_elements(line,year):
    lst = line.split(',')
    if len(lst) > 1:
        name = lst[0]
        if lst[1] == "M":
            sex = "Boy"
        elif lst[1] == "F":
            sex = "Girl"
        amount = int(lst[-1])
        entry = Name(name=name,sex=sex,amount=amount,year=year)
        entry.save()
    return 1
