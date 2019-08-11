from django.shortcuts import render
from pages.models import Names
from pages.choices import year, sex


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        startyear = request.POST["startyear"]
        endyear = request.POST["endyear"]
        sex = request.POST["BG"].lower()
        yearsearch = Names.objects.filter(year__range=(startyear, endyear))
        sexsearch = yearsearch.filter(sex=sex)
        names = sexsearch.filter(name__iwithin=name)
        context = {"names": names, "sex": sex, "years": year}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
 