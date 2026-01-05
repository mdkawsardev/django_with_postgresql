from django.db import models
from datetime import datetime
# Create your models here.
class Mycontact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    pub_date = models.DateTimeField(default=datetime.now)