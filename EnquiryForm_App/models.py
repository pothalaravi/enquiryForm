from django.db import models
from multiselectfield import MultiSelectField


class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.BigIntegerField(unique=True)

    course_choices = [
        ('python', 'python'),
        ('Django', 'Django'),
        ('MySQL', 'MySQL')
    ]

    course = MultiSelectField(choices=course_choices)

    location_choices = [
        ('hyderabad', 'hyderabad'),
        ('pune', 'pune'),
        ('mumbai', 'mumbai')
    ]

    location = MultiSelectField(choices=location_choices)
    start_date = models.DateField()
    gender = models.CharField(max_length=10)
