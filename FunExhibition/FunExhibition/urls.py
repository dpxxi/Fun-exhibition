"""FunExhibition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backstage import views as b_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # admin background 
    path('index_basket/', b_view.index_basket, name='index_basket'),
    path('index_support_us/', b_view.index_support_us, name='index_support_us'),  # support_us model
    path('', b_view.index_home),  # home
    path('index_home/', b_view.index_home, name='index_home'),  # home
    path('index_exhibition/', b_view.index_exhibition, name='index_exhibition'),  # exhibition model
    path('index_exhibition_detail/<int:id>/', b_view.index_exhibition_detail, name="index_exhibition_detail"),  # exhibition_detail
    path('index_news/', b_view.index_news, name='index_news'),  # news model
    path('index_news_detail/<int:news_id>/', b_view.index_news_detail, name='index_news_detail'),  # news_detail
    path('index_shopping/', b_view.index_shopping, name='index_shopping'),  # shopping model
    path('index_shopping_detail/<int:commodity_id>/', b_view.index_shopping_detail, name='index_shopping_detail'),  # Add items to shopping cart
    path('index_education/', b_view.index_education, name='index_education'),  # education model 
    path('index_education_detail/<int:education_id>/', b_view.index_education_detail, name='index_education_detail'),  # education_detail
    path('index_userinfo/', b_view.index_userinfo, name='index_userinfo'),  # User personal information
    path('login_ajax/', b_view.login_ajax, name='login_ajax'),  # user login
    path('register_ajax/', b_view.register_ajax, name='register_ajax'),  # user register
    path('logout/', b_view.logout, name='logout'),  # user logout
    path('touch/', b_view.touch, name='touch'),  # get in touch
    path('backstage_user/', b_view.backstage_user, name='backstage_user'),  # 后台编辑user信息
    path('backstage_works/', b_view.backstage_works, name='backstage_works'),
    path('find_password/', b_view.find_password, name='find_password'),  # Find password
    path('edit_password/', b_view.edit_password, name='edit_password'),  # Reset password
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
