from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

# this is the method to send the data to the database i.e (sql lite)
# for the database to work properly we need to register this myapp directory in the myproject directory.
# for the registeration open settings.py file and under the [INSTALLED_APPS = myapp] write this in the next line. 