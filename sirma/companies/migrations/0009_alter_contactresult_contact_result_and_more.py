# Generated by Django 4.1.7 on 2023-05-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactresult',
            name='contact_result',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contacttype',
            name='contact_type',
            field=models.CharField(max_length=20),
        ),
    ]
