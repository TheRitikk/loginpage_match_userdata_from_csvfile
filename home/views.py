from django.shortcuts import render, redirect
import csv

# Create your views here.
def index(request):
    queryDict = dict(request.POST)
    list1 = queryDict.values()
    list2 = list(list1)
    list3 = list2[1:3]
    # print(list3)
    with open('Userdata.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # print(row)
            row1 = [[row[0]], [row[1]]]
            # row1 = list(row[0], row[1])
            # row1.append(row(1))
            # for i in range(len(row)):
            #     row1.append(row[1])
            # print(row1)
            if row1 == list3:
                # print("Equal")
                return redirect('/main')
                # return render(request,"main.html")
            # else :
            #     print("Not match")
    return render(request,"index.html")

def main(request):
    return render(request,"main.html")
