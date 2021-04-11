# Generated by Django 3.1.6 on 2021-04-11 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='patient', serialize=False, to='auth.user')),
                ('age', models.IntegerField(default=0)),
                ('phone_number', models.CharField(default='01111111', max_length=15)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(default='none', max_length=10)),
                ('gender', models.CharField(default='O', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_appoinments', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.patient')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(max_length=20)),
                ('cvv', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=60)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.patient')),
            ],
        ),
    ]
