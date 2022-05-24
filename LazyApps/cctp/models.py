from django.db import models
from django.contrib.auth.models import User


class Moa(models.Model):
    moa_name = models.CharField(max_length=250)
    moa_adress = models.CharField(max_length=500)
    moa_cp = models.IntegerField()
    moa_city = models.CharField(max_length=250)
    moa_phone = models.CharField(max_length=20)
    moa_fax = models.CharField(max_length=20)
    moa_mail = models.EmailField(max_length=250)
    moa_logo = models.ImageField()


class Moe(models.Model):
    moe_name = models.CharField(max_length=250)
    moe_adress = models.CharField(max_length=500)
    moe_cp = models.IntegerField()
    moe_city = models.CharField(max_length=250)
    moe_phone = models.CharField(max_length=20)
    moe_fax = models.CharField(max_length=20)
    moe_mail = models.EmailField(max_length=250)
    moe_logo = models.ImageField()


class CctpChapter(models.Model):
    pass


class InfoDoc(models.Model):
    TYPE_CHOICES = [
        ('ESQ', 'esquisse'),
        ('PC', 'pc'),
        ('AVP', 'avp'),
        ('APS', 'aps'),
        ('APD', 'apd'),
        ('PRO', 'pro'),
        ('EXE', 'exe'),
        ('ACT', 'act'),
        ('DCE', 'dce'),
    ]

    doc_creator = models.CharField(max_length=20)
    doc_code = models.CharField(max_length=20)
    doc_type = models.Choices(TYPE_CHOICES)
    doc_indice = models.CharField(max_length=2)
    doc_date = models.DateTimeField()
