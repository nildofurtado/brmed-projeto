from django.db import models

# Create your models here.
class Post(models.Model):
    logIp      = models.GenericIPAddressField()
    dt_vl      = models.DateField(auto_now=False)
    vl_brl     = models.DecimalField(max_digits=6, decimal_places=3) 
    vl_ien     = models.DecimalField(max_digits=6, decimal_places=3) 
    vl_eur     = models.DecimalField(max_digits=6, decimal_places=3) 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)