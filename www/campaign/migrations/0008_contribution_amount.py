# Generated by Django 4.0.3 on 2022-03-08 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0007_remove_contribution_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='contribution',
            name='amount',
            field=models.DecimalField(decimal_places=12, default=0.0, max_digits=16),
            preserve_default=False,
        ),
    ]