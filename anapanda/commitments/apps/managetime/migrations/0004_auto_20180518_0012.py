# Generated by Django 2.0.5 on 2018-05-18 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managetime', '0003_auto_20180518_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='supercircle',
            field=models.ForeignKey(blank=True, default='Anchor Circle', null=True, on_delete=django.db.models.deletion.PROTECT, to='managetime.Circle'),
        ),
    ]