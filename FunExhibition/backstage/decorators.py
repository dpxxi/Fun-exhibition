from django.shortcuts import redirect
from .models import User


def user_required(view_func):
    """需要用户登录"""
    def wrapper(request, *args, **kwargs):
        if 'uid' not in request.session:
            return redirect('index_home')
        user = User.objects.filter(id=request.session['uid'], admin_level=1).first()
        if not user:
            return redirect('index_home')
        return view_func(request, me=user, *args, **kwargs)
    return wrapper
