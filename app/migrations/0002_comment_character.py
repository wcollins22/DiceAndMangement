# Generated by Django 3.2.7 on 2021-11-17 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.character'),
        ),
    ]