# Generated by Django 4.1.7 on 2023-05-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_rename_contact_type_contact_typ'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['company']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
