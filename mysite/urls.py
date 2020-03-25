"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static # static() 함수는 정적 파일을 처리하기 위해 그에 맞는 URL 패턴을 반환하는 함수
from django.conf import settings # settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체를 가리키는 reference이다.
from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 기존 URL 패턴에 static() 함수가 반환하는 URL 패턴을 추가한다.
# static(prefix, view=django.views.static.serve, **kwargs)
# 즉 settings.MEDIA_URL로 정의된 /media/ URL 요청이 오면 django.view.static.serve() 뷰 함수가 처리하고, 이 뷰 함수에 document_root = settings.MEDIA_ROOT 키워드 인자가 전달된다.
# static.serve() 함수는 개발용이고 상용에는 httpd, nginx 등의 웹 서버 프로그램을 사용한다.