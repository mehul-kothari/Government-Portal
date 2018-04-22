from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.forms import extras
from django.forms import forms
from django.core.files.storage import FileSystemStorage
from government import settings



CATEGORIES = (
    ('Mumbai Central', 'Mumbai Central'),
    ('Goregaon', 'Goregaon'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)










class Area(models.Model):
    user = models.OneToOneField(User)
    area1 = models.CharField(max_length=50,choices=CATEGORIES)

    def __str__(self):  # __unicode__ on Python 2
        return self.area1

class Locality(models.Model):
    user = models.OneToOneField(User)
    area2 = models.ForeignKey(Area, on_delete=models.CASCADE,)
    locality1 = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.locality1)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to='photo',
                              default="photo/765-default-avatar.png")

    def __str__(self):  # __unicode__ on Python 2
        return str(self.photo)


class GeneralProblems(models.Model):
    problem=models.CharField(max_length=60)




    def __str__(self):  # __unicode__ on Python 2
        return self.problem

class Areas(models.Model):
    areas1 = models.CharField(max_length=60)

    def __str__(self):  # __unicode__ on Python 2
        return self.areas1

class Localities(models.Model):
    localities1 = models.CharField(max_length=60)
    areas2=models.ForeignKey(Areas,on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.localities1

# Create your models here.

class form2(models.Model):
    details=models.CharField(max_length=500)
    genproblems=models.ForeignKey(GeneralProblems, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=500, default="No Heading")
    created = models.DateTimeField(auto_now_add=True,null=True)
    done=models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photo1',null=True)

    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return '{}'.format(self.details)


class Likes(models.Model):
    likes=models.BooleanField(default=False)
    details=models.ForeignKey(form2, on_delete=models.CASCADE)
    user1=models.ForeignKey(User, on_delete=models.CASCADE)
    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return str(self.details)



class Discussion(models.Model):
    detail_id=models.IntegerField()
    user_create=models.ForeignKey(User, on_delete=models.CASCADE)
    user_write=models.CharField(max_length=100)
    comment=models.CharField(max_length=1000)
    type=models.CharField(max_length=10,default="normal")
    created = models.DateTimeField(auto_now_add=True, null=True)
    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return str(self.comment)

class Likes2(models.Model):
    likes=models.BooleanField(default=False)
    comment=models.ForeignKey(Discussion, on_delete=models.CASCADE)
    user1=models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, default="normal")
    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return str(self.comment)





class Notifications(models.Model):
    message=models.CharField(max_length=1000)
    user_create=models.ForeignKey(User, on_delete=models.CASCADE)
    user_write=models.CharField(max_length=100)
    checked=models.BooleanField(default=False)
    urls1=models.CharField(max_length=1000,default="/login/home/Railway/")
    type = models.CharField(max_length=10, default="normal")
    created = models.DateTimeField(auto_now_add=True, null=True)
    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return str(self.user_create)


class SpecificLocality(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000)
    area=models.ForeignKey(Areas , on_delete=models.CASCADE)
    locality = models.ForeignKey(Localities , on_delete=models.CASCADE)
    heading = models.CharField(max_length=500, default="No Heading")
    created = models.DateTimeField(auto_now_add=True, null=True)
    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return str(self.comment)

class Likes1(models.Model):
    likes=models.BooleanField(default=False)
    comment=models.ForeignKey(SpecificLocality, on_delete=models.CASCADE)
    user1=models.ForeignKey(User, on_delete=models.CASCADE)
    #likes=models.CharField(max_length=10,default="nolike")
    def __str__(self):  # __unicode__ on Python 2
        return str(self.comment)


class SpecificProblems(models.Model):
    spec_problem=models.CharField(max_length=100)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.spec_problem)