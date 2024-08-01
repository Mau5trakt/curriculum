from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255)
    birthday = models.DateField(auto_now=False, auto_now_add=False, default='2024-01-01')
    phone_number = models.CharField(max_length=20)

    class Meta:
        app_label = 'cv'


class PersonalInformation(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    information = models.CharField(max_length=255)

    class Meta:
        ordering = ['-date']


class WorkExperience(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-from_date']


class Language(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    where = models.CharField(max_length=255)


class Course(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['-from_date']


class ProgrammingExperience(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    ability = models.CharField(max_length=255)
    h_type = models.CharField(max_length=255)


class Achievement(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, default='2024-01-01')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    class Meta:
        ordering = ['-date']


class Additional(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now=False, auto_now_add=False)
    to_date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ['-from_date']

