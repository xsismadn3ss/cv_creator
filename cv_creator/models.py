from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CV(models.Model):
    title = models.CharField(max_length=100, default="My CV")
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=100, default="")
    phone = models.CharField(default="", max_length=20)
    urls = models.CharField(default="", max_length=255)
    job = models.CharField(max_length=60, null=False)
    about = models.CharField(default="", max_length=1500)
    exp = models.CharField(null=False, max_length=1500)
    edu = models.CharField(null=False, max_length=1500)
    top_skills = models.CharField(null=False, max_length=255)
    soft_skills = models.CharField(null=False, max_length=255)
    lang = models.CharField(null=False, max_length=255)

    # foreign key
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
