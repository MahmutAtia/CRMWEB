# Generated by Django 4.1.7 on 2023-05-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_alter_contact_options_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
