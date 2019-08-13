from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    amount = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.name


class QueryObject:
    def __init__(self,name,sex,start,end):
        self.name = name
        self.sex = sex
        self.sart = start
        self.end = end

    def get_data(self):
        qfilter = Name.objects.filter(year__range=(self.start,self.end))
        if self.sex != "Both":
            qfilter = qfilter.filter(sex=self.sex)
        exact_data = qfilter.filter(name__iexact=self.name)
        total = 0
        for qry in exact_data:
            total += qry.amount
        context = {"data":exact_data,"total":total}
        return context
