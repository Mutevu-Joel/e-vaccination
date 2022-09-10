from django.db import models

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
    DOB = models.DateTimeField()
    parent_ID = models.PositiveIntegerField()
    immunization_type = models.CharField(max_length=12)
    immunization_dose_no = models.CharField(max_length=12)
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
    vaccine_name = models.CharField(max_length=50, null=True)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPE)
    vaccine_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.vaccine_id}-{self.vaccine_name}-{self.vaccine_quantity}'









