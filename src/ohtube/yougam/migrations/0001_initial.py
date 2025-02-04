# Generated by Django 2.2 on 2019-05-28 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(default='', max_length=255)),
                ('cmt', models.TextField(default='')),
                ('label', models.IntegerField(default=3)),
                ('label6', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=255)),
                ('period', models.CharField(default='', max_length=255)),
                ('randnum', models.IntegerField(default=1)),
                ('like', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PieChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100)),
                ('json_data', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='TimeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_sentiment', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('img_path', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=255)),
                ('title', models.CharField(default='', max_length=255)),
                ('sentiment_neutral', models.IntegerField(default=0)),
                ('sentiment_happy', models.IntegerField(default=0)),
                ('sentiment_sad', models.IntegerField(default=0)),
                ('sentiment_surprise', models.IntegerField(default=0)),
                ('sentiment_anger', models.IntegerField(default=0)),
                ('sentiment_fear', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WebCam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=100)),
                ('json_data', models.CharField(max_length=400)),
                ('video_path', models.CharField(default='SOME STRING', max_length=400)),
                ('capture_path', models.ImageField(upload_to='')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.IntegerField(default=-1)),
                ('comment', models.TextField(default='')),
                ('pid', models.CharField(default='', max_length=255)),
                ('label', models.IntegerField(default=3)),
                ('label6', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=255)),
                ('like', models.IntegerField(default=0)),
                ('randnum', models.IntegerField(default=1)),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yougam.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yougam.Video'),
        ),
    ]
