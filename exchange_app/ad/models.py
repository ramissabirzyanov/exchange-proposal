from django.db import models

from exchange_app.user.models import User
from exchange_app.category.models import Category


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=('Name')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=('Discription')
    )
    owner = models.ForeignKey(
        User,
        related_name='ads',
        on_delete=models.CASCADE,
        verbose_name=('Owner')
    )
    category = models.ForeignKey(
        Category,
        related_name='ads',
        on_delete=models.PROTECT,
        verbose_name=('Category')
    )
    image_url = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Image_url'
    )
    condition = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Condition'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    class Meta:
        ordering = ['id']
        db_table = 'Ad'
        verbose_name = ('Ad')