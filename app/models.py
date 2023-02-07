from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Vaccine(models.Model):
    AGE_CHOICE_1 = '6 mos to 4 years'
    AGE_CHOICE_2 = '6 mos to 5 years'
    AGE_CHOICE_3 = 'age 5-11'
    AGE_CHOICE_4 = 'age 6-11'
    AGE_CHOICE_5 = '12 and older'
    AGE_CHOICE_6 = '18 and older'

    AGE_CHOICES = [
        (AGE_CHOICE_1, '6 mos to 4 years'), 
        (AGE_CHOICE_2, '6 mos to 5 years'), 
        (AGE_CHOICE_3, 'age 5-11'), 
        (AGE_CHOICE_4, 'age 6-11'), 
        (AGE_CHOICE_5, '12 and older'), 
        (AGE_CHOICE_6, '18 and older')
    ]

    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255, choices=AGE_CHOICES, default=AGE_CHOICE_5)
    cap_color = models.CharField(max_length=50, default='gray')
    border_color = models.CharField(max_length=50, default='gray')
    dose = models.CharField(max_length=50, default='-')
    doses_per_vial = models.IntegerField(default=6)
    dilution = models.BooleanField(default=True)
    storage = models.CharField(max_length=255, default='-')
    thaw = models.CharField(max_length=255, default='-')
    bud = models.CharField(max_length=50, default='6 hours after puncture')
    # pic = 
    ndc = models.CharField(max_length=50, default='-')
    link = models.CharField(max_length=255, default='-')
    users = models.ManyToManyField(get_user_model())

    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(default='1999-11-10')
    comorbidities = models.BooleanField(default=False)
    allergies = models.BooleanField(default=False)
    vac_received = models.SmallIntegerField(default=0)
    vac_given = models.DateField(default='1999-11-10')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ['-last_name']

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)
