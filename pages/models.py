from django.db import models
import time
# Create your models here.


class Team(models.Model):
    fname  = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    desig = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d') # need to install pillow 
    fb_link = models.URLField (max_length=300)
    twitter_link = models.URLField (max_length=120)
    g_link = models.URLField (max_length=120)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.fname} - {self.lname}"


