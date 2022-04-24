from django.db import models


# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=256)
    description = models.TextField()
    salary_min = models.CharField(max_length=64)
    salary_max = models.CharField(max_length=64)
    published_at = models.DateField()


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64)
    logo = models.URLField()
    description = models.TextField()
    employee_count = models.CharField(max_length=64)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    picture = models.URLField()
