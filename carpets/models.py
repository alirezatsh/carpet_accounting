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
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='طول')

    class Meta:
        verbose_name = 'طول'
        
    def __str__(self):
        return str(self.value)

class Width(models.Model):
    value = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='عرض')

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
    value = models.CharField(max_length=100, default='Unknown', verbose_name='فرش ها')
    rang = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='رنگ')
    naghsheh = models.ForeignKey(Design, on_delete=models.CASCADE, verbose_name='طرح')
    tool = models.ForeignKey(Length, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='طول')
    arz = models.ForeignKey(Width, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='عرض')
    isrectangle = models.BooleanField(default=True, verbose_name='مستطیل')
    metraj = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='متراژ' , default=1)
    serial = models.CharField(max_length=30, verbose_name='سریال' , default=1)
    code = models.CharField(max_length=30, verbose_name='کد' , null=True, blank=True)
    shirazeh = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='شیرازه', related_name='shirazeh_carpets', null=True, blank=True)
    cheleh = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='چله', related_name='cheleh_carpets', null=True, blank=True)
    gereh = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='گره', related_name='gereh_carpets', null=True, blank=True)
    shirazehkhoroug = models.CharField(null=True, blank=True , max_length=40)
    chelehkhoroug = models.CharField(null=True, blank=True , max_length=40)
    grehkhoroug = models.CharField(null=True, blank=True , max_length=40)
    shirazehvouroud = models.CharField(null=True, blank=True , max_length=40)
    chellehvouroud = models.CharField(null=True, blank=True , max_length=40)
    gerehvouroud = models.CharField(null=True, blank=True , max_length=40)
    ersalshodeh = models.BooleanField(default=False)

    

   

    class Meta:
        verbose_name = 'فرش ها'

    def __str__(self):
        return self.value
