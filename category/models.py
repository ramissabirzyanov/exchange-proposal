from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            verbose_name=('Name'))

    class Meta:
        ordering = ['id']
        db_table = 'Category'
        verbose_name = ('Category')

    def __str__(self):
        return self.name
