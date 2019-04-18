from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class photo(models.Model):
    Img = models.ImageField(upload_to='images/',blank=True,null=True,default=None)


class expense_table(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    expense_date = models.DateTimeField('date')
    cost =  models.FloatField(default=0)
    image = models.ForeignKey(photo,on_delete=models.CASCADE,blank=True,null=True)




