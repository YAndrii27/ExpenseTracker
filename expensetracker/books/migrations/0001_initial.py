# Generated by Django 4.2.5 on 2023-09-29 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(max_length=128)),
                ('authors', models.CharField(max_length=64)),
                ('publisher', models.CharField(max_length=128)),
                ('published_date', models.DateField()),
                ('distribution_expense', models.FloatField()),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book_categories.bookcategory')),
            ],
        ),
    ]
