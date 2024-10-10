from django.db import models

# Create your models here.
from django.db import models

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
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, verbose_name='شکل')
    length = models.ForeignKey(Length, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='طول')
    width = models.ForeignKey(Width, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='عرض')
    radius = models.ForeignKey(Radius, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='شعاع')

   

    class Meta:
        verbose_name = 'فرش ها'

    def __str__(self):
        return self.value
