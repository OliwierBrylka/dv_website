from django.db import models
import uuid
# Create your models here.



class estan(models.Model):
    bl_id = models.TextField(max_length=100, blank=True)
    sku = models.TextField(max_length=100)
    ean = models.TextField(max_length=100, blank=True)
    Estan = models.TextField(max_length=100, blank=True)
    name = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.sku
    

class imp_excle(models.Model):
    ex_id = models.CharField(max_length=32, primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='estan_import', blank=True)

    def hex_uuid():
        return uuid.uuid4().hex