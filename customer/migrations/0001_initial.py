# Generated by Django 2.0 on 2017-12-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=9)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(blank=True, upload_to='images/avatars/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
            },
        ),
    ]