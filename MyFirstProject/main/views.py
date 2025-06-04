from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render # метод render нужен для передачи html-шаблонов
from news.forms import UploadFileForm
from news.models import UploadFiles


def index(request): # request указываем любое наименование параметра, это нужно для передачи данных из функции
    return render(request, 'main/index.html') # указываем ссылку на папку щаблона

@login_required
def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'main/about.html', {'form': form})

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')

