"""
URL configuration for MyFirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # include - передает задачи определенному приложению
# path - это функция, которое передает параметр, в данном случае это ссылка страницы

from django.conf import settings # подключение статичских файлов к HTML-шаблонам
from django.conf.urls.static import static # подключение статичских файлов к HTML-шаблонам

from main.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # include в данном случае передает отслеживание ссылки главной страницы папке urls в прилож main
    path('news/', include('news.urls')),
    path('users/', include('users.urls', namespace='users')), # namespace - нужен для дополнительного изолирования имен маршрутов
    path('__debug__/', include('debug_toolbar.urls')), # конечная установка debug для оптимизации сайта
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # подключение статичских файлов к HTML-шаблонам

handler404 = page_not_found