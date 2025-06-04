from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404  # redirect - переадресация
from django.urls import reverse_lazy
from django.views import View

from .models import Articles # импорт таблицы, чтобы размещать ее в html-шаблоне
from .forms import ArticlesForm # импорт формы для добавление записей пользователем
from django.views.generic import DetailView, UpdateView, DeleteView, \
    FormView  # импортируем класс, которы позволяет сделать динамическое отслеживание страницы

class NewsUpdateView(UpdateView): # создаем класс для редактирования и удаления записей на сайте
    model = Articles
    template_name = 'news/create.html' # перенаправление на шаблон
    form_class = ArticlesForm # подключаем форму


class NewsDeleteView(DeleteView): # создаем класс для удаление записей
    model = Articles
    template_name = 'news/news-delete.html'
    success_url = '/news/' # переадресация пользователя после удаление записи


class NewsDetailView(DetailView):   # создаем класс, который создает динамическое отсеживанием
    model = Articles # привязываем таблицу из базы данных
    template_name = 'news/details_view.html' # указываем нужный Html-шаблон
    context_object_name = 'article2' # context_object_name присваевает все объекты в таблице, article - ключ




def news_home(request):
    print(request.GET)
    news = Articles.objects.all() # получение всех объектов из таблицы. Объкт в этом случае это новость(название,анонос,статья,дата)
    return render(request, "news/news_home.html", {'news': news}) # передача таблицы в виде параметра в шаблон


# def create(request):
#     error = ''
#     if request.method == 'POST': # создаем условие, если была отправка данных пользователем
#         form = ArticlesForm(request.POST, request.FILES)  # то создаем новую запись в виде параметра form, указываем ключовое слово POST(передача)
#         if form.is_valid(): # создаем вложенное условие на корректность вводмых данных, метод is_valid берем из ModelForm
#             form.save() # сохраняем форму/запись пользователя
#             # try:
#             #     form2 = Articles(
#             #         title = form.cleaned_data['title'],
#             #         anons=form.cleaned_data['anons'],
#             #         full_text=form.cleaned_data['full_text'],
#             #         date=form.cleaned_data['date'],
#             #         slug=form.cleaned_data['slug'],
#             #         cat = form.cleaned_data['cat']
#             #     )
#             #     form2.save()
#             return redirect('home') # после сохранение записи пользователя, мы делаем переасацию на главную страницу
#             # except:
#             #     form.add_error(None, 'Форма была неверной2')
#         else:
#         # form = ArticlesForm()
#             error = 'Форма была неверной'
#
#     form = ArticlesForm() # отображение на html-шаблоне формы для пользователя
#     data = {  # помещение параметра form и error из функции craate в словарь
#         'form': form,
#         'error': error
#     }
#     return  render(request, 'news/create.html', data) # отоюражаем Html-шаблон и словарь

class creates(FormView):
    form_class = ArticlesForm
    template_name = 'news/create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



# class creates(View):
#     def get(self, request):
#         form = ArticlesForm()
#         data = {
#             'form': form
#         }
#         return render(request, 'news/create.html', data)
#
#     def post(self, request):
#         form = ArticlesForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Форма была неверной'
#
#         data = {
#             'form': form,
#             'error': error
#         }
#         return render(request, 'news/create.html', data)
