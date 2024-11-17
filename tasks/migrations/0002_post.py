# Generated by Django 5.1.2 on 2024-11-07 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_vendedor', models.CharField(max_length=255)),
                ('marca', models.CharField(default='Título', max_length=255)),
                ('año', models.IntegerField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('foto', models.ImageField(default='imagen', upload_to='foto/')),
            ],
        ),
    ]
