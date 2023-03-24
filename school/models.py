from django.db import models

# Create your models here.

CITY = (
    ("Purnea", "Purnea"),
    ("Patna", "Patna"),
    ("Bhagalpur", "Bhagalpur"),
    ("Bhopal", "Bhopal"),
    ("indore", "indore"),
    ("Delhi", "Delhi"),
    ("Kolkata", "Kolkata"),
)

class Students(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=200, choices=CITY)
    state = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
