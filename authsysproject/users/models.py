from django.db import models
from django.contrib.auth.models import User

# Create your models here.
VACCINE_TYPE = (
    ('BCG','BCG'),
    ('OPV','OPV'),
    ('Rotavirus','Rotavirus'),
    ('Pneumo_Conj','Pneumo_Conj'),
    ('DTWPHibHepB','DTWPHibHepB'),
    ('IPV','IPV'),
    ('YF','YF'),
    ('Measles','Measles'),
    ('HPV','HPV'),

)

MODE_OF_ADMISSION = (
    ('oral','oral'),
    ('injection','injection'),
)

UNDERLYING_CONDITION = (
    ('HIV','HIV'),
    ('Down Syndrome','Down Syndrome'),
    ('Orofacial cleft','Orofacial cleft'),
('Hemophilia','Hemophilia'),
('Congenital dislocated hip','Congenital dislocated hip'),
('Tay-Sachs disease','Tay-Sachs disease'),
)

WARD = (
    ('Thange','Thange'),
    ('Kikumbulyu South','Kikumbulyu South'),
('Kikumbulyu North','Kikumbulyu North'),
('Masongaleni','Masongaleni'),
('Nguumo','Nguumo'),
('Mtito Andei','Mtito Andei'),
('Ivingoni/Nzambani','Ivingoni/Nzambani'),
('Emali/Mulala','Emali/Mulala'),
('Makindu','Makindu'),
('Nguu/Masumba','Nguu/Masumba'),

)
class Parents(models.Model):
    parent_ID = models.PositiveIntegerField()
    father_id = models.PositiveIntegerField()
    Surname = models.CharField(max_length=12)
    Other_name = models.CharField(max_length=12)
    DOB = models.DateTimeField()
    Village = models.CharField(max_length=12)
    Ward = models.CharField(max_length=12)
    child_registration_no = models.CharField(max_length=12)
    Mobile_No = models.PositiveIntegerField()

class Child(models.Model):
    child_registration_no = models.CharField(max_length=12)
    Surname = models.CharField(max_length=12)
    Other_name = models.CharField(max_length=12)
    weight = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    DOB = models.DateField()
    parent_ID = models.CharField(max_length=10,null=True)
    phone_no = models.CharField(max_length=10,null=True)
    ward = models.CharField(max_length=50, null=True, choices=WARD)
    Underlying_condition = models.CharField(max_length=50, null=True, choices=UNDERLYING_CONDITION)
    immunization_type = models.CharField(max_length=12, choices=VACCINE_TYPE)
    immunization_dose_no = models.PositiveIntegerField(max_length=12)
    immunization_description = models.CharField(max_length=12)

class Staff(models.Model):
    staff_ID = models.PositiveIntegerField()
    Surname = models.CharField(max_length=12)
    Other_name = models.CharField(max_length=12)
    DOB = models.DateTimeField()
    Mobile_No = models.PositiveIntegerField()
    Job_description = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)


class Immunization(models.Model):
    vaccine_ID = models.PositiveIntegerField()
    child_registration_no = models.CharField(max_length=12)
    immunization_dose_no = models.CharField(max_length=12)
    immunization_description = models.CharField(max_length=12)

class vaccine(models.Model):
    vaccine_id = models.CharField(max_length=50, null=True)
    mode_of_admission = models.CharField(max_length=50, choices=MODE_OF_ADMISSION, null=True)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPE)
    vaccine_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.vaccine_id}'

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    image = models.ImageField(default='avatar.jpg',
                              upload_to='profile_images')
    objects = models.Manager()

    def __str__(self):
        return f'{self.staff.username}-Profile'









