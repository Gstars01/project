# Generated by Django 3.2 on 2021-05-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=64, verbose_name='사용자 아이디')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('emali', models.EmailField(max_length=128, verbose_name='이메일')),
                ('nick_name', models.CharField(max_length=32, verbose_name='닉네임')),
                ('registered_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'DOGE 사용자',
                'verbose_name_plural': 'DOGE 사용자',
                'db_table': 'DOGE_user',
            },
        ),
    ]
