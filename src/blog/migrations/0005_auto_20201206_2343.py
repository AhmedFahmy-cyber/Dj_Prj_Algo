# Generated by Django 2.2.10 on 2020-12-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_appregs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appregs',
            name='wlaya',
            field=models.CharField(blank=True, choices=[('أدرار', 'أدرار'), ('الشلف', 'الشلف'), ('الأغواط', 'الأغواط')], max_length=100, null=True),
        ),
    ]
