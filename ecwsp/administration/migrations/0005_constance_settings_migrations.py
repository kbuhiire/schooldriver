# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from constance import config

            
def configuration_to_constance(apps, schema_editor):
    """adds Configuration object data to Constance Config in settings"""
    Configuration = apps.get_model("administration", "Configuration")  
    settings_to_migrate = ['Discipline Merit Default Days', 'Discipline Merit Level One', 'Discipline Merit Level Two', 
    'Discipline Merit Level Three', 'Discipline Merit Level Four', 
    'attendance_disc_tardies_before_disc', 'attendance_disc_infraction', 'attendance_disc_action']
    for each_config in settings_to_migrate:
        configs = Configuration.objects.filter(name=each_config).first()
        if configs:
            config_name = configs.name
            config_value = configs.value
            formatted_config = config_name.replace(" ", "_").replace("-", "_").upper
            formatted = str(formatted_config())
            setattr(config, formatted, '')
        else:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_constance_settings_migrations'),
    ]

    operations = [
        migrations.RunPython(configuration_to_constance),

        
    ]