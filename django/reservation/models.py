from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

class Reservation(models.Model):

    check_in = models.DateField(verbose_name='チェックイン', blank=False, null=True,)
    check_out = models.DateField(verbose_name='チェックアウト', blank=False, null=True,)

    # first_name = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name=name,)
    # last_name = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name=last_name,)

    # email = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name=email)

    # phone = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name=phone)
    
    # tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    # tel_number = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号', blank=False, null=False,)
    
    zip_code = models.CharField(verbose_name='郵便番号', max_length=8, blank=False, null=True,)
    address1 = models.CharField(verbose_name='都道府県',max_length=40,blank=False, null=True,)
    address2 = models.CharField(verbose_name='市区町村番地',max_length=40,blank=False, null=True,)