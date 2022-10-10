from django.contrib import admin
from necktie_doctor.models import District, Category, WorkingHour, Doctor, Gender

# Register your models here.

admin.site.register(District)
admin.site.register(Category)
admin.site.register(WorkingHour)
admin.site.register(Doctor)
admin.site.register(Gender)