# Generated by Django 4.1 on 2022-09-04 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0011_alter_auto_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='motorpool.brand'),
        ),
    ]
