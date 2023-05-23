from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    sname=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sname
    
    def get_absolute_url(self):
        return reverse('School_Details',kwargs={'pk':self.pk})
class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='student')
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    location=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.stname