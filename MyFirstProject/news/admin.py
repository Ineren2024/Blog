from django.contrib import admin


from .models import Articles # делаем импорт таблицы с файла models, чтобы иметь доступ к таблице в панели администратоора

@admin.register(Articles) # через декоратор можно сразу же присваивать классы для админ панели. то бишь мы одновременно
# регистрируем саму таблицу и добавляем к ней функционал
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title')
    ordering = ['date']
    readonly_fields = ['slug']


# admin.site.register(Articles, ArticlesAdmin) # регистрируем таблицу в панели администратора

