from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=128, blank=False)
    description = models.TextField(null=True)
    specialist = models.CharField(max_length=64, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='static/website/images/employee')

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=64)
    history = models.TextField()
    photo = models.ImageField(null=True, blank=True, upload_to='static/website/images/customer')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    time = models.TimeField()
    person = models.ForeignKey(Employee, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='static/website/images/service')

    def __str__(self):
        return self.name


class Message(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.first_name
