from django.db import models
from django.urls import reverse



# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    amount_paid = models.IntegerField()
    date = models.CharField(max_length=50)



class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=50)
    Father_name = models.CharField(max_length=50)
    Experriance = models.IntegerField()
    mobile_no = models.IntegerField()
    Qualification = models.CharField(max_length=50)
    Date_of_joining = models.CharField(max_length=50)
    
    def get_absolute_url(self):
        return reverse('listteacher')


class careTaker(models.Model):
    student_name = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    year = models.IntegerField()
    admission_no = models.IntegerField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    caste_subcaste = models.CharField(max_length=50)
    ssc_marks_grade = models.IntegerField()
    ssc_reg_no = models.IntegerField()
    month_passing_year = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=50)
    rationcard_no = models.IntegerField()
    annual_income = models.IntegerField()
    adhaar_no = models.IntegerField()
    grama_sachivalyam = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('listcaretaker')


    
    
    




    
    
    



        