# Generated by Django 2.1.15 on 2020-10-27 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='COUNTRY')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='CITY')),
                ('address_info', models.TextField(blank=True, null=True, verbose_name='详细地址')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '地址',
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.ImageField(null=True, upload_to='artwork_img')),
                ('artist', models.CharField(blank=True, max_length=200, null=True, verbose_name='艺术家')),
                ('artist_letter', models.CharField(blank=True, max_length=10, null=True, verbose_name='艺术家首字母')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='年份')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('describe', models.CharField(max_length=1000, verbose_name='描述')),
                ('content', models.TextField(verbose_name='内容')),
                ('like_number', models.IntegerField(default=0, verbose_name='喜欢人数')),
                ('look_number', models.IntegerField(default=0, verbose_name='关看人数')),
                ('comment_number', models.IntegerField(default=0, verbose_name='评论数')),
                ('fabulous_number', models.IntegerField(default=0, verbose_name='点赞数')),
            ],
            options={
                'verbose_name': '艺术品表',
                'verbose_name_plural': '艺术品表',
                'db_table': 'artwork',
            },
        ),
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('browse_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='browse_artwork', to='backstage.Artwork', verbose_name='艺术品')),
            ],
            options={
                'verbose_name': '浏览记录',
                'verbose_name_plural': '浏览记录',
                'db_table': 'browse',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('comment_text', models.CharField(max_length=2000, verbose_name='评论内容')),
                ('comment_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_artwork', to='backstage.Artwork', verbose_name='艺术品')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='shopping', verbose_name='img')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('describe', models.CharField(max_length=300, verbose_name='describe')),
                ('money', models.FloatField(verbose_name='money')),
                ('number', models.IntegerField(default=0, verbose_name='number')),
                ('sell_number', models.IntegerField(default=0, verbose_name='sell_number')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'commodity',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.ImageField(null=True, upload_to='education_img')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('describe', models.CharField(max_length=1000, verbose_name='描述')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '教育',
                'verbose_name_plural': '教育',
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='Fabulous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('fabulous_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fabulous_artwork', to='backstage.Artwork', verbose_name='艺术品')),
            ],
            options={
                'verbose_name': '点赞表',
                'verbose_name_plural': '点赞表',
                'db_table': 'fabulous',
            },
        ),
        migrations.CreateModel(
            name='HomeSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('sequence', models.IntegerField(default=0, verbose_name='序号')),
                ('home_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_artwork', to='backstage.Artwork', verbose_name='艺术品')),
            ],
            options={
                'verbose_name': '精选',
                'verbose_name_plural': '精选',
                'db_table': 'homeSelected',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('like_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_artwork', to='backstage.Artwork', verbose_name='艺术品')),
            ],
            options={
                'verbose_name': '喜爱表',
                'verbose_name_plural': '喜爱表',
                'db_table': 'like',
            },
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='类型名')),
            ],
            options={
                'verbose_name': '类型表',
                'verbose_name_plural': '类型表',
                'db_table': 'medium',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.ImageField(null=True, upload_to='news_img')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('describe', models.CharField(max_length=1000, verbose_name='描述')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='OnNowArtwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('sequence', models.IntegerField(default=0, verbose_name='序号')),
                ('on_now_artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='on_now_artwork', to='backstage.Artwork', verbose_name='艺术品')),
            ],
            options={
                'verbose_name': '正在展出的',
                'verbose_name_plural': '正在展出的',
                'db_table': 'onNowArtwork',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('order_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='订单号')),
                ('order_money', models.FloatField(default=0, verbose_name='订单金额')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backstage.Address', verbose_name='地址')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='USERNAME')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='E-MAIL')),
                ('subject', models.CharField(blank=True, max_length=100, null=True, verbose_name='subject')),
                ('message', models.TextField(blank=True, null=True, verbose_name='message')),
            ],
            options={
                'verbose_name': '建议',
                'verbose_name_plural': '建议',
                'db_table': 'proposal',
            },
        ),
        migrations.CreateModel(
            name='Remind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('flag', models.IntegerField(default=0, verbose_name='状态')),
                ('remind_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remind_comment', to='backstage.Comment', verbose_name='数据')),
            ],
            options={
                'verbose_name': '消息提醒',
                'verbose_name_plural': '消息提醒',
                'db_table': 'remind',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('shopping_num', models.IntegerField(default=1, verbose_name='数量')),
                ('flag', models.IntegerField(default=0, verbose_name='状态')),
                ('order_num', models.CharField(blank=True, max_length=100, null=True, verbose_name='订单号')),
                ('shoppingCart_commodity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoppingCart_commodity', to='backstage.Commodity', verbose_name='商品')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'shoppingCart',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='STATUS')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='USERNAME')),
                ('public_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='PUBLIC NAME')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='COUNTRY')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='CITY')),
                ('pwd', models.CharField(max_length=100, verbose_name='PWD')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='PHONE')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='E-MAIL')),
                ('money', models.FloatField(default=0, verbose_name='MONEY')),
                ('admin_level', models.IntegerField(default=0, verbose_name='admin level')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_img')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shoppingCart_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoppingCart_user', to='backstage.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='remind',
            name='remind_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remind_user', to='backstage.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to='backstage.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='like',
            name='like_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to='backstage.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='fabulous',
            name='fabulous_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fabulous_user', to='backstage.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='backstage.User', verbose_name='评论用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='backstage.Comment', verbose_name='回复人'),
        ),
        migrations.AddField(
            model_name='browse',
            name='browse_commodity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='browse_commodity', to='backstage.Commodity', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='browse',
            name='browse_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='browse_user', to='backstage.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='medium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artwork_medium', to='backstage.Medium', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backstage.User', verbose_name='用户'),
        ),
    ]
