from django.db import models
# Create your models here.
class Tracking(models.Model):
    name = models.CharField(max_length=80, null=True,blank=True)
    tel = models.CharField(max_length=80, null=True,blank=True)
    tracking = models.CharField(max_length=80, null=True,blank=True)
    other = models.TextField(max_length=80, null=True,blank=True)

class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType, max_length=10)

class Ask(models.Model):
    name = models.CharField(max_length=80, null=True,blank=True, verbose_name = 'ชื่อผู้ติดต่อ')
    email = models.CharField(max_length=80, null=True,blank=True, verbose_name = 'อีเมล')
    title = models.CharField(max_length=80, null=True,blank=True, verbose_name = 'หัวข้อ')
    detail = models.TextField(null=True,blank=True, verbose_name = 'รายละเอียด')

    def __str__(self):
        return '{} - ({})'.format(self.name,self.title)