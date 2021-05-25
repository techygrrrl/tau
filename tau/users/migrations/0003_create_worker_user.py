# Generated by Django 3.1.7 on 2021-05-20 21:28

from django.db import migrations

def create_worker_user(apps, schema_editor):
    User = apps.get_model('users', 'User')
    u = User.objects.filter(username='worker_process')
    if u.exists():
        print('WARNING: worker_process user already exists.  Exiting...')
        return
    User.objects.create(username='worker_process', can_login=False)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_can_login'),
    ]

    operations = [
        migrations.RunPython(create_worker_user)
    ]
