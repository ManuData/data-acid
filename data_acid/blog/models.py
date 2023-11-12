from django.db import models

# Create your models here.

class Articles(models.Model):
   
    # Articles Metadata: 

    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title  
    


