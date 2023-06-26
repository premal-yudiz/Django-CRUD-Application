from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    password = models.CharField(max_length=80)

    def __str__(self):  
        return "%s %s %s" % (self.name, self.email, self.password)  