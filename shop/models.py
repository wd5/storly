from django.db import models


class Settings(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    domain = models.CharField(max_length=30)
    subdomain = models.CharField(max_length=30)
    wow = models.CharField(max_length=60)

    def __unicode__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    url = models.CharField(max_length=50)
    href = models.CharField(max_length=100)
    background = models.CharField(max_length=50)


    def __unicode__(self):
        return self.title

class Pages(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=60)
    content = models.TextField()
    menu = models.NullBooleanField()
    menu_title = models.CharField(max_length=25)
    with_goods = models.NullBooleanField()


    def __unicode__(self):
        return self.title
