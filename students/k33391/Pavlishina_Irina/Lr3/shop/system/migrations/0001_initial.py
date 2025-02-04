# Generated by Django 4.2.7 on 2023-12-18 10:49

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('index', models.CharField(max_length=100)),
                ('redactor_last_name', models.CharField(max_length=100)),
                ('redactor_first_name', models.CharField(max_length=100)),
                ('redactor_patronic', models.CharField(max_length=100)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PostOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PostOfficeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many_needed', models.IntegerField()),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='needed_in', to='system.newspaper')),
                ('post_office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='what_is_needed', to='system.postoffice')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('max_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PrintingNewspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_many_to_print', models.IntegerField()),
                ('newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='where_to_print', to='system.newspaper')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='what_is_printed', to='system.printer')),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('post_office_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printed_by', to='system.postofficeorder')),
                ('printing_newspaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printed_for', to='system.printingnewspaper')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.TextField(choices=[('A', 'A'), ('P', 'P'), ('PO', 'PO'), ('N', 'N')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('linkedin_token', models.TextField(blank=True, default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
