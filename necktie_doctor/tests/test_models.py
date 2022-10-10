from necktie_doctor.tests.test_setup import TestSetUp


class TestModels(TestSetUp):
    
    def test_district_on_creation(self):
        self.assertEqual(self.district.district, 'Test_district')

    def test_category_on_creation(self):
        self.assertEqual(self.category.category, 'Test_category')

    def test_doctor_on_creation(self):
        self.assertEqual(self.doctor.name, 'Doctor 1')

    def test_doctor_experience_relationship(self):
        self.assertEqual(self.experience.doctor, self.doctor)

    def test_doctor_service_relationship(self):
        self.assertEqual(self.service.doctor, self.doctor)

    def test_doctor_gender_relationship(self):
        self.assertEqual(self.service.doctor, self.doctor)

    def test_doctor_workinghour_relationship(self):
        self.assertEqual(self.workinghours.doctor, self.doctor)