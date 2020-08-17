# Generated by Django 3.0.8 on 2020-08-17 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200730_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Receita')),
            ],
        ),
    ]