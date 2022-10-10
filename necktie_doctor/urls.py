from django.urls import path
from necktie_doctor import views


urlpatterns = [
    path('', views.DoctorListAPI.as_view(), name='doctors_list'),
    path('<pk>', views.DoctorDetailAPI.as_view(), name='doctor_detail'),
    path('register/', views.RegisterDoctorAPI.as_view(), name="doctor_registration"),
]
