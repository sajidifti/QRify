# Generated by Django 5.0.1 on 2024-02-04 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='qr_codes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
