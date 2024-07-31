from django.db import models

# Create your models here.

class Category_Details(models.Model):
    categoryid=models.CharField(max_length=500)
    category=models.CharField(max_length=100)

class Scheme_Details(models.Model):
    category=models.CharField(max_length=100)
    schemeid=models.CharField(max_length=20)
    schemename=models.CharField(max_length=100)
    ministry=models.CharField(max_length=200)
    details=models.CharField(max_length=2000)
    benefits=models.CharField(max_length=2000)
    application=models.CharField(max_length=5000)
    state=models.CharField(max_length=500)
    documentsrequired=models.CharField(max_length=5000)
    

class User_Registration_Table(models.Model):
    fullname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=100)
    fulladdress=models.CharField(max_length=500)
    state=models.CharField(max_length=100)
    zip=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.CharField(max_length=100)
    mstatus=models.CharField(max_length=100)
    aor=models.CharField(max_length=100)
    caste=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    age=models.CharField(max_length=10)
    ph=models.CharField(max_length=50)
    minority=models.CharField(max_length=50)
    student=models.CharField(max_length=50)
    empstatus=models.CharField(max_length=50)
    currempstatus=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    annualincome=models.CharField(max_length=50)

class Eligibility_Table(models.Model):
    schemeid=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    mstatus=models.CharField(max_length=100)
    mage=models.CharField(max_length=50)
    maxage=models.CharField(max_length=50)
    aor=models.CharField(max_length=100)
    caste=models.CharField(max_length=100)
    ph=models.CharField(max_length=50)
    minority=models.CharField(max_length=50)
    student=models.CharField(max_length=50)
    empstatus=models.CharField(max_length=50)
    currempstatus=models.CharField(max_length=50)
    occupation=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    annualincome=models.CharField(max_length=50)

