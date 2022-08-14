from django.urls import path
from admissions.views import addAdmission
from admissions.views import admissionReport
from admissions.views import deleteStudent
from admissions.views import updateStudent
from admissions.views import classBasedView
from admissions.views import TeacherRead
from admissions.views import GetTeacher
from admissions.views import Addteacher
from admissions.views import UpdateTeacher
from admissions.views import DeleteTeacher
from django.contrib.auth.decorators import login_required
from admissions.views import Addcaretaker
from admissions.views import caretakerRead
from admissions.views import GetcareTaker
from admissions.views import Updatecaretaker
from admissions.views import DeletecareTaker







urlpatterns = [

    path('new/', addAdmission),
    path('report/', admissionReport),
    path('delete/<int:id>',deleteStudent),
    path('update/<int:id>',updateStudent),
    path('cbv/',classBasedView.as_view()),
    
    path('teacherlist/',login_required(TeacherRead.as_view()),name = 'listteacher'),
    path('getteacherdetails/<int:pk>/',login_required(GetTeacher.as_view())),
    path('insertteacher/',login_required(Addteacher.as_view())),
    path('updateteacher/<int:pk>/',login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/',login_required(DeleteTeacher.as_view())),

   
   
    path('insertcaretaker/',login_required(Addcaretaker.as_view())),
    path('caretakerlist/',login_required(caretakerRead.as_view()),name = 'listcaretaker'),
    path('getcaretakerdetails/<int:pk>/',login_required(GetcareTaker.as_view())),
    path('updatecaretaker/<int:pk>/',login_required(Updatecaretaker.as_view())),
    path('deletecaretaker/<int:pk>/',login_required(DeletecareTaker.as_view())),
    
   ]

