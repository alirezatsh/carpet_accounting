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
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='رنگ')
    design = models.ForeignKey(Design, on_delete=models.CASCADE, verbose_name='طرح')
    length = models.ForeignKey(Length, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='طول')
    width = models.ForeignKey(Width, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='عرض')
    radius = models.ForeignKey(Radius, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='شعاع')
    is_rectangle = models.BooleanField(default=True, verbose_name='مستطیل')
    metraj = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='متراژ' , default=1)
    serial = models.CharField(max_length=30, verbose_name='سریال' , default=1)
    code = models.CharField(max_length=30, verbose_name='کد' , null=True, blank=True)
    shirazeh = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='شیرازه', related_name='shirazeh_carpets', null=True, blank=True)
    cheleh = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='چله', related_name='cheleh_carpets', null=True, blank=True)
    gereh = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name='گره', related_name='gereh_carpets', null=True, blank=True)
    
    # حذف default=None از فیلدهای DateTimeField
    shirazehkhoroug = models.DateTimeField(null=True, blank=True)
    chelehkhoroug = models.DateTimeField(null=True, blank=True)
    grehkhoroug = models.DateTimeField(null=True, blank=True)
    shirazehvouroud = models.DateTimeField(null=True, blank=True)
    chellehvouroud = models.DateTimeField(null=True, blank=True)
    gerehvouroud = models.DateTimeField(null=True, blank=True)
    
    ersalshodeh = models.BooleanField(default=False)
    id_name = models.IntegerField(default=1)

    

   

    class Meta:
        verbose_name = 'فرش ها'

    def __str__(self):
        return self.value
