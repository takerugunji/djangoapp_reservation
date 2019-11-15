from django.db import models
from django.core.validators import RegexValidator

class Reservation(models.Model):

    check_in = models.DateField(verbose_name='チェックイン', blank=True, null=True,)
    check_out = models.DateField(verbose_name='チェックアウト', blank=True, null=True,)

    # name = models.CharField("名前", max_length=30, blank=True)
    
    # email = models.EmailField("メールアドレス", unique=True)

    # tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    # tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号')
    
    zip_code = models.CharField(verbose_name='郵便番号', max_length=8, blank=True,)
    address1 = models.CharField(verbose_name='都道府県',max_length=40,blank=True,)
    address2 = models.CharField(verbose_name='市区町村番地',max_length=40,blank=True,)
    # address3 = models.CharField(verbose_name='建物名',max_length=40,blank=True,)