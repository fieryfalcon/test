from random import choices
from django.db import models
from .participants_user_details import *


class recruitment_test(models.Model):
    STATUS = (
            (1,  ('verified')),
            (2, ('in progress')),
            (3,('pending'))
        )
    enrollment_number=models.ForeignKey(Participants_detail, on_delete=models.CASCADE)
    recruitment_season_code = models.ForeignKey(recruitment_season,on_delete=models.CASCADE)
    evaluation_status=models.PositiveSmallIntegerField(choices=STATUS,default=3)
    evaluation_result=models.CharField(max_length=50)
    remarks=models.CharField(max_length=500)
    total_marks=models.IntegerField()
    
    
    class Meta:
        verbose_name = "recruitment_test"
        verbose_name_plural = "recruitment_tests"

    def __str__(self):
        return self.name
    
    
    
class winter_assingment(models.Model):
    STATUS = (
            (1,  ('verified')),
            (2, ('in progress')),
            (3,('pending'))
        )
    enrollment_number=models.ForeignKey(Participants_detail, on_delete=models.CASCADE)
    recruitment_season_code = models.ForeignKey(recruitment_season,on_delete=models.CASCADE)
    project_link=models.URLField(max_length=200)
    evaluation_result=models.CharField(max_length=50)
    remarks=models.CharField(max_length=500)
    total_marks=models.IntegerField()
    
    
    class Meta:
        verbose_name = "winter_assingment"
        verbose_name_plural = "winter_assingments"

    def __str__(self):
        return self.name


