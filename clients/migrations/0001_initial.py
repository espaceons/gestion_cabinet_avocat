# Generated by Django 5.2.1 on 2025-05-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type_client', models.CharField(choices=[('PARTICULIER', 'Particulier'), ('ENTREPRISE', 'Entreprise')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
