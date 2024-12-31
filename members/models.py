from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    joining_date = models.DateField()
    department = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    spouse_name = models.CharField(max_length=255, null=True, blank=True)
    religion = models.CharField(max_length=50, choices=[
        ('Islam', 'Islam'),
        ('Hindu', 'Hindu'),
        ('Buddha', 'Buddha'),
        ('Christian', 'Christian'),
        ('Others', 'Others'),
    ])
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ])
    permanent_address = models.TextField()
    present_address = models.TextField()
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=11)
    phone_office = models.CharField(max_length=15, null=True, blank=True)
    phone_residence = models.CharField(max_length=15, null=True, blank=True)
    blood_group = models.CharField(max_length=10, choices=[
        ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('Others', 'Others'),
    ])
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    signature = models.ImageField(upload_to='signatures/')

    def __str__(self):
        return self.name
