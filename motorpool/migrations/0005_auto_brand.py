# Generated by Django 4.1 on 2022-09-03 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0004_auto_alter_brand_options_alter_brand_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='motorpool.brand'),
        ),
    ]