import json
from rest_framework import status
from necktie_doctor.tests.test_setup import TestSetUp


class DoctorListViewTest(TestSetUp):

    # This function send get request to have the list of doctors.
    # Response status code should be 200. 
    def test_doctor_list_GET(self):
        response = self.client.get(self.doctor_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # This function send get request to have the  detail of doctor.
    # Response status code should be 200. 
    def test_doctor_detail_GET(self):
        response = self.client.get(self.doctor_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # This function send get request to register a doctor but it should be post request.
    # Response status code should be 405. 
    def test_register_doctor_GET(self):
        response = self.client.get(self.doctor_registration_url)
        self. assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # This function send post request to register a doctor but no data is passed.
    # Response status code should be 400. 
    def test_register_doctor_POST_no_data(self):
        response = self.client.post(self.doctor_registration_url)
        self. assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # This function send post request to register a doctor with correct information.
    # Response status code should be 201. 
    def test_register_doctor_POST(self):
        data = {
                "name": "Doctor 1",
                "about": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                "phone": 12356789,
                "email": "doctor1@gmail.com",
                "category": self.category.id,
                "address": "ABC, level - 4",
                "district": self.district.id,
                "lat": 51.078159,
                "lng": -114.135803,
                "price": 400,
                "language": "English, Bangla",
                "education": "MBBS",
                "public_holiday": "U",
                "experience": [
                    {
                        "workplace": "ABC Hospital",
                        "designation": "Senior Consultant"
                    }
                ],
                "service": [
                    {"service": "Inclusive 3 Days of Western medicine"}
                ],

                "operating_hours": [
                    {
                        "weekday": 1,
                        "from_hour": "03:53:51",
                        "to_hour": "03:53:49"
                    },
                    {
                        "weekday": 2,
                        "from_hour": "03:53:51",
                        "to_hour": "03:53:49"
                    }
                ]
            }

        response = self.client.post(self.doctor_registration_url, json.dumps(data), content_type='application/json')
        self. assertEqual(response.status_code, status.HTTP_201_CREATED)

        