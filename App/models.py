from django.db import models
from django.contrib.auth.models import User


class UserOTP(models.Model):
     user_name=models.ForeignKey(User,on_delete=models.CASCADE)
     time_st=models.DateTimeField(auto_now=True)
     otp=models.SmallIntegerField()



class wantedperson(models.Model):
    person_name=models.CharField(max_length=200)
    person_crime=models.CharField(max_length=200)
    crime_date=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='app/images',default="")
    def __str__(self):
        return self.person_name 
class missingperson(models.Model):
    person_name=models.CharField(max_length=200)
    age=models.IntegerField()
    missing_date=models.DateField()
    image=models.ImageField(upload_to='app/images',default="")
    def __str__(self):
        return self.person_name 

class ComplaintRegister(models.Model):
    CATEGORY=(('Credit Card Fraud','Credit Card Fraud'),
         
            ('Fraud','Fraud'),
            ('Harassment','Harassment'),
            ('Kidnapping','Kidnapping'),
            ('Money Laundering','Money Laundering'),
            ('Murder','Murder'),
            ('Public Intoxication','Public Intoxication'),
            ('Rape','Rape'),
            ('Robbery','Robbery'),
            ('Sexual Assault','Sexual Assault'),
            ('Shoplifting','Shoplifting'),
            ('Statutory Rape','Statutory Rape'),
            ('Theft','Theft'),
            ('Wire Fraud','Wire Fraud'),
            ('Insurance Fraud','Insurance Fraud'),
            ('Identity Theft','Identity Theft'),
            ('Perjury','Perjury')
              )
    gender_category=(('Male','Male'),
                 ('Female','Female'),
                 ('Others','Others')
    )
    states_category=(('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('	Bihar','	Bihar'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Telangana','Telangana'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Rajasthan','Rajasthan'),
    ('Odisha','Odisha'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('	Uttarakhand','	Uttarakhand'))


    distict_place=(('Agra','Agra'),
    ('Aligarh','Aligarh'),
    ('	Allahabad','Allahabad'),
    ('Azamgarh','Azamgarh'),
    ('Chitrakoot','Chitrakoot'),
    ('Faizabad','Faizabad'),
    ('Gorakhpur','Gorakhpur'),
    ('Jhansi','Jhansi'),
    ('Kanpur ','Kanpur '),
    ('Lucknow','Lucknow'),
    ('Meerut','Meerut'),
    ('Mirzapur','Mirzapur'),
    ('Moradabad','Moradabad'),
    ('Varanasi','Varanasi'),
    ('Etawah','Etawah'),
    ('Ghaziabad	','Ghaziabad	'),
    ('Jaunpur','Jaunpur'),
    ('Kasganj','Kasganj'),
    ('Farrukhabad','Farrukhabad'),
    ('Shahdara','Shahdara'),
    ('	Central Delhi','Central Delhi'),
    ('New Delhi ','New Delhi '),
    ('South Delhi','South Delhi'),
    ('South West Delhi','South West Delhi'),
    ('Bareilly','Bareilly'),
    )
     
    complaint_type=models.CharField(max_length=100,choices=CATEGORY)
    crime_place=models.TextField()
    crime_in_detail=models.TextField(null=True)
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=100,choices=gender_category)
    date_of_birth=models.CharField(max_length=200)
    email_id=models.EmailField()
    mobile_no=models.CharField(max_length=10)
    house_no=models.CharField(max_length=10)
    permanent_address=models.TextField()
    landmark=models.TextField()
    state=models.CharField(max_length=100,choices=states_category)
    distict_place=models.CharField(max_length=100,choices=distict_place)
    
    def __str__(self):
        return self.first_name+' '+self.last_name
        

class crimestories(models.Model):
    Heading=models.CharField(max_length=500)
    detail=models.TextField()
    image=models.ImageField()
    def __str__(self):
        return self.Heading