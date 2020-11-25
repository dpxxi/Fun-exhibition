import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render, redirect
from backstage.models import *
from django.views.decorators.csrf import csrf_exempt
from .decorators import user_required
from django.db.models import Q
from django.http import JsonResponse
import datetime


@csrf_exempt  # Remove Django's csrf check function in this view request, and no security check.
def backstage_user(request):
    """Edit user information in the background"""
    ctx = {}
    q = ''
    action = request.POST.get('action', '')
    # Update user information
    if action == 'update_user':
        id = request.POST.get('user_id')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        money = request.POST.get('money')
        status = request.POST.get('status', '0')
        admin_level = request.POST.get('admin_level', '0')
        get_user = User.objects.filter(id=id).first()
        if get_user:
            get_user.name = name
            get_user.phone = phone
            get_user.email = email
            get_user.money = money
            get_user.status = status
            get_user.admin_level = admin_level
            get_user.save()
    # add new user
    if action == 'add_user':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        money = request.POST.get('money')
        status = request.POST.get('status', '0')
        admin_level = request.POST.get('admin_level', '0')
        get_user = User.objects.filter(name=name).first()
        if not get_user:
            User.objects.create(name=name, phone=phone, email=email, money=money, status=status, admin_level=admin_level)
    # View User Information
    users = User.objects.all()
    if action == 'select_action':
        q = request.POST.get('q', '')
        if q:
            users = users.filter(Q(name__icontains=q) | Q(email__icontains=q))

    ctx['users'] = users
    ctx['q'] = q
    return render(request, 'backstage_user.html', ctx)


@csrf_exempt
@user_required
def backstage_works(request):
    ctx = {}
    q = ''
    action = request.POST.get('action', '')
    # update user
    if action == 'update_user':
        id = request.POST.get('user_id')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        money = request.POST.get('money')
        status = request.POST.get('status', '0')
        admin_level = request.POST.get('admin_level', '0')
        get_user = User.objects.filter(id=id).first()
        if get_user:
            get_user.name = name
            get_user.phone = phone
            get_user.email = email
            get_user.money = money
            get_user.status = status
            get_user.admin_level = admin_level
            get_user.save()
    # add_user
    if action == 'add_user':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        money = request.POST.get('money')
        status = request.POST.get('status', '0')
        admin_level = request.POST.get('admin_level', '0')
        get_user = User.objects.filter(name=name).first()
        if not get_user:
            User.objects.create(name=name, phone=phone, email=email, money=money, status=status, admin_level=admin_level)
    # select user
    users = User.objects.all()
    if action == 'select_action':
        q = request.POST.get('q', '')
        if q:
            users = users.filter(Q(name__icontains=q) | Q(email__icontains=q))

    ctx['users'] = users
    ctx['q'] = q
    return render(request, 'backstage_works.html', ctx)


def send_sms(sms_to, content):
    """Send mail method"""
    msg_from = '2738304473@qq.com'  # Sender's email
    passwd = 'xnkrnwgnlupodeje'  # Fill in the authorization code of the sender's mailbox
    msg_to = sms_to  # Recipient email address
    subject = 'welcome to "Fun"'  # title
    content = content  # content
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # Mail server and port number
        s.login(msg_from, passwd)  # Log in to the SMTP server
        s.sendmail(msg_from, msg_to, msg.as_string())  # Email as_string() to change the MIMEText object to STR
    except s.SMTPException:
        print("Send failure")
    finally:
        s.quit()


@csrf_exempt
def logout(request):
    """logout"""
    request.session.flush()
    return redirect('/index_home/')


@csrf_exempt
def login_ajax(request):
    """login"""
    action = request.POST.get('action')
    if action == 'login_action':
        username = request.POST.get('username')
        password = request.POST.get('password')
        get_user = User.objects.filter(name=username, pwd=password, status=0).first()
        if get_user:
            request.session['uid'] = get_user.id
            return JsonResponse({'code': 0, "data": "success"})
        else:
            return JsonResponse({'code': -1, "data": "Wrong user name or password, please re-enter!"})


@csrf_exempt
def register_ajax(request):
    """register"""
    action = request.POST.get('action')
    if action == 'create_user_action':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        get_user = User.objects.filter(name=username, status=0).first()
        if get_user:
            return JsonResponse({'code': -1, "data": "The user name already exists, please change the user name!"})
        else:
            User.objects.create(status=0, name=username, pwd=password, country=country, email=email, city=city)
            content = "Dear" + username + "：Welcome to the “fun” online art exhibition family, enjoy the visual feast we bring you here!"
            send_sms(email, content)  # Success to register and sign up to send mail
            return JsonResponse({'code': 0, "data": "success"})


@csrf_exempt
def find_password(request):
    """Retrieve Password"""
    import random
    action = request.POST.get('action', '')

    number = []
    for i in range(6):
        rand_num = random.randint(0, 9)
        number.append(str(rand_num))
    num = ''.join(number)

    if action == 'find_pass':
        name = request.POST.get('name', '')
        get_user = User.objects.filter(name=name, status=0).first()
        if get_user:
            get_user.code = num
            get_user.save()
            num = "Dear" + get_user.name + ": Sorry to hear that you forgot your password, but don't worry, here is the captcha code provided for you by the website, please enter the " + get_user.name + " in the specified location,code:" + num
            send_sms(get_user.email, num)  # Forget your password to send an email
    return JsonResponse({'code': 0})


@csrf_exempt
def edit_password(request):
    """Repeat Password"""
    action = request.POST.get('action', '')

    if action == 'edit_pass':
        name = request.POST.get('name', '')
        code = request.POST.get('code', '')
        new_password_id = request.POST.get('new_password_id', '')
        user = User.objects.filter(name=name, code=code, status=0).first()
        if user:
            user.pwd = new_password_id
            user.save()
        else:
            return JsonResponse({'code': -1, 'err': 'error code'})
    return JsonResponse({'code': '0'})


@csrf_exempt
def touch(request):
    """User gives advice"""
    touch_name = request.POST.get('touch_name', '')
    touch_email = request.POST.get('touch_email', '')
    touch_subject = request.POST.get('touch_subject', '')
    touch_message = request.POST.get('touch_message', '')
    if touch_name and touch_message and touch_subject and touch_email:
        Proposal.objects.create(name=touch_name, email=touch_email, subject=touch_subject, message=touch_message)
        content = "email：" + str(touch_email) + "message:" + str(touch_message)
        send_sms('2738304473@qq.com', content) # Submitted email sent successfully
    return JsonResponse({'data': 'success'})


@csrf_exempt
def index_support_us(request):
    """support us"""
    ctx = {}
    user = ''
    remind = []
    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
        # Determine if there is data available
        if user:
            remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    ctx['remind'] = remind
    ctx['user'] = user
    return render(request, 'index_support_us.html', ctx)


@csrf_exempt
def index_home(request):
    """homepage"""
    ctx = {}
    user = ''
    remind = []
    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
        if user:
            remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    artwork_lists = Artwork.objects.filter(status=0).order_by('-look_number')[0:3]  # Artwork should be ranked top 3 by the number of views
    home_selected_list = HomeSelected.objects.filter(status=0).order_by('sequence')[0:3]  
    ctx['home_selected_list'] = home_selected_list
    ctx['user'] = user
    ctx['artwork_lists'] = artwork_lists
    ctx['remind'] = remind
    return render(request, 'index_home.html', ctx)


@csrf_exempt
def index_exhibition(request):
    """exhibition model"""
    ctx = {}
    user = ''
    action = request.POST.get('action')
    artist = 'A-Z'  # artist
    year = '0'  # year
    medium = 'all'  # medium
    search = ''  # Enter the condition that you are querying
    onnows_id_list = []  # # Store ID that are on display
    more_flag = 'false'  # false No data available
    remind = []

    # Determine if a user exists
    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
        if user:
            remind = Remind.objects.filter(flag=0, status=0, remind_user=user)
    onnows = OnNowArtwork.objects.filter(status=0).order_by('sequence')[0:6]  # Select the top three artworks on the homepage
    for x in onnows:
        onnows_id_list.append(x.on_now_artwork.id)

    # Load the rest of the artwork
    if action == 'more_data_action':
        data_list = []  # Store the data loaded by clicking more
        page_index = request.POST.get('page_index', '1')
        artist = request.POST.get('artist', 'A-Z')
        year = request.POST.get('year', '0')
        medium = request.POST.get('medium', 'all')
        search = request.POST.get('search', '')
        page_index = int(page_index)
        page_end_index = int(page_index) + 1

        # Check what is on display
        onnows = OnNowArtwork.objects.filter(status=0)
        # Determine whether the user chooses artist, year, medium and search
        if artist != 'A-Z':
            onnows = onnows.filter(on_now_artwork__artist_letter=artist)
        if year != '0':
            onnows = onnows.filter(on_now_artwork__year=year)
        if medium != 'all':
            onnows = onnows.filter(on_now_artwork__medium__name=medium)
        if search:
            onnows = onnows.filter(
                Q(on_now_artwork__artist__icontains=search) | Q(on_now_artwork__title__icontains=search))
        onnows = onnows.order_by('sequence')[0:6]
        for x in onnows:
            onnows_id_list.append(x.on_now_artwork.id)

        past_exhibitions = Artwork.objects.filter(status=0).exclude(id__in=onnows_id_list)  
        if artist != 'A-Z':
            past_exhibitions = past_exhibitions.filter(artist=artist)
        if year != '0':
            past_exhibitions = past_exhibitions.filter(year=year)
        if medium != 'all':
            past_exhibitions = past_exhibitions.filter(medium__name=medium)
        if search:
            past_exhibitions = past_exhibitions.filter(Q(artist__icontains=search) | Q(title__icontains=search))

        # Determine if the More button also needs to be generated, Eight pieces of data per page
        if past_exhibitions.count() > 8 * page_end_index:
            more_flag = 'true'

        past_exhibitions = past_exhibitions[page_index * 8:page_end_index * 8]
        for _ in past_exhibitions:
            data_dict = {}
            data_dict['data_img'] = _.img.url
            data_dict['title'] = _.title
            data_dict['id'] = _.id
            data_dict['year'] = _.year
            data_dict['artist'] = _.artist
            data_list.append(data_dict)
        return JsonResponse({"data": data_list, "more_flag": more_flag})

    past_exhibitions = Artwork.objects.filter(status=0).exclude(id__in=onnows_id_list)
    # search
    if action == 'select_action':
        artist = request.POST.get('artist', 'A-Z')
        year = request.POST.get('year', '0')
        medium = request.POST.get('medium', 'all')
        search = request.POST.get('search', '')
        # Check out the art exhibits on display
        onnows = OnNowArtwork.objects.filter(status=0)
        if artist != 'A-Z':
            onnows = onnows.filter(on_now_artwork__artist_letter=artist)
        if year != '0':
            onnows = onnows.filter(on_now_artwork__year=year)
        if medium != 'all':
            onnows = onnows.filter(on_now_artwork__medium__name=medium)
        if search:
            onnows = onnows.filter(
                Q(on_now_artwork__artist__icontains=search) | Q(on_now_artwork__title__icontains=search))
        onnows = onnows.order_by('sequence')[0:6]
        for x in onnows:
            onnows_id_list.append(x.on_now_artwork.id)

        # Inquire about previous art exhibits
        past_exhibitions = Artwork.objects.filter(status=0).exclude(id__in=onnows_id_list)
        if artist != 'A-Z':
            past_exhibitions = past_exhibitions.filter(artist_letter=artist)
        if year != '0':
            past_exhibitions = past_exhibitions.filter(year=year)
        if medium != 'all':
            past_exhibitions = past_exhibitions.filter(medium__name=medium)
        if search:
            past_exhibitions = past_exhibitions.filter(Q(artist__icontains=search) | Q(title__icontains=search))

    # Determine if the More button is displayed
    if past_exhibitions.count() > 8:
        more_flag = 'true'
    ctx['artist'] = artist
    ctx['year'] = year
    ctx['medium'] = medium
    ctx['search'] = search
    ctx['onnows'] = onnows
    ctx['past_exhibitions'] = past_exhibitions[0:8]
    ctx['more_flag'] = more_flag
    ctx['medium_list'] = Medium.objects.filter(status=0)
    ctx['user'] = user
    ctx['remind'] = remind
    return render(request, 'index_exhibition.html', ctx)


@csrf_exempt
def index_exhibition_detail(request, id):
    """exhibition_detail"""
    ctx = {}
    user = ''
    remind = []
    likeflag = 0  # 0 defaults to no thumb up
    action = request.POST.get('action')
    get_artwork = Artwork.objects.filter(status=0, id=id).first()

    # Determine if the user is logged in
    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
    if user:
        is_remind = Remind.objects.filter(remind_user=user, remind_comment__comment_artwork__id=id, status=0, flag=0).first()  # Check if there is a reminder
        if is_remind:
            is_remind.flag = 1
            is_remind.save()
    if user:
        remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    if action == 'fabulous_chat_action':
        flag = 0  # no thumb up
        id = request.POST.get('id')
        get_comment = Comment.objects.filter(id=id).first()
        get_fabulou_comment = FabulousComment.objects.filter(fabulous_Comment=get_comment, fabulousComment_user=user).first()  # Find user thumb up's comments
        if get_fabulou_comment:  # If the user has already liked the comment
            if get_fabulou_comment.status == 0:
                get_fabulou_comment.status = -1
                get_comment.fabulous_num = get_comment.fabulous_num - 1
                get_comment.save()
            else:
                get_fabulou_comment.status = 0
                get_comment.fabulous_num = get_comment.fabulous_num + 1
                get_comment.save()
                flag = 1
            get_fabulou_comment.save()
        else:  #Otherwise create a new comment like
            FabulousComment.objects.create(fabulous_Comment=get_comment, fabulousComment_user=user, status=0)
            get_comment.fabulous_num += 1
            get_comment.save()
            flag = 1
        return JsonResponse({'data': flag})

    # give the thumbs-up
    if action == 'fabulous_action':
        likeflag = request.POST.get('likeflag', '0')
        get_fabulous = Fabulous.objects.filter(fabulous_artwork=get_artwork, fabulous_user=user, status=0).first()
        # 0 For those which have not liked or canceled
        if likeflag == '0':
            # Determining the availability of data
            if get_fabulous:
                get_fabulous.status = 0
                get_fabulous.save()
            else:
                Fabulous.objects.create(fabulous_artwork=get_artwork, fabulous_user=user)
            # After liking, add 1 to the number
            if get_artwork:
                get_artwork.fabulous_number += 1
                get_artwork.save()

        else:
            if get_fabulous:
                get_fabulous.status = -1
                get_fabulous.save()
                # If user cancel the compliment, the number is reduced by 1.
                if get_artwork:
                    get_artwork.fabulous_number -= 1
                    get_artwork.fabulous_number = get_artwork.fabulous_number if get_artwork.fabulous_number < 0 else 0
                    get_artwork.save()
        return JsonResponse({'data': 'success'})

    # comment
    if action == 'new_comment':
        artwork_id = request.POST.get('artwork_id', '')
        content = request.POST.get('content', '')

        if 'uid' not in request.session:
            ctx = {
                'code': -1,
                'err': 'Please login',
            }
            return JsonResponse(ctx)
        user = User.objects.filter(id=request.session['uid'], status=0).first()
        if user:
            artwork = Artwork.objects.filter(id=artwork_id, status=0).first()
            artwork.comment_number += 1  # Comment number add 1
            artwork.save()
            comment = Comment.objects.create(
                comment_artwork=artwork,
                comment_user=user,
                comment_text=content
            )
            ctx = {
                'code': 0,
                'msg': 'success',
                'img': user.image.url,
                'username': user.name,
                'now_time': comment.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'content': content,
                'id': comment.id,
                'fabulous_num': comment.fabulous_num,
            }
        return JsonResponse(ctx)

    # Reply to comments
    if action == 'submit_reply':
        artwork_id = request.POST.get('artwork_id', '')
        content = request.POST.get('content', '')
        reply_user_id = request.POST.get('reply_user_id', '')

        if 'uid' not in request.session:
            ctx = {
                'code': -1,
                'err': 'Please login',
            }
            return JsonResponse(ctx)
        user = User.objects.filter(id=request.session['uid'], status=0).first()
        if user:
            artwork = Artwork.objects.filter(id=artwork_id, status=0).first()
            artwork.comment_number += 1  # Number of comments
            artwork.save()
            parent_comment = Comment.objects.filter(id=reply_user_id).first()
            comment = Comment.objects.create(
                parent=parent_comment,
                comment_artwork=artwork,
                comment_user=user,
                comment_text=content
            )
            ctx = {
                'code': 0,
                'msg': 'success',
                'username': user.name,
                'img': user.image.url,
                'now_time': comment.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'content': content,
                'id': comment.id,
            }
        return JsonResponse(ctx)
    # Create browsing history
    if user:
        Browse.objects.create(browse_user=user, browse_artwork=get_artwork)
        get_fabulous = Fabulous.objects.filter(fabulous_artwork=get_artwork, fabulous_user=user, status=0).first()  # Check to see if you've liked it
        if get_fabulous:
            likeflag = 1
    # Watch count plus 1
    if get_artwork:
        get_artwork.look_number += 1
        get_artwork.save()

    comment = Comment.objects.filter(comment_artwork=get_artwork, parent=None).order_by('-fabulous_num', '-create_time')  # Comments are displayed in reverse order of fabulous_num, create_time
    ctx['likeflag'] = likeflag
    ctx['artwork'] = get_artwork
    ctx['user'] = user
    ctx['comment'] = comment
    ctx['remind'] = remind
    ctx['dict'] = [{1: 0}, {2: 1}]
    return render(request, 'index_exhibition_detail.html', ctx)


@csrf_exempt
def index_news(request):
    """news page"""
    ctx = {}
    user = ''
    remind = []

    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
    if user:
        remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    news_list = News.objects.filter(status=0)
    ctx['user'] = user
    ctx['news_list'] = news_list
    ctx['remind'] = remind
    return render(request, 'index_news.html', ctx)


@csrf_exempt
def index_news_detail(request, news_id):
    """news detail"""
    ctx = {}
    user = ''
    remind = []

    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
    if user:
        remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    ctx['remind'] = remind
    ctx['news'] = News.objects.filter(status=0, id=news_id).first()
    ctx['user'] = user
    return render(request, 'index_news_detail.html', ctx)


@csrf_exempt
def index_shopping(request):
    """shopping page"""
    ctx = {}
    user = ''
    remind = []

    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
        if user:
            remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    # Search for items and sort by sales volume
    commodities = Commodity.objects.filter(status=0).order_by('-sell_number')  # Order in reverse order by sales volume
    ctx['commodities'] = commodities
    ctx['user'] = user
    ctx['remind'] = remind
    return render(request, 'index_shopping.html', ctx)


def index_shopping_detail(request, commodity_id):
    ctx = {}
    user = ''
    remind = []

    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
        if user:
            remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    action = request.POST.get('action', '')
    # add items to shopping car
    if action == 'add':
        commodity_id = request.POST.get('commodity_id', '')
        num = request.POST.get('num', '')
        commodity = Commodity.objects.filter(id=commodity_id, status=0).first()
        if user:
            shoppingCart = ShoppingCart.objects.filter(shoppingCart_user=user, shoppingCart_commodity=commodity, flag=0, status=0).first()
            if commodity.number == 0:  # Determine whether the product inventory is 0
                return JsonResponse({'code': -1, 'err': 'The inventory has been 0, can not be added'})
            if shoppingCart:  # Determine whether the user has added the product before the shopping cart
                shoppingCart.shopping_num = shoppingCart.shopping_num + int(num)
                shoppingCart.save()
            else:  # Otherwise create a new shopping cart record
                shoppingCart = ShoppingCart.objects.create(
                    shoppingCart_commodity=commodity,
                    shoppingCart_user=user,
                    shopping_num=1,
                    flag=0,
                    order_num='DD' + str(int(datetime.datetime.now().timestamp())).zfill(12)
                )
            shoppingCart.shoppingCart_commodity.number = shoppingCart.shoppingCart_commodity.number - 1
            shoppingCart.shoppingCart_commodity.save()
            return JsonResponse({'code': 0, 'msg': 'success'})

    ctx['aa'] = '<p style="color:red">fdsf</p>'
    # Search for items and sort by sales volume
    commodity = Commodity.objects.filter(status=0, id=commodity_id).first()
    ctx['commodity'] = commodity
    ctx['user'] = user
    ctx['remind'] = remind
    return render(request, 'index_shopping_detail.html', ctx)


def index_basket(request):
    """payment page"""
    ctx = {}
    remind = []
    user = ''
    if 'uid' in request.session:
        action = request.POST.get('action', '')
        user = User.objects.filter(id=request.session['uid']).first()
        if user:
            remind = Remind.objects.filter(flag=0, status=0, remind_user=user)
            is_ShoppingCart = ShoppingCart.objects.filter(shoppingCart_user=user, flag=0, status=0)
            if len(is_ShoppingCart) == 0:
                return redirect(index_shopping)
        # Add the number of items to the shopping cart interface
        if action == 'add_num':
            shoppingCart_id = request.POST.get('shoppingCart_id', '')
            money_all = 0
            shoppingCart = ShoppingCart.objects.filter(id=shoppingCart_id, status=0, flag=0).first()
            if shoppingCart.shoppingCart_commodity.number == 0:  # Judging product inventory
                return JsonResponse({'code': -1, 'err': 'The inventory has been 0, can not be added'})

            if shoppingCart:
                shoppingCart.shopping_num = shoppingCart.shopping_num + 1
                shoppingCart.save()
                shoppingCart.shoppingCart_commodity.number = shoppingCart.shoppingCart_commodity.number - 1
                shoppingCart.shoppingCart_commodity.save()

            shoppingCart_all = ShoppingCart.objects.filter(shoppingCart_user=user, status=0, flag=0)
            for i in shoppingCart_all:
                temp = i.shoppingCart_commodity.money * i.shopping_num
                money_all = temp + money_all
            return JsonResponse(
                {'code': 0, 'msg': 'success', 'num': shoppingCart.shopping_num, 'money_all': round(money_all, 2)})
        # Shopping cart interface to reduce the number of items
        if action == 'jian_num':
            shoppingCart_id = request.POST.get('shoppingCart_id', '')
            money_all = 0
            shoppingCart = ShoppingCart.objects.filter(id=shoppingCart_id, status=0, flag=0).first()
            if shoppingCart:
                shoppingCart.shopping_num = shoppingCart.shopping_num - 1
                shoppingCart.save()
                shoppingCart.shoppingCart_commodity.number = shoppingCart.shoppingCart_commodity.number + 1
                shoppingCart.shoppingCart_commodity.save()

                if shoppingCart.shopping_num == 0:
                    shoppingCart.status = -1
                    shoppingCart.save()

            shoppingCart_all = ShoppingCart.objects.filter(shoppingCart_user=user, status=0, flag=0)
            for i in shoppingCart_all:
                temp = i.shoppingCart_commodity.money * i.shopping_num
                money_all = temp + money_all

            return JsonResponse(
                {'code': 0, 'msg': 'success', 'num': shoppingCart.shopping_num, 'money_all': round(money_all, 2)})
        #  Add shopping address
        if action == 'add_address':
            gw_country_id = request.POST.get('gw_country_id', '')
            gw_city_id = request.POST.get('gw_city_id', '')
            gw_address_info = request.POST.get('gw_address_info', '')
            Address.objects.create(
                user=user,
                country=gw_country_id,
                city=gw_city_id,
                address_info=gw_address_info
            )
            return JsonResponse({'code': 0, 'msg': 'success'})
        # check out
        if action == 'checkout':
            address = request.POST.get('address', '')
            zong_monery = request.POST.get('zong_monery', '')
            address = Address.objects.filter(id=address, status=0).first()
            if user.money - float(zong_monery) < 0:  # Determine if the user's money - total amount of goods <0
                return JsonResponse({'code': -1, 'err': 'Lack of balance'})
            Order.objects.create(
                order_user=user,
                order_num='DD' + str(int(datetime.datetime.now().timestamp())).zfill(12),
                order_money=zong_monery,
                address=address
            )
            user.money = user.money - float(zong_monery)
            user.save()
            return JsonResponse({'code': 0, 'msg': 'success'})

        shoppingCart = ShoppingCart.objects.filter(shoppingCart_user=user, status=0, flag=0)
        address = Address.objects.filter(user=user, status=0)

        money_all = 0
        for i in shoppingCart:
            temp = i.shoppingCart_commodity.money * i.shopping_num
            money_all = temp + money_all
        ctx['shoppingCart'] = shoppingCart
        ctx['money_all'] = round(money_all, 2)  # Keep 2 decimal places
        ctx['address'] = address

    ctx['user'] = user
    ctx['remind'] = remind
    return render(request, 'index_basket.html', ctx)


@csrf_exempt
def index_education(request):
    """education page"""
    ctx = {}
    remind = []
    user = ''
    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()

    education_list = Education.objects.filter(status=0)
    if user:
        remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    ctx['remind'] = remind
    ctx['user'] = user
    ctx['education_list'] = education_list
    return render(request, 'index_education.html', ctx)


@csrf_exempt
def index_education_detail(request, education_id):
    """education detail"""
    ctx = {}
    user = ''
    remind = []

    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
    if user:
        remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    ctx['remind'] = remind
    ctx['education'] = Education.objects.filter(status=0, id=education_id).first()
    ctx['user'] = user
    return render(request, 'index_education_detail.html', ctx)


@csrf_exempt
def index_userinfo(request):
    """User personal information"""
    ctx = {}
    remind = []
    user = ''
    attr = []
    action = request.POST.get('action')

    if 'uid' in request.session:
        user = User.objects.filter(id=request.session['uid']).first()
        # Prevent users without data from knowing the address to access
        if not user:
            return redirect('/index_home/')

    if action == 'edit_user':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        head = request.FILES.get('head', '')  

        user.public_name = username
        user.email = email
        user.country = country
        user.city = city
        if head:
            user.image = head
        user.save()

    # Query the last 6 user browsing records, sorted by browse_artwork__id
    browses = Browse.objects.values('browse_artwork__id', 'browse_artwork__title', 'browse_artwork__img').filter(status=0, browse_user=user).distinct().order_by('-browse_artwork__id')[:6]
    for i in browses:
        d = {
            'id': i['browse_artwork__id'],
            'title': i['browse_artwork__title'],
            'img': i['browse_artwork__img']
        }
        attr.append(d)

    if user:
        remind = Remind.objects.filter(flag=0, status=0, remind_user=user)

    ctx['remind'] = remind
    ctx['user'] = user
    ctx['browses'] = attr
    return render(request, 'index_userinfo.html', ctx)
