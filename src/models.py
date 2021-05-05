from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.OneToOneField(User, default = 1, on_delete = models.SET_DEFAULT,primary_key = True)
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 200)

    def __str__(self):
        return self.title