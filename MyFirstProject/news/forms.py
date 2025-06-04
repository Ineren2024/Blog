from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Articles, Category # импортируем таблицу, чтобы на основе таблицы пользователь мог сам добавлять записи на сайте
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea # импортируем атрибуты для формы
from django import forms

# @deconstructible
# class RussianValidator:
#     ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁйцукенгшщзхъфывапролджэячсмитьбю0123456789- '
#     code = 'russian'
#
#     def  __init__(self, message=None):
#         self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел.'
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code = self.code)

# class ArticlesForm(forms.Form):
#     title = forms.CharField(label = 'название', max_length=50, min_length=5, error_messages={'min_length': 'Ужин с мразью'},
#                             validators=[RussianValidator()])
#     anons = forms.CharField(label = 'анонс', max_length=250)
#     full_text = forms.CharField(label = 'Статья')
#     date = forms.DateTimeField(label = 'Дата публикации')
#     slug = forms.SlugField(max_length=250, label='URL')
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label= 'Категория')

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     ALLOWED_CHARS = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁйцукенгшщзхъфывапролджэячсмитьбю0123456789- '
    #
    #     if not (set(title) <= set(ALLOWED_CHARS)):
    #         raise ValidationError('Должны присутствовать')






class ArticlesForm(ModelForm): # создаем класс с названием артиклформ и в скобках указываем что мы все наследуем от класса моделформ
    class Meta: # создаем вложенный класс
        model = Articles # создаем новую форму привязываем ее к таблице артиклс
        fields = ['title', 'anons', 'full_text', 'date','slug','cat', 'photo'] # подключаем строки из таблицы артиклс


        widgets = {
            'title': TextInput(attrs={  # к строке таблицы присваеваем класс, который позволяет вводить текст пользователю на сайте
                'class': 'form-control', # стиль текста
                'placeholder': 'Название статьи' # поле ввода текста
            }),


            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'

            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'

            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'

            })
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')