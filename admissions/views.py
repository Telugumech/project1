from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from admissions.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required
from admissions.models import careTaker








# Create your function based views here. 

#@login_required
def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')


@login_required
def addAdmission(request):
    form = StudentModelForm
    studentform = {'form':form}

    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return homepage(request)

    return render(request,'admissions/add_admission.html',studentform)

@login_required
def admissionReport(request):
    result = Student.objects.all();
    students = {'allstudents':result}
    return render(request,'admissions/admission_report.html',students)

@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s = Student.objects.get(id = id)
    s.delete()
    return admissionReport(request)

@login_required
@permission_required('admissions.change_student') #add ,delete,view,change,
def updateStudent(request,id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form':form}

    if request.method == "POST":
        form = StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return homepage(request)

    return render(request,'admissions/update_admission.html',dict)




#class based views
class classBasedView(View):
    def get(self,request):
        return render(request,'admissions/classbased.html')


class TeacherRead(ListView):
    model = Teacher


class GetTeacher(DetailView):
    model = Teacher


class Addteacher(CreateView):
    model = Teacher
    fields = ('Teacher_name','Father_name','Experriance','mobile_no',
    'Qualification','Date_of_joining')

class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('Teacher_name','Father_name','Experriance','mobile_no',
    'Qualification','Date_of_joining')

class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteacher')




class Addcaretaker(CreateView):
    model = careTaker
    fields = ('student_name','group','roll_no','year',
    'admission_no','father_name','mother_name','caste_subcaste','ssc_marks_grade','ssc_reg_no',
    'month_passing_year','dob','father_occupation','rationcard_no','annual_income','adhaar_no',
    'grama_sachivalyam','mobile_no','blood_group','address')

class caretakerRead(ListView):
    model = careTaker


class GetcareTaker(DetailView):
    model = careTaker
    


class Updatecaretaker(UpdateView):
    model = careTaker
    fields = ('student_name','group','roll_no','year',
    'admission_no','father_name','mother_name','caste_subcaste','ssc_marks_grade','ssc_reg_no',
    'month_passing_year','dob','father_occupation','rationcard_no','annual_income','adhaar_no',
    'grama_sachivalyam','mobile_no','blood_group','address')


class DeletecareTaker(DeleteView):
    model = careTaker
    success_url = reverse_lazy('listcaretaker')




    
    
    
    


    



 
