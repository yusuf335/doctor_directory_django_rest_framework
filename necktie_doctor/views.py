from django.db.models import Max
from rest_framework import generics, pagination

from necktie_doctor.models import Doctor
from necktie_doctor.serializers import DoctorListSerializers, DoctorDetailSerializers, DoctorRegistrationSerializers



# Custom pagination
class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# Doctor list api view
class DoctorListAPI(generics.ListAPIView):
    serializer_class = DoctorListSerializers
    pagination_class = CustomPagination

    def get_queryset(self):
        # Getting query parametes from the url
        max_price = self.request.query_params.get('max_price') or \
                    Doctor.objects.all().aggregate(Max('price'))['price__max'] or 0
                    
        min_price = self.request.query_params.get('min_price') or 0
        district = self.request.query_params.get('district') or ''
        category = self.request.query_params.get('category') or ''
        language = self.request.query_params.get('language') or ''

        return  Doctor.objects.filter(
                                        price__lte = max_price,
                                        price__gte = min_price,
                                        district__district__icontains = district,
                                        category__category__icontains = category,
                                        language__icontains = language
                                    ).order_by('name').distinct()



# Doctor detail api view
class DoctorDetailAPI(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializers  


# Doctor registration api view      
class RegisterDoctorAPI(generics.CreateAPIView):
    serializer_class = DoctorRegistrationSerializers

    def perform_create(self, serializer):
        serializer.save()



