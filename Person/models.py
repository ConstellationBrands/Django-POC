from django.db import models



class Person(models.Model):

    name = models.TextField()

    company = models.TextField()

    city = models.TextField()
