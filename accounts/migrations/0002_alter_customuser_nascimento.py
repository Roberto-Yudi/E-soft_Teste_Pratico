# Generated by Django 3.2.8 on 2021-10-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nascimento',
            field=models.DateField(help_text='MM/DD/AA', null=True),
        ),
    ]