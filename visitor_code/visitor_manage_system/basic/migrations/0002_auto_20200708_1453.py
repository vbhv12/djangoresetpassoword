# Generated by Django 3.0.7 on 2020-07-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitdetails',
            old_name='visit_detail',
            new_name='visitor_detail',
        ),
        migrations.AddField(
            model_name='visitdetails',
            name='flat_no',
            field=models.CharField(default=' ', max_length=300),
        ),
        migrations.AlterField(
            model_name='host',
            name='Phone_no',
            field=models.CharField(default=' ', max_length=12),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
