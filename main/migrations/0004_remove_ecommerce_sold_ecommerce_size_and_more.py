# Generated by Django 5.1.1 on 2024-09-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_ecommerce_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ecommerce',
            name='sold',
        ),
        migrations.AddField(
            model_name='ecommerce',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='M', max_length=3),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='price',
            field=models.IntegerField(default=1500000),
        ),
    ]
