# Generated by Django 4.2.6 on 2023-10-11 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_in_bag_alter_item_id_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=4, serialize=False),
        ),
    ]
