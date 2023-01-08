from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Bloodgroups(models.TextChoices):
        O_positive = 'O+'
        O_negative = 'O-'
        B_positive = 'B+'
        B_negative = 'B-'
        AB_positive = 'AB+'
        AB_negative = 'AB-'
        A_positive = 'A+'
        A_negative = 'A-'

class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'
    TRANSGENDER = 'transgender'
    OTHER = 'other'

class BloodUnit(models.Model):
    bloodgroup = models.CharField(max_length=3, 
                                  choices= Bloodgroups.choices,
                                  default = Bloodgroups.B_positive
                                  )
    
    donor_name = models.CharField(max_length=50,
                                  default=None)    
    
    donor_mobile_number = models.CharField(max_length=16,
                                           default=None)
    
    donor_age = models.PositiveIntegerField(max_length=3, 
                                            default=None)
    
    donor_sex = models.CharField(max_length=15,
                                 default=None)

    donation_date = models.DateField(_("Date"), default=datetime.date.today)

    def is_rare_blood_group(self):
        return self.bloodgroup in {
            self.bloodgroups.B_negative, 
            self.bloodgroups.AB_negative, 
            self.bloodgroups.A_positive 
        }