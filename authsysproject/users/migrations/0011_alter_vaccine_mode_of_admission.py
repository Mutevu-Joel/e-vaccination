# Generated by Django 4.0.6 on 2022-09-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_vaccine_name_vaccine_mode_of_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='mode_of_admission',
            field=models.CharField(choices=[('oral', 'oral'), ('injection', 'injection')], max_length=50, null=True),
        ),
    ]
