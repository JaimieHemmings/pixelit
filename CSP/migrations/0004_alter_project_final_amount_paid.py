# Generated by Django 5.1 on 2024-09-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSP', '0003_remove_project_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='final_amount_paid',
            field=models.BooleanField(default=False),
        ),
    ]
