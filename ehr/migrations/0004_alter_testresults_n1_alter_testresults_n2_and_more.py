# Generated by Django 4.2 on 2023-09-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0003_rename_image_reports_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresults',
            name='n1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='n2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='n3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='n4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='n5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testresults',
            name='n6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]