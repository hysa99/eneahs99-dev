# Generated by Django 4.1.7 on 2023-04-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(choices=[('bg-yellow-500', 'bg-yellow-500'), ('bg-pink-500', 'bg-pink-500'), ('bg-orange-500', 'bg-orange-500'), ('bg-blue-500', 'bg-blue-500')], default='bg-orange-500', max_length=50),
        ),
    ]
