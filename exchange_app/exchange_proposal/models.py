from django.db import models

from exchange_app.ad.models import Ad
from exchange_app.user.models import User


class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'ожидает'),
        ('accepted', 'принята'),
        ('canceled', 'отменена'),
    ]
    sender_id = models.ForeignKey(
        User,
        related_name='sender',
        on_delete=models.CASCADE,
        verbose_name=('Sender')
    )
    reciever_id = models.ForeignKey(
        User,
        related_name='reciever',
        on_delete=models.CASCADE,
        verbose_name=('Reciever')
    )
    ad_id = models.ForeignKey(
        Ad,
        related_name='ads',
        on_delete=models.PROTECT,
        verbose_name='Ads')
    status = models.CharField(
        choices=STATUS_CHOICES,
        verbose_name='Status',
        default='waiting'
    )
    comment = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Comment'
    )
