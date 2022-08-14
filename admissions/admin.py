from django.contrib import admin
from admissions.models import Student
from admissions.models import Teacher
from admissions.models import careTaker




class StudentAdmin(admin.ModelAdmin):
    list_display = ['sname','fname','group','mobile_no','amount_paid','date']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['Teacher_name','Father_name','Experriance','mobile_no','Qualification','Date_of_joining']

class careTakerAdmin(admin.ModelAdmin):
    list_display = ['student_name','group','roll_no','year','admission_no','father_name','mother_name','caste_subcaste','ssc_marks_grade',
    'ssc_reg_no','month_passing_year','dob','father_occupation','rationcard_no','annual_income','adhaar_no','grama_sachivalyam','mobile_no','blood_group','address'
    ]

# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(careTaker,careTakerAdmin)





