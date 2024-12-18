from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    value = models.CharField(max_length=100 , verbose_name='بخش ها')
    
    class Meta:
        verbose_name = 'بخش ها'

    def __str__(self):
        return self.value
    
    
class Workers(models.Model):
    name = models.CharField(max_length=30 , null=True , blank=True , verbose_name='نام')
    last_name = models.CharField(max_length=40 ,blank=True, null=True , verbose_name='نام خانوادگی')
    section = models.ForeignKey(Section, on_delete=models.CASCADE , related_name='workers' , blank=True , null=True , verbose_name='بخش')
    phone = models.CharField(max_length=11 , blank=True , null=True , verbose_name='تلفن')
    landline_phone = models.CharField(max_length=20 , blank=True , null=True , verbose_name='تلفن ثابت')
    address = models.TextField(blank=True , null=True , verbose_name='آدرس')
    
    class Meta:
        verbose_name = 'کارمندان'
    
    def __str__(self):
        if self.name and self.last_name:
            return f"{self.name} {self.last_name}"  
        
        elif self.name:
            return self.name  
        
        elif self.last_name:
            return self.last_name 
        
        return ""
    
    
    
class SectionUser(models.Model):
    user = models.ForeignKey(Workers, on_delete=models.CASCADE , verbose_name='کارمند')
    section = models.ForeignKey(Section, on_delete=models.CASCADE , verbose_name='بخش')
    
    class Meta:
        verbose_name = 'بخش و کارمند'

    def __str__(self):
        if self.user.last_name and self.user.name:
            return f"{self.user.name} {self.user.last_name} - {self.section.value}"
        
        elif self.user.last_name:
            return f"{self.user.last_name} - {self.section.value}"
        
        return ""
    
    

class Help(models.Model):
    worker = models.ForeignKey(Workers , on_delete=models.CASCADE , verbose_name='نام کارمند')
    money = models.IntegerField(verbose_name='مبلغ')
    date = models.CharField(max_length=30 , verbose_name='تاریخ ')
    
    
    def __str__(self):
        return f'{self.worker} - {self.date}'
    
    class Meta:
        verbose_name = 'مساعده'