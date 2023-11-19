from django.db import models

# Create your models here.

class Articles(models.Model):
   
    # Articles Metadata: 

    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title  
    


class LeadsForm(models.Model):
    profesion = models.CharField(max_length=100)
    salary_range = models.IntegerField()
