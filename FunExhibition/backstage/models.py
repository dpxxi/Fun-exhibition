from django.db import models


class User(models.Model):
    """user"""
    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = 'user'

    status = models.IntegerField(verbose_name='STATUS', default=0)  
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Creation time
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)  # update time
    name = models.CharField(verbose_name='USERNAME', max_length=100)
    public_name = models.CharField(verbose_name='PUBLIC NAME', max_length=100, null=True, blank=True)
    country = models.CharField(verbose_name='COUNTRY', max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name='CITY', max_length=100, null=True, blank=True)
    pwd = models.CharField(verbose_name='PWD', max_length=100)
    phone = models.CharField(verbose_name='PHONE', max_length=100, null=True, blank=True)
    email = models.CharField(verbose_name='E-MAIL', max_length=100, null=True, blank=True)
    money = models.FloatField(verbose_name='MONEY', default=0)
    admin_level = models.IntegerField(verbose_name='admin level', default=0)  # 0 normal users, 1 administrator
    image = models.ImageField(upload_to='user_img', default="user_img/user.png")
    code = models.CharField(max_length=250, null=True, blank=True, verbose_name='code')


class Address(models.Model):
    """user's address"""
    class Meta:
        verbose_name = verbose_name_plural = 'address'
        db_table = 'address'

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='user')
    country = models.CharField(verbose_name='COUNTRY', max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name='CITY', max_length=100, null=True, blank=True)
    address_info = models.TextField(null=True, blank=True, verbose_name='address_info')
    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)


class Artwork(models.Model):
    """artworks"""
    class Meta:
        db_table = 'artwork'
        verbose_name = verbose_name_plural = 'artwork'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    img = models.ImageField(null=True, upload_to='artwork_img')
    artist = models.CharField(verbose_name='artist', max_length=200, null=True, blank=True)
    artist_letter = models.CharField(verbose_name='artist_letter', max_length=10, null=True, blank=True)
    year = models.IntegerField(verbose_name='year', null=True, blank=True)
    time = models.CharField(verbose_name='time', max_length=200, null=True, blank=True)
    medium = models.ForeignKey('Medium', verbose_name='medium_id', null=True, blank=True, on_delete=models.CASCADE, related_name='artwork_medium')
    title = models.CharField(verbose_name='title', max_length=200)
    content = models.TextField(verbose_name='content')
    like_number = models.IntegerField(verbose_name='fabulous_number', default=0)
    look_number = models.IntegerField(verbose_name='look_number', default=0)
    comment_number = models.IntegerField(verbose_name='comment_number', default=0)
    fabulous_number = models.IntegerField(verbose_name='like_number', default=0)

    def __str__(self):
        return self.title


class OnNowArtwork(models.Model):
    """on now"""
    class Meta:
        db_table = 'onNowArtwork'
        verbose_name = verbose_name_plural = 'onNowArtwork'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    on_now_artwork = models.ForeignKey('Artwork', verbose_name='artwork', null=True, blank=True, on_delete=models.CASCADE, related_name='on_now_artwork')
    sequence = models.IntegerField(verbose_name='sequence', default=0)


class Medium(models.Model):
    class Meta:
        db_table = 'medium'
        verbose_name = verbose_name_plural = 'medium'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    name = models.CharField(verbose_name='medium_id', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Like(models.Model):  # Currently unused model
    class Meta:
        db_table = 'like'
        verbose_name = verbose_name_plural = 'fabulous'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    like_artwork = models.ForeignKey('Artwork', verbose_name='artwork', null=True, blank=True, on_delete=models.CASCADE, related_name='like_artwork')
    like_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='like_user')


class Comment(models.Model):
    """comments"""
    class Meta:
        db_table = 'comment'
        verbose_name = verbose_name_plural = 'comment'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    parent = models.ForeignKey('Comment', verbose_name='回复人', null=True, on_delete=models.CASCADE, related_name='parent_comment', default=None)
    comment_artwork = models.ForeignKey('Artwork', verbose_name='artwork', null=True, blank=True, on_delete=models.CASCADE, related_name='comment_artwork')
    comment_user = models.ForeignKey('User', verbose_name='comment_user', null=True, blank=True, on_delete=models.CASCADE, related_name='comment_user')
    comment_text = models.CharField(verbose_name='comment_text', max_length=2000)
    fabulous_num = models.IntegerField(verbose_name="fabulous_num", default=0)  #Number of fabulous

    @property
    def get_children(self):
        return Comment.objects.filter(status=0, parent=self).order_by('-id')


class FabulousComment(models.Model):
    """Like the comment"""
    class Meta:
        db_table = 'fabulousComment'
        verbose_name = verbose_name_plural = 'fabulousComment'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    fabulous_Comment = models.ForeignKey('Comment', verbose_name='comment', null=True, blank=True, on_delete=models.CASCADE, related_name='fabulous_Comment')
    fabulousComment_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='fabulousComment_user')


class Fabulous(models.Model):
    """thumbs up"""
    class Meta:
        db_table = 'fabulous'
        verbose_name = verbose_name_plural = 'fabulous'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    fabulous_artwork = models.ForeignKey('Artwork', verbose_name='artwork', null=True, blank=True, on_delete=models.CASCADE, related_name='fabulous_artwork')
    fabulous_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='fabulous_user')


class Browse(models.Model):
    """Browsing history"""
    class Meta:
        db_table = 'browse'
        verbose_name = verbose_name_plural = 'browse'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    browse_artwork = models.ForeignKey('Artwork', verbose_name='artist', null=True, blank=True, on_delete=models.CASCADE, related_name='browse_artwork')
    browse_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='browse_user')
    browse_commodity = models.ForeignKey('Commodity', verbose_name='商品', null=True, blank=True, on_delete=models.CASCADE, related_name='browse_commodity')


class HomeSelected(models.Model):
    """homeselect"""
    class Meta:
        db_table = 'homeSelected'
        verbose_name = verbose_name_plural = 'homeSelected'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    home_artwork = models.ForeignKey('Artwork', verbose_name='artwork', null=True, blank=True, on_delete=models.CASCADE, related_name='home_artwork')
    sequence = models.IntegerField(verbose_name='sequence', default=0)  


class Commodity(models.Model):
    """commodity"""
    class Meta:
        db_table = 'commodity'
        verbose_name = verbose_name_plural = 'commodity'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    img = models.ImageField(verbose_name='img', upload_to='shopping', null=True, blank=True)
    title = models.CharField(verbose_name='title', max_length=100)
    describe = models.CharField(verbose_name='describe', max_length=300)
    money = models.FloatField(verbose_name='money')
    number = models.IntegerField(verbose_name='number', default=0)
    sell_number = models.IntegerField(verbose_name='sell_number', default=0)
    description = models.TextField(verbose_name='description', null=True, blank=True)
    detail = models.TextField(verbose_name='detail', null=True, blank=True)


class ShoppingCart(models.Model):
    class Meta:
        db_table = 'shoppingCart'
        verbose_name = verbose_name_plural = 'shoppingCart'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    shoppingCart_commodity = models.ForeignKey('Commodity', verbose_name='commodity', null=True, blank=True, on_delete=models.CASCADE, related_name='shoppingCart_commodity')
    shoppingCart_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='shoppingCart_user')
    shopping_num = models.IntegerField(verbose_name='number', default=1)
    flag = models.IntegerField(verbose_name='status', default=0)  # 0 with payment, 1 paid successfully, -1 cancelled payment
    order_num = models.CharField(verbose_name='sell_number', max_length=100, blank=True, null=True)


class Order(models.Model):
    """order"""
    class Meta:
        db_table = 'order'
        verbose_name = verbose_name_plural = 'order'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    order_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='order_user')
    order_num = models.CharField(verbose_name='sell_number', max_length=100, blank=True, null=True)
    order_money = models.FloatField(verbose_name="money", default=0)
    address = models.ForeignKey('Address', null=True, blank=True, verbose_name='address', on_delete=models.CASCADE)

    # Property method, according to the order number to find enough goods sold
    @property
    def get_shopping(self):
        shoppings = ShoppingCart.objects.filter(order_num=self.order_num, flag=0)
        return shoppings


class Proposal(models.Model):
    """proposal"""
    class Meta:
        db_table = 'proposal'
        verbose_name = verbose_name_plural = 'proposal'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    name = models.CharField(verbose_name='USERNAME', max_length=100)
    email = models.CharField(verbose_name='E-MAIL', max_length=100, null=True, blank=True)
    subject = models.CharField(verbose_name='subject', max_length=100, null=True, blank=True)
    message = models.TextField(verbose_name='message', null=True, blank=True)


class News(models.Model):
    """news"""
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = 'news'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    img = models.ImageField(null=True, upload_to='news_img')
    title = models.CharField(verbose_name='title', max_length=200)
    describe = models.CharField(verbose_name='describe', max_length=1000)
    content = models.TextField(verbose_name='content')
    artist = models.CharField(verbose_name='artist', max_length=200, null=True, blank=True)
    time = models.CharField(verbose_name='time', max_length=200, null=True, blank=True)
    news_user = models.ForeignKey('User', verbose_name='Upload users', null=True, blank=True, on_delete=models.CASCADE, related_name='news_user')

    def __str__(self):
        return self.title


class Education(models.Model):
    """education"""
    class Meta:
        db_table = 'education'
        verbose_name = verbose_name_plural = 'education'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    img = models.ImageField(null=True, upload_to='education_img')
    title = models.CharField(verbose_name='title', max_length=200)
    describe = models.CharField(verbose_name='describe', max_length=1000)
    content = models.TextField(verbose_name='content')
    education_user = models.ForeignKey('User', verbose_name='Upload users', null=True, blank=True, on_delete=models.CASCADE, related_name='education_user')


class Remind(models.Model):
    """User information reminder"""
    class Meta:
        db_table = 'remind'
        verbose_name = verbose_name_plural = 'remind'

    status = models.IntegerField(verbose_name='STATUS', default=0)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    flag = models.IntegerField(verbose_name='status', default=0)  # 0 not viewed
    remind_comment = models.ForeignKey('Comment', verbose_name='数据', null=True, blank=True, on_delete=models.CASCADE, related_name='remind_comment')
    remind_user = models.ForeignKey('User', verbose_name='user', null=True, blank=True, on_delete=models.CASCADE, related_name='remind_user')
