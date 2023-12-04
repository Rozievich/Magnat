# Generated by Django 4.2.7 on 2023-12-04 06:10

from django.db import migrations, models
import magnat.custom_validator


class Migration(migrations.Migration):

    dependencies = [
        ('magnat', '0004_client_sana'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='blog/', validators=[magnat.custom_validator.validate_image])),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Worker',
            new_name='Hodim',
        ),
        migrations.RenameModel(
            old_name='Client',
            new_name='Mijoz',
        ),
        migrations.RenameModel(
            old_name='Media',
            new_name='Portfolio',
        ),
        migrations.RenameModel(
            old_name='MediaCategory',
            new_name='PortfolioKategoriya',
        ),
        migrations.AlterModelOptions(
            name='hodim',
            options={'ordering': ['created_at'], 'verbose_name': 'Hodim', 'verbose_name_plural': 'Hodimlar'},
        ),
        migrations.AlterModelOptions(
            name='mijoz',
            options={'ordering': ['-created_at', '-update_at'], 'verbose_name': 'Mijoz', 'verbose_name_plural': 'Mijozlar'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['-created_at', '-update_at'], 'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfoliolar'},
        ),
        migrations.AlterModelOptions(
            name='portfoliokategoriya',
            options={'verbose_name': 'PortfolioKategoriya', 'verbose_name_plural': 'PortfolioKategoriyalar'},
        ),
    ]
