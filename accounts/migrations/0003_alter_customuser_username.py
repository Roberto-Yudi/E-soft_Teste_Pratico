# Generated by Django 3.2.8 on 2021-10-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]
