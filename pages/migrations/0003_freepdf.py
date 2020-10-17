# Generated by Django 3.0.7 on 2020-10-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contacto_redessociales_suscriptor_web'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreePdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('file', models.FileField(upload_to='pdf')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
