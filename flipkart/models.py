from django.db import models

# Create your models here.


class Names(models.Model):
    name =models.CharField(max_length=255)
    father_name=models.CharField(max_length=255)
    mobile_number=models.BigIntegerField()
    dob = models.DateTimeField()

    def __str__(self):
        return str(self.name)


class Attendance(models.Model):
    name=models.ForeignKey(Names,on_delete=models.CASCADE)
    day=models.DateTimeField()
    is_present=models.BooleanField()




