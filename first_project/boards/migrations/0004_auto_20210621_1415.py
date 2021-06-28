# Generated by Django 3.2.4 on 2021-06-21 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0003_auto_20210620_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topic',
            name='updated_dt',
            field=models.DateTimeField(null=True),
        ),
    ]
