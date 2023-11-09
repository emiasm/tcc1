# Generated by Django 4.2.7 on 2023-11-08 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bairro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo_rua', models.CharField(choices=[('Urbana', 'Urbana'), ('Rural', 'Rural')], max_length=100)),
                ('data_adicao', models.DateTimeField(auto_now_add=True)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bairro.bairro')),
            ],
        ),
    ]
