from django.db import models
import datetime

# Create your models here.

class Blog(models.Model):
    alumini = models.CharField(max_length=200)
    years = [(r,r) for r in range(1970, datetime.date.today().year+1)]
    passed_out_year = models.IntegerField(choices=years, default=datetime.datetime.now().year)
    company_names = (
        ('Google', 'Google'),
        ('Ashok Leyland', 'Ashok Leyland'),
        ('Accsenger', 'Accsenger'),
        ('Caterpiller', 'Caterpillar'),
    )
    company = models.CharField(max_length=200, choices=company_names)
    salary = models.CharField(max_length=50)
    description = models.TextField(default='', null=True)

    def __str__(self):
        return self.alumini


