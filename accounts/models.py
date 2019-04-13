from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class expense_table(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    expense_date = models.DateTimeField('date')
    cost =  models.FloatField(default=0)
    image = models.ImageField(blank=True,null=True)
