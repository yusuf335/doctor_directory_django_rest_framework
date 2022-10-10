from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# District Model
class District(models.Model):
    district = models.CharField(max_length=150)

    class Meta:
        db_table = 'district'
    
    def __str__(self):
        return self.district


# Category Model
class Category(models.Model):
    category = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category


# Gender Model
class Gender(models.Model):
    gender = models.CharField(max_length=150)

    class Meta:
        db_table = 'gender'

    def __str__(self):
        return self.gender


# Doctor Model
# Lat and lng high precision depends on the number of digit and decimal places stored 
# For more info regarding lat and lng please visit https://xkcd.com/2170/

class Doctor(models.Model):

    class PublicHoliday(models.TextChoices):
        UNKNOWN = ('U', 'Unknown')
        OPENED = ('O', 'Opened')
        CLOSED = ('C', 'Closed')

    # Personal Information 
    name = models.CharField(max_length=250)
    phone = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    price = models.PositiveIntegerField()
    about = models.TextField()
    education = models.TextField()
    language = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, db_column='category')
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, db_column='gender')

    # Address
    address = models.TextField()
    lat = models.DecimalField(_('Latitude'), max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(_('Longitude'), max_digits=22, decimal_places=16, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, db_column='district')
    
    # Working Hour
    public_holiday = models.CharField(max_length=1, choices=PublicHoliday.choices, default=PublicHoliday.UNKNOWN)

    # Other config
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return self.name



# Doctor's experience model
class Experience(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='experience', blank=True)
    workplace = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'experience'  

    def __str__(self):
        return self.workplace



# Services provided by the consultation see
class Services(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='service', blank=True)
    service = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'services'

    def __str__(self):
        return self.service  

# Working Days 
WEEKDAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Sunday"),
    (8, "Public Holiday"),
]

class WorkingHour(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='operating_hours', db_column='doctor', blank=True)
    weekday = models.IntegerField(choices=WEEKDAYS, validators=[MinValueValidator(1), MaxValueValidator(8)])
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        db_table = 'working_hour'

    def __str__(self) :
        return str(self.weekday)


