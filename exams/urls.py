from django.urls import path
from django.contrib.auth.decorators import login_required,permission_required
from exams.views import Addmarks
from exams.views import marksRead
from exams.views import Getmarks
from exams.views import Updatemarks
from exams.views import Deletemarks


urlpatterns = [

    
   
    
    path('insertmarks/',login_required(Addmarks.as_view())),
    path('markslist/',login_required(marksRead.as_view()), name = 'listmarks'),
    path('getmarksdetails/<int:pk>/', login_required(Getmarks.as_view())),
    path('updatemarks/<int:pk>/', login_required(Updatemarks.as_view())),
    path('deletemarks/<int:pk>/', login_required(Deletemarks.as_view())),
    
   ]



