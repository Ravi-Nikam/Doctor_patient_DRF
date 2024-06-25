from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin
from doctor.manager import UserManager

# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    username=None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone_number  = models.IntegerField(null=True)
    user_type = models.CharField(max_length=1,choices=[('D', 'Doctor'), ('P', 'Patient')])

    # required fields
    
    is_staff =models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone_number','user_type']


    objects = UserManager()

    def __str__(self):
        return self.email



# models.py
class Patient(models.Model):
    Doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    medical_history = models.TextField()



# models.py
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    date_prescribed = models.DateTimeField(auto_now_add=True)
