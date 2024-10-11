from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=100 , verbose_name='بخش ها')
    
    class Meta:
        verbose_name = 'بخش ها'

    def __str__(self):
        return self.name
    
    
class Workers(models.Model):
    name = models.CharField(max_length=30 , null=True , blank=True , verbose_name='نام')
    last_name = models.CharField(max_length=40 ,blank=True, null=True , verbose_name='نام خانوادگی')
    
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
            return f"{self.user.name} {self.user.last_name} - {self.section.name}"
        
        elif self.user.last_name:
            return f"{self.user.last_name} - {self.section.name}"
        
        return ""