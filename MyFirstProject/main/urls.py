from django.urls import path
from . import views # привязываем папку views, чтобы вызывать методы при переходе пользователя на странцу сайта


urlpatterns = [
    path('', views.index, name = 'home'), # название нужно, для тега href, чтобы ссылаться на определенную ссылку без привязки к наименованию самого URL
    path('Laputa', views.about, name = 'Laputa')


]
