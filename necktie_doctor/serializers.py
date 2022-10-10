from rest_framework import serializers
from necktie_doctor.models import Doctor, District, Category, WorkingHour, Experience, Services, Gender



class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class WorkingHourSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkingHour
        fields = ['weekday', 'from_hour', 'to_hour']

class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['workplace', 'designation']


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['service']

class GenderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['gender']


class DoctorListSerializers(serializers.ModelSerializer):
    district = serializers.SlugRelatedField(read_only=True, slug_field='district')
    category = serializers.SlugRelatedField(read_only=True, slug_field='category')
    gender = serializers.SlugRelatedField(read_only=True, slug_field='gender')
    service = ServiceSerializers(read_only=True, many=True)
    operating_hours = WorkingHourSerializers(read_only=True, many=True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'category', 'address', 'district', 'gender', 'lat', 'lng', 'price', 'featured', 'public_holiday', 'language', 'service','operating_hours']


class DoctorDetailSerializers(serializers.ModelSerializer):
    district = serializers.SlugRelatedField(read_only=True, slug_field='district')
    category = serializers.SlugRelatedField(read_only=True, slug_field='category')
    gender = serializers.SlugRelatedField(read_only=True, slug_field='gender')
    experience = ExperienceSerializers(read_only=True, many=True)
    service = ServiceSerializers(read_only=True, many=True)
    operating_hours = WorkingHourSerializers(read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorRegistrationSerializers(serializers.ModelSerializer):
    experience = ExperienceSerializers(read_only=False, many=True)
    service = ServiceSerializers(read_only=False, many=True)
    operating_hours = WorkingHourSerializers(read_only=False, many=True)


    class Meta:
        model = Doctor
        fields = ['name', 'phone', 'email', 'address', 'about', 'price', 'lat', 'lng', 'public_holiday', 'district', 'category', 'gender', 'language', 'experience', 'education', 'service', 'operating_hours']

    def create(self, validated_data):
        experiences = validated_data.pop('experience')
        services = validated_data.pop('service')
        operating_hours = validated_data.pop('operating_hours')

        doctor = Doctor.objects.create(**validated_data)

        for exp in experiences:
            Experience.objects.create(doctor=doctor, **exp)

        for ser in services:
            Services.objects.create(doctor=doctor, **ser)

        for operating_data in operating_hours:
            WorkingHour.objects.create(doctor=doctor, **operating_data)

        return doctor
