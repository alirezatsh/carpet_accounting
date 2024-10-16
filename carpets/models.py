from django.db import models
from accounts.models import Workers


# مدل رنگ
class Color(models.Model):
    value = models.CharField(max_length=50, verbose_name='رنگ ها')

    class Meta:
        verbose_name = 'رنگ ها'

    def __str__(self):
        return self.value

# مدل طرح
class Design(models.Model):
    value = models.CharField(max_length=100, verbose_name='طرح ها')

    class Meta:
        verbose_name = 'طرح ها'

    def __str__(self):
        return self.value

# مدل شکل (دایره یا مستطیل)
class Shape(models.Model):
    RECTANGLE = 'rectangle'
    CIRCLE = 'circle'
    SHAPE_CHOICES = [
        (RECTANGLE, 'مستطیل'),
        (CIRCLE, 'دایره'),
    ]
    value = models.CharField(max_length=50, choices=SHAPE_CHOICES, verbose_name='شکل')

    class Meta:
        verbose_name = 'شکل‌ها'

    def __str__(self):
        return self.get_value_display()


class Length(models.Model):
    value = models.CharField(max_length=20 , blank=True , null=True , verbose_name='طول')

    class Meta:
        verbose_name = 'طول'
        
    def __str__(self):
        return str(self.value)

class Width(models.Model):
    value = models.CharField(max_length=20 , blank=True , null=True , verbose_name='عرض')

    class Meta:
        verbose_name = 'عرض'
        
    def __str__(self):
        return str(self.value)

class Radius(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='شعاع')
    
    class Meta:
        verbose_name = 'شعاع'
        
    def __str__(self):
        return str(self.value)




class Carpet(models.Model):
    rang = models.CharField(max_length=20 , blank=True , null=True , verbose_name='رنگ')
    naghsheh = models.CharField(max_length=20, blank=True , null=True , verbose_name='نقشه')
    tool = models.CharField(max_length=20 , blank=True , null=True , verbose_name='طول')
    arz = models.CharField(max_length=20 , blank=True , null=True , verbose_name='عرض')
    isRectangle = models.BooleanField(default=True, verbose_name='مستطیل')
    metraj = models.CharField(max_length=20 , blank=True , null=True , verbose_name='متراژ')
    serial = models.CharField(max_length=30, verbose_name='سریال' , default=1)
    code = models.CharField(max_length=30, verbose_name='کد' , null=True, blank=True)
    shirazeh = models.CharField(max_length=30, verbose_name = 'شیرازه'  , blank=True , null=True)
    gereh = models.CharField(max_length=30, verbose_name = 'گره'  , blank=True , null=True)
    cheleh = models.CharField(max_length=30, verbose_name = 'چله'  , blank=True , null=True)
    shirazehKhoroug = models.CharField(null=True, blank=True , max_length=40)
    chelehKhoroug = models.CharField(null=True, blank=True , max_length=40)
    grehKhoroug = models.CharField(null=True, blank=True , max_length=40)
    shirazehVouroud = models.CharField(null=True, blank=True , max_length=40)
    chellehVouroud = models.CharField(null=True, blank=True , max_length=40)
    gerehVouroud = models.CharField(null=True, blank=True , max_length=40)
    ersalshodeh = models.BooleanField(default=False)

    

   

    class Meta:
        verbose_name = 'فرش ها'

    def __str__(self):
        return str(self.id)




