
from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name = 'news_home'),
    path('create/', views.creates.as_view(), name = 'create'),
    path('<slug>', views.NewsDetailView.as_view(), name = 'news_detail'), # когда мы во views указываем класс, прописываем метод as_view
    path('<slug>/update', views.NewsUpdateView.as_view(), name = 'news-update'), # <int:pk> - динамеский номер записи(1,2,3,4 и т.д.), update - название url адреса для редактирования новостей
    path('<slug>/delete', views.NewsDeleteView.as_view(), name = 'news-delete')
]



