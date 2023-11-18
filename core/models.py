from django.db import models

# Create your models here.
class Home1FirstSpace(models.Model):
    image = models.ImageField(upload_to="user_info/")
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    button = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Home1AboutUs(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    def __str__(self):
        return self.name
    
class Home1Icon(models.Model):
    icon_link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.icon_link

class Home1Info(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def  __str__(self):
        return self.title

class Home1ListInfo(models.Model):
    name = models.CharField(max_length=20)
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.name
