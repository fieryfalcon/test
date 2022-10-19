from random import choices
from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser


def year_choices():
    return [(r,r) for r in range(datetime.date.today().year-2, datetime.date.today().year+4)]

def current_year():
    return datetime.date.today().year



class img_member(AbstractUser):

    
    name = models.CharField(max_length=70)
    year = models.IntegerField()
    is_designer=models.BooleanField(default=True,null=True)
    enrollment_number = models.IntegerField(primary_key=True,unique=True)
    

    class Meta:
        verbose_name = "Img_member"
        verbose_name_plural = "Img_members"

    def __str__(self):
        return self.name
    
    
    
class recruitment_season(models.Model):
    STATUS = (
            (1,  ('development')),
            (2, ('design')),
        )
    role=models.PositiveSmallIntegerField(choices=STATUS,default=1)
    year = models.IntegerField(choices=year_choices(), default=current_year())
    
    

    class Meta:
        verbose_name = "recruitment_season"
        verbose_name_plural = "recruitment_seasons"
        
        



class Participants_detail(models.Model):
    STATUS = (
            (1,  ('recruitment Test')),
            (2, ('WInter Assingment')),
        )
    enrollment_number = models.IntegerField(unique=False)
    name=models.CharField(max_length=40)
    department=models.CharField(max_length=50)
    mode_of_entry=models.PositiveSmallIntegerField(choices=STATUS,default=1)
    phone_number = models.BigIntegerField(("phone number"),default=123456789)
    email = models.EmailField(("email"), max_length=254,null="True")
    

    class Meta:
        verbose_name = "Participants_detail"
        verbose_name_plural = "Participants_details"

    def __str__(self):
        return self.name
    


class connection_participant_seasons(models.Model):
    recruitment_season_code = models.ForeignKey(recruitment_season,on_delete=models.CASCADE)
    Participants_detail = models.ForeignKey(Participants_detail,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name