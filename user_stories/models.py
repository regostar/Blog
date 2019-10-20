from django.db import models
from django_mysql.models import JSONField # Otherwise use postgresql db
# Create your models here.

class User(models.Model):
    models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=256, unique=True)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    # company if required in future, we can add Foreign Key here to Company Table which has name, bs, catchPhrase, etc..
