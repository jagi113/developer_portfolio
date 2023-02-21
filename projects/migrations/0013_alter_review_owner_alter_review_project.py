# Generated by Django 4.1.5 on 2023-02-20 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
        ('projects', '0012_alter_review_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='users.profile', verbose_name='reviews'),
        ),
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='projects.project', verbose_name='reviews'),
        ),
    ]
