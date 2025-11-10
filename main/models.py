from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
      name = models.ForeignKey(User, on_delete=models.CASCADE)
      specialization = models.CharField(max_length=50)
      def __str__(self):
          return self.name

class Patient(models.Model):
      name = models.CharField(max_length=100)
      age = models.IntegerField()
      gender = models.CharField(max_length=10)
      doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
      def __str__(self):
          return self.name

class Result(models.Model):
      patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
      test_name = models.CharField(max_length=100)
      result_value = models.CharField(max_length=50)
      unit = models.CharField(max_length=50)
      normal_range = models.CharField(max_length=50)
      date = models.DateTimeField(auto_now_add=True)
      def __str__(self):
          return f'{self.patient.name} - {self.test_name}'

# Create your models here.
