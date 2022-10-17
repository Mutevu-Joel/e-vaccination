from django.db import models
from django.contrib.auth.models import User
import os
from twilio.rest import Client


# Create your models here.
VACCINE_TYPE = (
    ('BCG','BCG'),
    ('OPV I','OPV I'),
    ('OPV II','OPV II'),
    ('OPV III','OPV III'),
    ('Rotavirus I','Rotavirus I'),
    ('Rotavirus II','Rotavirus II'),
    ('Pneumo_Conj I','Pneumo_Conj I'),
    ('Pneumo_Conj II','Pneumo_Conj II'),
    ('Pneumo_Conj III','Pneumo_Conj III'),
    ('DTWPHibHepB I','DTWPHibHepB I'),
    ('DTWPHibHepB II','DTWPHibHepB II'),
    ('DTWPHibHepB III','DTWPHibHepB III'),
    ('IPV','IPV'),
    ('YF','YF'),
    ('Measles I','Measles I'),
    ('Measles II','Measles II'),
    ('HPV','HPV'),

)

MODE_OF_ADMISSION = (
    ('oral','oral'),
    ('injection','injection'),
)

SEX = (
    ('male','male'),
    ('female','female'),
)

UNDERLYING_CONDITION = (
(   'None','None'),
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
    
class Vaccine(models.Model):
    vaccine_id = models.CharField(max_length=50, null=True)
    mode_of_admission = models.CharField(max_length=50, choices=MODE_OF_ADMISSION, null=True)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPE)
    vaccine_quantity = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.vaccine_id}'
    
class Child(models.Model):
    child_registration_no = models.CharField(max_length=50, null=True)
    Surname = models.CharField(max_length=12,  null=True)
    Other_name = models.CharField(max_length=12)
    weight = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=10, null=True, choices=SEX)
    height = models.CharField(max_length=10, null=True)
    DOB = models.DateTimeField()
    parent_ID = models.CharField(max_length=10,null=True)
    phone_no = models.CharField(max_length=10,null=True)
    ward = models.CharField(max_length=50, null=True, choices=WARD)
    Underlying_condition = models.CharField(max_length=50, null=True, choices=UNDERLYING_CONDITION)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE, null=True)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPE, null=True)
    immunization_description = models.CharField(max_length=12, null=True)
    immunized_at = models.DateTimeField()
    

    class Meta:
        verbose_name_plural='Child'
    def __str__(self):
        return f'{self.child_registration_no}'
    def save(self, *args,**kwargs):
        if self.vaccine_type == 'BCG':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname} {self.Other_name}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
            
        elif self.vaccine_type == 'OPV I':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
        
        elif self.vaccine_type == 'OPV II':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
        
                 )   
            
        elif self.vaccine_type == 'OPV III':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 ) 
            
        elif self.vaccine_type == 'Pneumo_Conj I':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
        elif self.vaccine_type == 'Pneumo_Conj II':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
        elif self.vaccine_type == 'Pneumo_Conj III':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
        elif self.vaccine_type == 'DTWPHibHepB I':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )  
        elif self.vaccine_type == 'DTWPHibHepB II':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 ) 
        elif self.vaccine_type == 'DTWPHibHepB III':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
        elif self.vaccine_type == 'IPV':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )  
        elif self.vaccine_type == 'YF':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )
        elif self.vaccine_type == 'Measles I':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )  
        elif self.vaccine_type == 'Measles II':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 ) 
        elif self.vaccine_type == 'HPV':
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"Congratulations {self.Surname}, for receiving {self.vaccine_type}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )   
              
            
             
        
        else:
            account_sid = 'AC472396e9279bcb521327435da6e855d2'
            auth_token = 'a7c4be0c621e51f4fe52ecaf9039e7cd'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                     body=f"sorry {self.Surname}, for receiving {self.vaccine_type},Batch number{self.vaccine_id}, on {self.immunized_at}",
                     from_='+13856006974',
                     to='+254798466318'
                 )

            print(message.sid)
            return super().save(*args, **kwargs)
            

class Staff(models.Model):
    staff_ID = models.PositiveIntegerField()
    Surname = models.CharField(max_length=12)
    Other_name = models.CharField(max_length=12)
    email = models.CharField(max_length=12,null=True)
    DOB = models.DateTimeField()
    Mobile_No = models.PositiveIntegerField()
    Job_description = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)


class Profile(models.Model, ):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    image = models.ImageField(default='avatar.jpg',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.staff.username}-Profile'

class Immunization(models.Model):
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE, null=True)
    vaccine_type = models.CharField(max_length=50, choices=VACCINE_TYPE, null=True)
    immunization_description = models.CharField(max_length=12, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vaccine_id}'

    









