# Generated by Django 3.2.8 on 2021-10-27 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tree_type', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('fruit_bearing', models.CharField(blank=True, max_length=50, null=True)),
                ('season', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'type_db',
            },
        ),
        migrations.CreateModel(
            name='MainDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.CharField(blank=True, max_length=50, null=True)),
                ('trunk_circumference', models.IntegerField(blank=True, null=True)),
                ('year_planted', models.CharField(blank=True, max_length=50, null=True)),
                ('health', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('sector', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.typedb')),
            ],
            options={
                'db_table': 'main_db',
            },
        ),
    ]
