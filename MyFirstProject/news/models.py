from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Articles(models.Model):   # в скобках указываем что мы все унаследуем от класса Model
    title = models.CharField('название', max_length=50) # через класс Model мы имеем доступ к дгуим классам как CharField
    anons = models.CharField('анонс', max_length=250) # CharField нужен для ввода строки
    full_text = models.TextField('Статья') # TextField нужен для ввода большего количества текста
    date = models.DateTimeField('Дата публикации') # DateTimeField нужен для отображения даты
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d', default=None, blank=True, null=True, verbose_name='Фото')

    def __str__(self): # методstr необходим для корректного отображения названий заголовков(в данном случае новостей) таблицы на сайте
        return self.title # отображаем нахвание новости(объекта)

    def get_absolute_url(self): # функция для редактирования записей
        return f'/news/{self.slug}' # после редактирования идет переадресация пользователя

    class Meta:
        verbose_name = 'Новость' # указываем названия для таблицы в единственном числе
        verbose_name_plural = 'Новости' # в множественном
        ordering = ['date'] # отбор по дате добавления записи
        indexes = [models.Index(fields=['date'])] # связка идексов и даты публикации,НАВЕРНО

    def save(self, *args, **kwargs): # функкция, которая при создании новой записи присваевает наименование slug
        self.slug = slugify(translit_to_end(self.title)) # название slug указываем по тайтлу, добавляем функцию для перевода языка
        super().save(args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

def translit_to_end(s: str) -> str: # функция для перевода title с русского на английский язык для присваевания slug
    d = { 'а' : 'a', 'б' : 'b', 'в' : 'v', 'г' : 'g', 'д' : 'd', 'е' : 'e', 'ё' : 'yo', 'ж' : 'zh', 'з' : 'z',
          'и' : 'i', 'к' : 'k', 'л' : 'l', 'm' : 'm', 'н' : 'n', 'о' : 'o', 'п' : 'p', 'р' : 'r', 'c' : 's', 'т' : 't',
          'y': 'u', 'ф' : 'f','x': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'shch', 'ь': '', 'ы': 'y', 'э': 'r', 'ю': 'yu', 'я': 'ya'
    }
    return ''.join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uplpoads_model')



