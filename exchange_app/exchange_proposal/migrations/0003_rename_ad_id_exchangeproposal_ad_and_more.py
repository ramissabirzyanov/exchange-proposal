# Generated by Django 5.2 on 2025-04-16 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_proposal', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchangeproposal',
            old_name='ad_id',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='exchangeproposal',
            old_name='reciever_id',
            new_name='reciever',
        ),
        migrations.RenameField(
            model_name='exchangeproposal',
            old_name='sender_id',
            new_name='sender',
        ),
    ]
