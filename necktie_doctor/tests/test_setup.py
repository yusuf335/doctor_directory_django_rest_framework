from rest_framework.test import APITestCase
from django.urls import reverse
from necktie_doctor.models import District, Category, Doctor, Experience, Services, WorkingHour, Gender


class TestSetUp(APITestCase):

    def setUp(self): 
        # https://www.django-rest-framework.org/api-guide/testing/

        # URL path
        self.doctor_list_url = reverse('doctors_list')
        self.doctor_registration_url = reverse('doctor_registration')
        

        # Creating instances for doctor
        self.district = District.objects.create(district= 'Test_district')
        self.category = Category.objects.create(category='Test_category')
        self.gender = Gender.objects.create(gender='Male')


        # Creating a Doctor profile
        self.doctor = Doctor.objects.create(
            name = "Doctor 1",
            about = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            phone = 12356789,
            email = "doctor1@gmail.com",
            category = self.category,
            address =  "ABC, level - 4",
            district = self.district,
            lat = None,
            lng = None,
            price = 400,
            language = "English, Bangla",
            education = "MBBS",
            public_holiday = "U",
        )
    
        # URL path for doctor detail with id as parameter
        self.doctor_detail_url = reverse('doctor_detail', args=[self.doctor.id])


        self.experience = Experience.objects.create(
            doctor = self.doctor,
            workplace = "ABC Hospital",
            designation = "Senior Consultant"
        )

        self.service = Services.objects.create(
            doctor = self.doctor,
            service = "Inclusive 3 Days of Western medicine"
        )

        self.workinghours = WorkingHour.objects.create(
            doctor = self.doctor,
            weekday = 1,
            from_hour = "03:53:51",
            to_hour = "03:53:49"
        )

        return super().setUp()

    