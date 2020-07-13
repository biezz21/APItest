from django.db import models

# Create your models here.


class OpenlabModel(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)

    class Meta:
        db_table = 'openlab'
