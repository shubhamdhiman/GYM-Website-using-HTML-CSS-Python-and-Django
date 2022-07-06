# Generated by Django 4.0.4 on 2022-07-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_delete_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
