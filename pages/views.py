from django.shortcuts import render
from pages.models import Name
from pages.choices import year as year_choices
from pages.choices import sex as sex_choices


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        startyear = request.POST["startyear"]
        start = int(startyear)
        endyear = request.POST["endyear"]
        end = int(endyear)
        sex = request.POST["sex"]
        sexsearch = Name.objects.filter(sex=sex)
        results = sexsearch.filter(name__icontains=name)
        data = [name,start,end,sex,sexsearch]
        context = {"results": results, "sex": sex_choices, "years": year_choices,"data":data}
        return render(request, 'index.html', context)
    else:
        context = {"sex": sex_choices, "years": year_choices}
        return render(request, 'index.html',context)
