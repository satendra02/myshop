# Generated by Django 3.0.8 on 2020-07-20 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0003_products_ctg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_categorie',
            name='catagory_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mystore.categorie', verbose_name='id'),
        ),
    ]
