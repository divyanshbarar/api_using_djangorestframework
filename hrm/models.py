from django.db import models

# Create your models here.
class User(models.Model):
    employee_id=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=29)
    age=models.IntegerField()
    ranking=models.FloatField()
    
    def upload_photo(self,filename):
        path='hrm/photo/{}'.format(filename)
        return path

    photo=models.ImageField(upload_to=upload_photo,null=True,blank=True)

    def upload_file(self,filename):
        path='hrm/file/{}'.format(filename)
        return path

    resume=models.ImageField(upload_to=upload_file,null=True,blank=True)
