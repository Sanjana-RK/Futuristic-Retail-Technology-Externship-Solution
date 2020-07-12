from django.db import models
from django.contrib.auth.models import User

# This code is for the creation of models, here I have created Storemodel
class Storemodel(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.PROTECT)


    def __str__(self):
        return self.title
