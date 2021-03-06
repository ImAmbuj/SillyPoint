# Generated by Django 3.0.1 on 2021-12-15 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('C', 'Cricket'), ('F', 'Football')], max_length=20)),
                ('headline', models.TextField(max_length=70)),
                ('img', models.ImageField(null=True, upload_to='blog_imgs')),
                ('start', models.TextField(max_length=10000)),
                ('text', models.TextField(max_length=10000)),
            ],
        ),
    ]
