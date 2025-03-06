from django.urls import path, include
from .views import *
from .forms import *

urlpatterns = [
    # path('index/', index),
    path('index/', Index.as_view()),
    path('index/', Index.as_view(), name='index'),
    path('index/', Index.as_view, name='home'),
    path('add_kurs/', add_kurs, name='add_kurs'),
    path('add_student/', add_student, name='add_student'),
    path('kursinfo/<int:kurs_id>', Kursinfo.as_view(), name='kursinfo'),
    path('download_pdf/<int:student_id>', download_student_pdf, name='download_student_pdf'),
    path('del_info/<int:student_id>', del_info, name='del_info'),

]
