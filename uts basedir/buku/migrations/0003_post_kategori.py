# Generated by Django 2.2 on 2022-11-12 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0002_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kategori',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buku.kategori'),
        ),
    ]
