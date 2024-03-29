# Generated by Django 4.2.7 on 2024-02-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0002_rename_name_prot_lname_prot_fname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('image', models.FileField(null=True, upload_to='static/uploads')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=200, null=True)),
                ('college_address', models.CharField(max_length=200, null=True)),
                ('date_frm', models.DateField()),
                ('date_end', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('company_address', models.CharField(max_length=200, null=True)),
                ('date_frm', models.DateField()),
                ('date_end', models.DateField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True)),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='prot',
            name='lname',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
