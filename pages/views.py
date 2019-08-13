from django.shortcuts import render
from pages.models import Name, QueryObject
from pages.choices import year as year_choices
from pages.choices import sex as sex_choices


def index(request):
        context = {}
        return render(request, 'pages/index.html',context)


def injax(request):
    if request.method == "POST":
        name =  request.POST["name"]
        sex = request.POST["sex"]
        start_year = request.POST["start_year"]
        end_year = request.POST["end_year"]
        query = QueryObject(name,sex,start_year,end_year)
        context = query.get_data()
        return render(request,"partials/_table.html",context)
