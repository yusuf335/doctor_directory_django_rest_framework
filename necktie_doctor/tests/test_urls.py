from django.urls import resolve
from necktie_doctor.tests.test_setup import TestSetUp
from necktie_doctor.views import DoctorListAPI, DoctorDetailAPI, RegisterDoctorAPI


class TestUrls(TestSetUp):

    def test_docotr_list_url(self):
        self.assertEqual(resolve(self.doctor_list_url).func.view_class, DoctorListAPI)

    def test_docotr_detail_url(self):
        self.assertEqual(resolve(self.doctor_detail_url).func.view_class, DoctorDetailAPI)
        

    def test_docotr_registration_url(self):
        self.assertEqual(resolve(self.doctor_registration_url).func.view_class, RegisterDoctorAPI)
        
